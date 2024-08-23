import customtkinter as ctk
from tkinter import StringVar, font

from CTkMessagebox import CTkMessagebox
from CTkTable import *

from config import db
import config.functions_grals as fn

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None
invoice_code = None


def fetch_records():
    query = ("SELECT code,description FROM activities_eco_f833 LIMIT 50")
    result = db.fetchRecords(query)
    print(result)
    return result


def get_record(record):
    query = f"SELECT * FROM activities_eco_f833 WHERE code = '{record}'"
    result = db.fetchRecord(query)
    print("valor devuelto: ", result)
    return result


def select_activity(objeto, e):
    # 'e' tiene los datos pasados por el widget tabla de donde se hizo el  Click
    global selected_row
    global activity_code

    if selected_row is not None:
        objeto.deselect_row(selected_row)

    objeto.select_row(e["row"])
    selected_row = e["row"]
    activity_code = objeto.get(selected_row, 0)
    print(" CODE Activity Selected: ", invoice_code)
    print(e)


# =================
#  Clase Principal
# =================
class ActivitiesWindow:
    def __init__(self, root):
        self.root = ctk.CTkToplevel()
        self.root.title('Actividades Económicas')
        self.root.grab_set()
        self.root.config(padx=10, pady=10)
        # Evitar que la ventana se expanda
        self.root.resizable(False, False)
        # Evitar que la ventana se cierre
        # self.root.protocol("WM_DELETE_WINDOW", lambda: None)

    def agregar_widget(self, widget):
        widget.pack()

    def agregar_widget2(self, widget, **kwargs):
        widget.grid(**kwargs)

    def cerrar_ventana(self):
        self.root.winfo_parent()
        self.root.destroy()

    def cambiar_titulo(self, titulo=None):
        self.root.title(titulo)


