import customtkinter as ctk
from tkinter import StringVar, font

from CTkMessagebox import CTkMessagebox
from CTkTable import *

from config import db
import gui.invoices_functions as validar

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None


def saveRecord(datos):
    print(datos)

    # data.insertRecord(item_name=item_name.get(), item_price=item_amt.get(), purchase_date=transaction_date.get())


def fetch_records():
    query = "SELECT CODE,DESCRIPTION FROM invoices"
    result = db.fetchRecord(query)
    print(result)
    return result

def get_records(record):
    query = f"SELECT * FROM invoices WHERE code = '{record}'"
    result = db.fetchRecord(query)

    print("valor devuelto: ", result)
    return result

def select_invoice(objeto, e):
    print(e)
    global selected_row
    global invoice_code

    if selected_row != None:
        objeto.deselect_row(selected_row)

    objeto.select_row(e["row"])
    selected_row = e["row"]
    invoice_code = objeto.get(selected_row, 0)
    print(" Click en Row:", selected_row, "\n CODE Invoice: ", invoice_code)


# =================
#  Clase Principal
# =================
class InvoiceWindow:
    def __init__(self, root):
        self.root = ctk.CTkToplevel()
        self.root.title('Comprobantes')
        self.root.grab_set()
        self.root.config(padx=10, pady=10)

    def agregar_widget(self, widget):
        widget.pack()

    def cerrar_ventana(self):
        self.root.destroy()

    def cambiar_titulo(self, titulo=None):
        self.root.title(titulo)


