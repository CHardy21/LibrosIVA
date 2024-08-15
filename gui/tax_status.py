import customtkinter as ctk
from tkinter import StringVar, font

from CTkMessagebox import CTkMessagebox
from CTkTable import *

from config import db
import config.functions_grals as fn

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None
tax_status_code = None


def save_record(datos):
    print(datos)
    query = """INSERT INTO tax_status (code, description, observations, type_ret, type_cert, type_dc, active_buy, 
    active_sell, numeration, c_fiscal, code_a, code_b, code_c, code_e, code_m, code_t, code_o) VALUES (?, ?, ?, ?, ?, 
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    values = (datos['Code'], datos['Description'], datos['Obs'], datos['TypeRet'], datos['TypeCert'], datos['TypeDC'],
              datos['Op1'], datos['Op2'], datos['Op3'], datos['Op4'], datos['CodeA'], datos['CodeB'], datos['CodeC'],
              datos['CodeE'], datos['CodeM'], datos['CodeT'], datos['CodeO'])

    result = db.insertRecord(query, values)
    if result:
        return True


def update_record(datos):
    print(datos)
    query = """
        UPDATE tax_status
        SET code = ?, description = ?, observations = ?, type_ret = ?, type_cert = ?, type_dc = ?,
            active_buy = ?, active_sell = ?, numeration = ?, c_fiscal = ?, code_a = ?, code_b = ?,
            code_c = ?, code_e = ?, code_m = ?, code_t = ?, code_o = ?
        WHERE id = ?
    """
    values = (datos['Code'], datos['Description'], datos['Obs'], datos['TypeRet'], datos['TypeCert'],
              datos['TypeDC'], datos['Op1'], datos['Op2'], datos['Op3'], datos['Op4'], datos['CodeA'],
              datos['CodeB'], datos['CodeC'], datos['CodeE'], datos['CodeM'], datos['CodeT'],
              datos['CodeO'], datos['Id'])
    result = db.updateRecord(query, values)

    if result:
        return True


def fetch_records():
    query = "SELECT code, description FROM tax_status"
    result = db.fetchRecords(query)
    print("fetchall: ", result)
    return result


def get_record(record):
    query = f"SELECT * FROM tax_status WHERE code = '{record}'"
    result = db.fetchRecord(query)
    print("fetchone: ", result)
    return result


def select_tax_status(objeto, e):
    # 'e' tiene los datos pasados por el widget tabla de donde se hizo el Click
    global selected_row
    global tax_status_code

    if selected_row is not None:
        objeto.deselect_row(selected_row)

    objeto.select_row(e["row"])
    selected_row = e["row"]
    tax_status_code = objeto.get(selected_row, 0)
    print(" CODE Tax Status Selected: ", tax_status_code)
    print(e)


def delete_tax_status(self):
    print("Eliminar Registro: ", tax_status_code)
    # query = f"DELETE FROM invoices WHERE code='{tax_status_code}'"
    query = ""
    result = db.removeRecord(query)
    if result:
        CTkMessagebox(title="Ok", message="El registro fue borrado correctamente.", icon="check", sound=True)
        self.ventana_principal.cerrar_ventana()


# =================
#  Clase Principal
# =================
class TaxStatusWindow:
    def __init__(self, root):
        self.root = ctk.CTkToplevel()
        self.root.title('Condiciones Fiscales')
        self.root.grab_set()
        self.root.config(padx=10, pady=10)

    def agregar_widget(self, widget):
        widget.pack()

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
class TaxStatusWidgets:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal

    def listForm(self):
        marco = ctk.CTkScrollableFrame(master=self.ventana_principal.root,
                                       width=300,
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
                         command=lambda e: select_tax_status(table, e),
                         )

        table.edit_column(0, width=50)
        table.edit_column(1, width=250, anchor="w")
        table.grid(row=0, column=0, )

        # Agregar widget creado en la Clase Principal
        self.ventana_principal.agregar_widget(marco)

        # Botones de Acciones
        marco_btns = ctk.CTkFrame(master=self.ventana_principal.root,
                                  width=300,
                                  )

        cancel_btn = ctk.CTkButton(marco_btns, text="Cancelar", width=100,
                                   command=lambda: self.ventana_principal.cerrar_ventana())
        delete_btn = ctk.CTkButton(marco_btns, text="Borrar", width=100,
                                   command=lambda: delete_tax_status(self)
                                   if selected_row is not None
                                   else CTkMessagebox(title="Error",
                                                      message="Debe seleccionar un Comprobante para Borrar",
                                                      icon="cancel"),
                                   )
        new_btn = ctk.CTkButton(marco_btns, text="Nuevo", width=100,
                                command=lambda: tax_status("new", self.ventana_principal), )
        edit_btn = ctk.CTkButton(marco_btns, text="Editar", width=100,
                                 command=lambda: tax_status("edit", self.ventana_principal)
                                 if selected_row is not None
                                 else CTkMessagebox(title="Error",
                                                    message="Debe seleccionar un Comprobante para editar",
                                                    icon="cancel"),
                                 )

        marco_btns.pack(pady=15)

        delete_btn.grid(row=1, column=0, padx=15, pady=5, )
        cancel_btn.grid(row=1, column=1, padx=5, pady=5, )
        edit_btn.grid(row=1, column=2, padx=5, pady=5, )
        new_btn.grid(row=1, column=3, padx=5, pady=5, )

        # Agregar widget creados en la Clase Principal
        self.ventana_principal.agregar_widget(marco_btns)

    def dataForm(self, opt=None):
        datos = {}
        # opt="new" - Muestra el formulario vacío.
        # opt="edit" - Muestra el formulario con los datos del registro seleccionado para ser editado
        if opt == "new":
            titulo_ventana = "Nueva Condición Fiscal"
            self.ventana_principal.cambiar_titulo(titulo_ventana)
            # Inicializa el dict datos[...] con las Variables del Formulario
            datos = {
                'id': None,
                'code': StringVar(),
                'description': StringVar(),
                'detail_buy': StringVar(),
                'detail_sell': StringVar(),
                'monotributo': StringVar(),
                'magnetic_bracket': StringVar(),
            }

        elif opt == "edit":
            titulo_ventana = "Editar Condición Fiscal"
            self.ventana_principal.cambiar_titulo(titulo_ventana)
            print("Editar Code: ", selected_row, " - ", tax_status_code)
            # Recupera Valores del Formulario desde la DB y se carga al dict datos[...]
            result = get_record(tax_status_code)
            datos = {
                'id': StringVar(value=result[0]),
                'code': StringVar(value=result[1]),
                'description': StringVar(value=result[2]),
                'detail_buy': StringVar(value=result[3]),
                'detail_sell': StringVar(value=result[4]),
                'monotributo': StringVar(value=result[5]),
                'magnetic_bracket': StringVar(value=result[6]),
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

        code_label = ctk.CTkLabel(marco, text="Código", ).place(x=10, y=10)
        code_entry = ctk.CTkEntry(marco, textvariable=datos['code'], width=47,
                                  validate="focusout", ).place(x=110, y=10)
        description_label = ctk.CTkLabel(marco, text="Descripción", ).place(x=10, y=40)
        description_entry = ctk.CTkEntry(marco, textvariable=datos['description'], width=180).place(x=110, y=40)
        # obs_label = ctk.CTkLabel(marco, text="Observaciones:", ).place(x=10, y=70)
        # invoiceObs_entry = ctk.CTkEntry(marco, textvariable=datos['Obs'], width=300).place(x=110, y=70)
        #
        # invoiceTypeRet_checkbox = ctk.CTkCheckBox(marco, text="Retencion", variable=datos['TypeRet'],
        #                                           onvalue="on",
        #                                           offvalue="off").place(x=10, y=115)
        # invoiceTypeCert_checkbox = ctk.CTkCheckBox(marco, text="Certificado", variable=datos['TypeCert'],
        #                                            onvalue="on",
        #                                            offvalue="off").place(x=110, y=115)
        #
        # invoiceTypeDC_label = ctk.CTkLabel(marco, text="Débito o Crédito (D/C)", )
        # invoiceTypeDC_label.place(x=(170 - len(invoiceTypeDC_label.cget("text")) * 6), y=145)
        # invoiceTypeDC_entry = ctk.CTkEntry(marco, textvariable=datos['TypeDC'], width=25).place(x=180, y=145)
        # invoiceOp1_label = ctk.CTkLabel(marco, text="  Tiene Numeración (S/N) ", )
        # invoiceOp1_label.place(x=(170 - len(invoiceOp1_label.cget("text")) * 6), y=175)
        # invoiceOp1_entry = ctk.CTkEntry(marco, textvariable=datos['Op1'], width=25).place(x=180, y=175)
        # invoiceOp2_label = ctk.CTkLabel(marco, text=" Activo en Compras (S/N) ", )
        # invoiceOp2_label.place(x=(170 - len(invoiceOp2_label.cget("text")) * 6), y=205)
        # invoiceOp2_entry = ctk.CTkEntry(marco, textvariable=datos['Op2'], width=25).place(x=180, y=205)
        # invoiceOp3_label = ctk.CTkLabel(marco, text=" Activo en Ventas (S/N)", )
        # invoiceOp3_label.place(x=(170 - len(invoiceOp3_label.cget("text")) * 6), y=235)
        # print(180 - len(invoiceOp3_label.cget("text")))
        # invoiceOp3_entry = ctk.CTkEntry(marco, textvariable=datos['Op3'], width=25).place(x=180, y=235)
        # invoiceOp4_checkbox = ctk.CTkCheckBox(marco, text="Emitido por Controlador Fiscal", variable=datos['Op4'],
        #                                       onvalue="on",
        #                                       offvalue="off").place(x=10, y=265)
        #
        # invoiceCodes_label = ctk.CTkLabel(marco, text="Cód. s/ RG 3685 (AFIP):", font=font_widgets, ).place(x=255,
        #                                                                                                     y=115)
        # invoiceCodeA_label = ctk.CTkLabel(marco, text="Comprobante Tipo A", ).place(x=240, y=145)
        # invoiceCodeA_entry = ctk.CTkEntry(marco, textvariable=datos['CodeA'], width=40).place(x=370, y=145)
        # invoiceCodeB_label = ctk.CTkLabel(marco, text="Comprobante Tipo B", ).place(x=240, y=175)
        # invoiceCodeB_entry = ctk.CTkEntry(marco, textvariable=datos['CodeB'], width=40).place(x=370, y=175)
        # invoiceCodeC_label = ctk.CTkLabel(marco, text="Comprobante Tipo C", ).place(x=240, y=205)
        # invoiceCodeC_entry = ctk.CTkEntry(marco, textvariable=datos['CodeC'], width=40).place(x=370, y=205)
        # invoiceCodeE_label = ctk.CTkLabel(marco, text="Comprobante Tipo E", ).place(x=240, y=235)
        # invoiceCodeE_entry = ctk.CTkEntry(marco, textvariable=datos['CodeE'], width=40).place(x=370, y=235)
        # invoiceCodeM_label = ctk.CTkLabel(marco, text="Comprobante Tipo M", ).place(x=240, y=265)
        # invoiceCodeM_entry = ctk.CTkEntry(marco, textvariable=datos['CodeM'], width=40).place(x=370, y=265)
        # invoiceCodeT_label = ctk.CTkLabel(marco, text="Comprobante Tipo T", ).place(x=240, y=295)
        # invoiceCodeT_entry = ctk.CTkEntry(marco, textvariable=datos['CodeT'], width=40).place(x=370, y=295)
        # invoiceCodeO_label = ctk.CTkLabel(marco, text="Otros", ).place(x=240, y=325)
        # invoiceCodeO_entry = ctk.CTkEntry(marco, textvariable=datos['CodeO'], width=40).place(x=370, y=325)

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
                    print("La edicion fue exiosa (Ahora cree la funcion update_record()  :)")
                    print(datos)
                    update = update_record(datos)
                    if update:
                        CTkMessagebox(title="Ok", message="El registro fue Actualizado correctamente.", icon="check", )
                        self.ventana_principal.cerrar_ventana()
                    else:
                        CTkMessagebox(title="Error", message="Ha ocurrido un error.", icon="cancel")

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
    ventana_principal = TaxStatusWindow(root)
    # Crear y agregar widgets desde la clase secundaria
    crear_widgets = TaxStatusWidgets(ventana_principal)
    return crear_widgets


def tax_status(opt=None, ventana_principal=None):
    match opt:
        case "new":
            # Cerrar la ventana actual
            if ventana_principal is not None:
                ventana_principal.cerrar_ventana()
            crear_widgets = create_window()
            crear_widgets.dataForm("new")

        case "edit":
            # Cerrar la ventana actual
            ventana_principal.cerrar_ventana()
            crear_widgets = create_window()
            crear_widgets.dataForm("edit")

        case _:
            crear_widgets = create_window()
            crear_widgets.listForm()


if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    tax_status()
    app.mainloop()