# =================
# Clase Secundaria.
# =================
# En esta clase, los métodos configuran los widget que se muestran en
# las distintas ventanas relacionadas con los comprobantes.
class ActivitiesWidgets:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal

    def listForm(self):
        marco_search = ctk.CTkFrame(master=self.ventana_principal.root,
                                    width=518,
                                    height=50,
                                    corner_radius=0,



                                    )

        search_entry = ctk.CTkEntry(master=marco_search,
                                    width=360,
                                    )
        search_btn = ctk.CTkButton(master=marco_search,
                                   width=120,
                                   text='Buscar')
        # Agregar widget creados en la Clase Principal
        self.ventana_principal.agregar_widget2(marco_search)
        search_entry.grid(row=0, column=0, pady= 10, padx=10, sticky='e')
        search_btn.grid(row=0, column=1, padx=10, pady=10, sticky='w')


        marco = ctk.CTkScrollableFrame(master=self.ventana_principal.root,
                                       width=500,
                                       height=250,
                                       corner_radius=0,
                                       border_width=1,
                                       border_color="black",
                                       scrollbar_fg_color="black",
                                       )

        marco.grid_rowconfigure(0, weight=1)
        marco.grid_columnconfigure(0, weight=1)
        # Leer comprobantes desde la base de datos (DB)
        value = fetch_records()
        # Crear tabla con los comprobantes existentes en la DB
        table = CTkTable(master=marco,
                         row=len(value),
                         column=2,
                         values=value,
                         border_width=0,
                         corner_radius=0,
                         command=lambda e: select_activity(table, e),
                         )

        table.edit_column(0, width=250)
        table.edit_column(1, width=250, anchor="w")
        table.grid(row=0, column=0, )

        # Agregar widget creado en la Clase Principal
        self.ventana_principal.agregar_widget2(marco)

        # Botones de Acciones
        marco_btns = ctk.CTkFrame(master=self.ventana_principal.root,
                                  width=300,
                                  )

        cancel_btn = ctk.CTkButton(marco_btns, text="Cancelar", width=100,
                                   command=lambda: self.ventana_principal.cerrar_ventana())
        select_btn = ctk.CTkButton(marco_btns, text="Seleccionar", width=100,
                                   command=lambda: invoice("edit", self.ventana_principal)
                                   if selected_row is not None
                                   else CTkMessagebox(title="Error",
                                                      message="Debe seleccionar un Comprobante para editar",
                                                      icon="cancel"),
                                   )

        marco_btns.grid()

        cancel_btn.grid(row=1, column=1, padx=5, pady=5, )
        select_btn.grid(row=1, column=2, padx=5, pady=5, )

        # Agregar widget creados en la Clase Principal
        self.ventana_principal.agregar_widget2(marco_btns)

    def dataForm(self, opt=None):
        datos = {}
        # opt="new" - Muestra el formulario vacío.
        # opt="edit" - Muestra el formulario con los datos del registro seleccionado para ser editado
        if opt == "new":
            titulo_ventana = "Nuevo Comprobante"
            self.ventana_principal.cambiar_titulo(titulo_ventana)
            # Inicializa el dict datos[...] con las Variables del Formulario
            datos = {
                "Id": None,
                "Code": StringVar(),
                "Description": StringVar(),
                "Obs": StringVar(),
                "TypeRet": StringVar(),
                "TypeCert": StringVar(),
                "TypeDC": StringVar(),
                "Op1": StringVar(),
                "Op2": StringVar(),
                "Op3": StringVar(),
                "Op4": StringVar(),
                "CodeA": StringVar(),
                "CodeB": StringVar(),
                "CodeC": StringVar(),
                "CodeE": StringVar(),
                "CodeM": StringVar(),
                "CodeT": StringVar(),
                "CodeO": StringVar(),
            }

        elif opt == "edit":
            titulo_ventana = "Editar Comprobante"
            self.ventana_principal.cambiar_titulo(titulo_ventana)
            print("Editar Code: ", selected_row, " - ", invoice_code)
            # Recupera Valores del Formulario desde la DB y se carga al dict datos[...]
            result = get_record(invoice_code)
            datos = {
                "Id": StringVar(value=result[0]),
                "Code": StringVar(value=result[1]),
                "Description": StringVar(value=result[2]),
                "Obs": StringVar(value=result[3]),
                "TypeRet": StringVar(value=result[4]),
                "TypeCert": StringVar(value=result[5]),
                "TypeDC": StringVar(value=result[6]),
                "Op1": StringVar(value=result[7]),
                "Op2": StringVar(value=result[8]),
                "Op3": StringVar(value=result[9]),
                "Op4": StringVar(value=result[10]),
                "CodeA": StringVar(value=result[11]),
                "CodeB": StringVar(value=result[12]),
                "CodeC": StringVar(value=result[13]),
                "CodeE": StringVar(value=result[14]),
                "CodeM": StringVar(value=result[15]),
                "CodeT": StringVar(value=result[16]),
                "CodeO": StringVar(value=result[17]),
            }

        else:
            print("ERROR: opcion no valida")

        # Crea el frame con el formulario y lo añade a la ventana
        marco = ctk.CTkFrame(master=self.ventana_principal.root,
                             width=420,
                             height=420,
                             corner_radius=0,
                             border_width=1,
                             border_color="black",
                             )

        invoiceCode_label = ctk.CTkLabel(marco, text="Código", ).place(x=10, y=10)
        invoiceCode_entry = ctk.CTkEntry(marco, textvariable=datos['Code'], width=47,
                                         validate="focusout", ).place(x=110, y=10)
        invoiceDescription_label = ctk.CTkLabel(marco, text="Descripción", ).place(x=10, y=40)
        invoiceDescription_entry = ctk.CTkEntry(marco, textvariable=datos['Description'], width=180).place(x=110, y=40)
        invoiceObs_label = ctk.CTkLabel(marco, text="Observaciones:", ).place(x=10, y=70)
        invoiceObs_entry = ctk.CTkEntry(marco, textvariable=datos['Obs'], width=300).place(x=110, y=70)

        invoiceTypeRet_checkbox = ctk.CTkCheckBox(marco, text="Retencion", variable=datos['TypeRet'],
                                                  onvalue="on",
                                                  offvalue="off").place(x=10, y=115)
        invoiceTypeCert_checkbox = ctk.CTkCheckBox(marco, text="Certificado", variable=datos['TypeCert'],
                                                   onvalue="on",
                                                   offvalue="off").place(x=110, y=115)

        invoiceTypeDC_label = ctk.CTkLabel(marco, text="Débito o Crédito (D/C)", )
        invoiceTypeDC_label.place(x=(170 - len(invoiceTypeDC_label.cget("text")) * 6), y=145)
        invoiceTypeDC_entry = ctk.CTkEntry(marco, textvariable=datos['TypeDC'], width=25).place(x=180, y=145)
        invoiceOp1_label = ctk.CTkLabel(marco, text="  Tiene Numeración (S/N) ", )
        invoiceOp1_label.place(x=(170 - len(invoiceOp1_label.cget("text")) * 6), y=175)
        invoiceOp1_entry = ctk.CTkEntry(marco, textvariable=datos['Op1'], width=25).place(x=180, y=175)
        invoiceOp2_label = ctk.CTkLabel(marco, text=" Activo en Compras (S/N) ", )
        invoiceOp2_label.place(x=(170 - len(invoiceOp2_label.cget("text")) * 6), y=205)
        invoiceOp2_entry = ctk.CTkEntry(marco, textvariable=datos['Op2'], width=25).place(x=180, y=205)

        invoiceOp3_label = ctk.CTkLabel(marco, text=" Activo en Ventas (S/N)", )
        invoiceOp3_label.place(x=(170 - len(invoiceOp3_label.cget("text")) * 6), y=235)
        print(180 - len(invoiceOp3_label.cget("text")))
        invoiceOp3_entry = ctk.CTkEntry(marco, textvariable=datos['Op3'], width=25).place(x=180, y=235)
        invoiceOp4_checkbox = ctk.CTkCheckBox(marco, text="Emitido por Controlador Fiscal", variable=datos['Op4'],
                                              onvalue="on",
                                              offvalue="off").place(x=10, y=265)

        invoiceCodes_label = ctk.CTkLabel(marco, text="Cód. s/ RG 3685 (AFIP):", font=font_widgets, ).place(x=255,
                                                                                                            y=115)
        invoiceCodeA_label = ctk.CTkLabel(marco, text="Comprobante Tipo A", ).place(x=240, y=145)
        invoiceCodeA_entry = ctk.CTkEntry(marco, textvariable=datos['CodeA'], width=40).place(x=370, y=145)
        invoiceCodeB_label = ctk.CTkLabel(marco, text="Comprobante Tipo B", ).place(x=240, y=175)
        invoiceCodeB_entry = ctk.CTkEntry(marco, textvariable=datos['CodeB'], width=40).place(x=370, y=175)
        invoiceCodeC_label = ctk.CTkLabel(marco, text="Comprobante Tipo C", ).place(x=240, y=205)
        invoiceCodeC_entry = ctk.CTkEntry(marco, textvariable=datos['CodeC'], width=40).place(x=370, y=205)
        invoiceCodeE_label = ctk.CTkLabel(marco, text="Comprobante Tipo E", ).place(x=240, y=235)
        invoiceCodeE_entry = ctk.CTkEntry(marco, textvariable=datos['CodeE'], width=40).place(x=370, y=235)
        invoiceCodeM_label = ctk.CTkLabel(marco, text="Comprobante Tipo M", ).place(x=240, y=265)
        invoiceCodeM_entry = ctk.CTkEntry(marco, textvariable=datos['CodeM'], width=40).place(x=370, y=265)
        invoiceCodeT_label = ctk.CTkLabel(marco, text="Comprobante Tipo T", ).place(x=240, y=295)
        invoiceCodeT_entry = ctk.CTkEntry(marco, textvariable=datos['CodeT'], width=40).place(x=370, y=295)
        invoiceCodeO_label = ctk.CTkLabel(marco, text="Otros", ).place(x=240, y=325)
        invoiceCodeO_entry = ctk.CTkEntry(marco, textvariable=datos['CodeO'], width=40).place(x=370, y=325)

        clear_btn = ctk.CTkButton(marco, text="Vaciar", width=80,
                                  command=lambda: limpiar_form(marco))
        cancel_btn = ctk.CTkButton(marco, text="Cancelar", width=80,
                                   command=lambda: self.ventana_principal.cerrar_ventana())
        ok_btn = ctk.CTkButton(marco, text="Guardar", width=120,
                               command=lambda: validation_form(self, datos, opt)
                               )

        clear_btn.place(x=12, y=370)
        cancel_btn.place(x=205, y=370)
        ok_btn.place(x=290, y=370)

        self.ventana_principal.agregar_widget(marco)

        def validation_form(self, dataForm, optt):

            if dataForm['Id'] is not None:
                value = dataForm['Id'].get()  # Accede al método get() aquí
            else:
                value = ""  # Maneja el caso en que dataForm['Id'] es None, o sea cuando opt = "new"

            # Recuperando Datos Del Formulario
            datos = {
                "Id": value,
                "Code": dataForm['Code'].get().upper(),
                "Description": dataForm['Description'].get(),
                "Obs": dataForm['Obs'].get(),
                "TypeRet": dataForm['TypeRet'].get(),
                "TypeCert": dataForm['TypeCert'].get(),
                "TypeDC": dataForm['TypeDC'].get().upper(),
                "Op1": dataForm['Op1'].get().upper(),
                "Op2": dataForm['Op2'].get().upper(),
                "Op3": dataForm['Op3'].get().upper(),
                "Op4": dataForm['Op4'].get(),
                "CodeA": dataForm['CodeA'].get(),
                "CodeB": dataForm['CodeB'].get(),
                "CodeC": dataForm['CodeC'].get(),
                "CodeE": dataForm['CodeE'].get(),
                "CodeM": dataForm['CodeM'].get(),
                "CodeT": dataForm['CodeT'].get(),
                "CodeO": dataForm['CodeO'].get(),
            }
            error = {}
            count = 0
            msg = ""

            # Validando los Datos del Formulario
            if not fn.validate_txt(datos['Code'], 1, 4, str):
                count += 1
                error[count] = "Código de Comprobante debe contener 1-4 caracteres."

            if not fn.validate_txt(datos['Description'], 1, 24, str):
                count += 1
                error[count] = "Descripción de Comprobante debe contener 1-24 caracteres."

            if not fn.validar_string(datos['TypeDC'], "DCdc"):
                count += 1
                error[count] = "Debe indicar Débito o Crédito (D/C)."

            if not fn.validar_string(datos['Op1'], "SNsn "):
                count += 1
                error[count] = "Debe indicar si tiene numeración (S/N)."

            if not fn.validar_string(datos['Op2'], "SNsn"):
                count += 1
                error[count] = "Debe indicar si esta activo para Compras (S/N)."

            if not fn.validar_string(datos['Op3'], "SNsn"):
                count += 1
                error[count] = "Debe indicar si esta activo para Ventas (S/N)."

            print("'Resultado de la Validación'")
            print(datos, "Cantidad de elementos:      ", len(datos))
            print(error, "Cant. Errores de Validacón: ", len(error))

            if len(error) > 0:
                for txt, i in enumerate(error):
                    msg += "* " + error[i] + "\n"
                CTkMessagebox(title="Error", message=msg, icon="cancel")
            else:
                print("Se validaron todos los Datos.")
                if optt == "new":
                    save = save_record(datos)
                    if save:
                        CTkMessagebox(title="Ok", message="El registro fue guardado correctamente.", icon="check", )
                        self.ventana_principal.cerrar_ventana()
                    else:
                        CTkMessagebox(title="Error", message="Ha ocurrido un error.", icon="cancel")
                elif optt == "edit":
                    update = update_record(datos)

        def limpiar_form(widget):
            widgets = widget.winfo_children()
            print(widgets)
            for entry in widgets:
                if isinstance(entry, ctk.CTkEntry):
                    entry.delete(0, ctk.END)  # Borrar el valor actual
                    entry.insert(0, '')  # Insertar el nuevo valor
                    # print(entry.winfo_name())


# ===================================================================
#  Métodos que manejan la creación de widget de las distintas ventanas
# ===================================================================

def create_window():
    # Crear la ventana principal
    root = ctk.CTk()
    ventana_principal = ActivitiesWindow(root)
    # Crear y agregar widgets desde la clase secundaria
    crear_widgets = ActivitiesWidgets(ventana_principal)
    return crear_widgets


def activities(opt=None, ventana_principal=None):
    crear_widgets = create_window()
    crear_widgets.listForm()


if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    activities()
    app.mainloop()