# =================
# Clase Secundaria.
# =================
# En esta clase los métodos configuran los widget que se muestran en
# las distintas ventanas relacionadas con los comprobantes.
class InvoiceWidgets:
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
                         command=lambda e: select_invoice(table, e),
                         )
        table.edit_column(0, width=50)
        table.edit_column(1, width=250, anchor="w")
        table.grid(row=0, column=0, )

        # Agregar widget creados en la Clase Principal
        self.ventana_principal.agregar_widget(marco)

        # Botones de Acciones
        marco_btns = ctk.CTkFrame(master=self.ventana_principal.root,
                                  width=300,
                                  )

        cancel_btn = ctk.CTkButton(marco_btns, text="Cancelar", width=100,
                                   command=lambda: self.ventana_principal.cerrar_ventana())
        new_btn = ctk.CTkButton(marco_btns, text="Nuevo", width=100,
                                command=lambda: invoice("new", self.ventana_principal), )
        edit_btn = ctk.CTkButton(marco_btns, text="Editar", width=100,
                                 command=lambda: invoice("edit", self.ventana_principal)
                                 if selected_row is not None
                                 else CTkMessagebox(title="Error",
                                                    message="Debe seleccionar un Comprobante para editar",
                                                    icon="cancel"),
                                 )
        delete_btn = ctk.CTkButton(marco_btns, text="Eliminar", width=100, )

        marco_btns.pack(pady=15)

        cancel_btn.grid(row=1, column=0, padx=5, pady=5, )
        edit_btn.grid(row=1, column=1, padx=5, pady=5, )
        new_btn.grid(row=1, column=2, padx=5, pady=5, )

        # Agregar widget creados en la Clase Principal
        self.ventana_principal.agregar_widget(marco_btns)

    def dataForm(self, opt=None):
        datos = {}
        if opt == "new":
            titulo_ventana = "Nuevo Comprobante"
            self.ventana_principal.cambiar_titulo(titulo_ventana)
            # Variables del Formulario
            datos = {
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
            # Recupera Valores del Formulario desde la Base de Datos
            result = get_records(invoice_code)
            #
            # tuplas = [(3, 'FAC1', 'Factura', None, 0, 0, 'D', 'S', 'S', 'S', 0, 1, 6, 11, None, 51, None, 99)]
            #
            # # Lista de claves
            # claves = ['id', 'Code', 'Description', 'Obs', 'TypeRet', 'TypeCert', 'TypeDC', 'Op1', 'Op2',
            #           'Op3', 'Op4', 'CodeA', 'campo13', 'campo14', 'campo15', 'campo16', 'campo17', 'campo18']
            # # Crear el diccionario
            # data = {clave: valor for clave, valor in zip(claves, result[0])}
            # print(">>> ", result[0][2])
            datos = {
                "id": StringVar(value=result[0][0]),
                "Code": StringVar(value=result[0][1]),
                "Description": StringVar(value=result[0][2]),
                "Obs": StringVar(value=result[0][3]),
                "TypeRet": StringVar(value=result[0][4]),
                "TypeCert": StringVar(value=result[0][5]),
                "TypeDC": StringVar(value=result[0][6]),
                "Op1": StringVar(value=result[0][7]),
                "Op2": StringVar(value=result[0][8]),
                "Op3": StringVar(value=result[0][9]),
                "Op4": StringVar(value=result[0][10]),
                "CodeA": StringVar(value=result[0][11]),
                "CodeB": StringVar(value=result[0][12]),
                "CodeC": StringVar(value=result[0][13]),
                "CodeE": StringVar(value=result[0][14]),
                "CodeM": StringVar(value=result[0][15]),
                "CodeT": StringVar(value=result[0][16]),
                "CodeO": StringVar(value=result[0][17]),
            }
            print("=> ", datos)
        else:
            print("ERROR: opcion no valida")

        # Crea el frame y añádelo a la ventana
        marco = ctk.CTkFrame(master=self.ventana_principal.root,
                             width=420,
                             height=420,
                             corner_radius=0,
                             border_width=1,
                             border_color="black",
                             )
        # marco.pack(padx=5, pady=5)

        invoiceCode_label = ctk.CTkLabel(marco, text="Código", ).place(x=10, y=10)
        invoiceCode_entry = ctk.CTkEntry(marco, textvariable=datos['Code'], width=40,
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

        #  command=lambda: selectInvoice()
        clear_btn = ctk.CTkButton(marco, text="Borrar", width=80, )
        cancel_btn = ctk.CTkButton(marco, text="Cancelar", width=80,
                                   command=lambda: self.ventana_principal.cerrar_ventana())
        ok_btn = ctk.CTkButton(marco, text="Guardar", width=120,
                               command=lambda: validation_form(self, datos)
                               )

        clear_btn.place(x=12, y=370)
        cancel_btn.place(x=205, y=370)
        ok_btn.place(x=290, y=370)

        self.ventana_principal.agregar_widget(marco)

        def validation_form(self, dataForm):
            # Recuperando Datos Del Formulario
            datos = {
                "Code": dataForm['Code'].get(),
                "Description": dataForm['Description'].get(),
                "Obs": dataForm['Obs'].get(),
                "TypeRet": dataForm['TypeRet'].get(),
                "TypeCert": dataForm['TypeCert'].get(),
                "TypeDC": dataForm['TypeDC'].get(),
                "Op1": dataForm['Op1'].get(),
                "Op2": dataForm['Op2'].get(),
                "Op3": dataForm['Op3'].get(),
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
            if not validar.validate_txt(datos['Code'], 1, 4, str):
                count += 1
                error[count] = "Código de Comprobante debe contener 1-4 caracteres."

            if not validar.validate_txt(datos['Description'], 1, 24, str):
                count += 1
                error[count] = "Descripción de Comprobante debe contener 1-24 caracteres."

            if not validar.validar_string(datos['TypeDC'], "DCdc"):
                count += 1
                error[count] = "Debe indicar Débito o Crédito (D/C)."

            if not validar.validar_string(datos['Op1'], "SNsn "):
                count += 1
                error[count] = "Debe indicar si tiene numeración (S/N)."

            if not validar.validar_string(datos['Op2'], "SNsn"):
                count += 1
                error[count] = "Debe indicar si esta activo para Compras (S/N)."

            if not validar.validar_string(datos['Op3'], "SNsn"):
                count += 1
                error[count] = "Debe indicar si esta activo para Ventas (S/N)."

            print(datos, "Cantidad de elementos:      ", len(datos))
            print(error, "Cant. Errores de Validacón: ", len(error))

            if len(error) > 0:
                for txt, i in enumerate(error):
                    msg += "* " + error[i] + "\n"
                CTkMessagebox(title="Error", message=msg, icon="cancel")
            else:
                print("Se validaron todos los Datos.")
                saveRecord(datos)
            #     CTkMessagebox(title="Error", message=error[1], icon="cancel")

            pass


# ===================================================================
#  Método que maneja la creación de widget de las distintas ventanas
# ===================================================================
def invoice(opt=None, ventana_principal=None):
    # # Crear la ventana principal
    # root = ctk.CTk()
    # ventana_principal = InvoiceWindow(root)
    # # Crear y agregar widgets desde la clase secundaria
    # crear_widgets = InvoiceWidgets(ventana_principal)

    match opt:
        case "new":
            # Cerrar la ventana actual y abrir una nueva para el formulario
            ventana_principal.cerrar_ventana()
            root = ctk.CTk()
            ventana_principal = InvoiceWindow(root)
            # Crear y agregar widgets desde la clase secundaria
            crear_widgets = InvoiceWidgets(ventana_principal)
            crear_widgets.dataForm("new")

        case "edit":
            # Cerrar la ventana actual y abrir una nueva para el formulario
            ventana_principal.cerrar_ventana()
            root = ctk.CTk()
            ventana_principal = InvoiceWindow(root)
            # Crear y agregar widgets desde la clase secundaria
            crear_widgets = InvoiceWidgets(ventana_principal)
            crear_widgets.dataForm("edit")

        case _:
            # Crear la ventana principal
            root = ctk.CTk()
            ventana_principal = InvoiceWindow(root)
            # Crear y agregar widgets desde la clase secundaria
            crear_widgets = InvoiceWidgets(ventana_principal)
            crear_widgets.listForm()


if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    invoice()
    app.mainloop()
