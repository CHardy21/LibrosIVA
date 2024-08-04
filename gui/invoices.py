import customtkinter as ctk
from tkinter import StringVar, font

from CTkMessagebox import CTkMessagebox
from CTkTable import *

from config import db
import gui.invoices_functions as validar

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None


def saveRecord(self):
    # Código para recuperar los datos y meterlos en un diccionario para luego pasarlo
    # a la funcion que los guarda en la base de datos
    print(self)
    # Recuperando Datos Del Formulario
    datos = {
        "invoiceCode": self.invoiceCode.get(),
        # "invoiceDescription": self.invoiceDescription_entry.get(),
        # "invoiceObs": self.invoice_obs.get()
        # invoiceTypeRet = StringVar()
        # invoiceTypeCert = StringVar()
        # invoiceTypeDC = StringVar()
        # invoiceOp1 = StringVar()
        # invoiceOp2 = StringVar()
        # invoiceOp3 = StringVar()
        # invoiceOp4 = StringVar()
        # invoiceCodeA = StringVar()
        # invoiceCodeB = StringVar()
        # invoiceCodeC = StringVar()
        # invoiceCodeE = StringVar()
        # invoiceCodeM = StringVar()
        # invoiceCodeT = StringVar()
        # invoiceCodeO = StringVar()
    }
    print(datos)
    # data.insertRecord(item_name=item_name.get(), item_price=item_amt.get(), purchase_date=transaction_date.get())


def fetch_records():
    query = "SELECT CODE,DESCRIPTION FROM invoices"
    result = db.fetchRecord(query)
    print(result)
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

        # Agregar el widget creado en la Clase Principal
        self.ventana_principal.agregar_widget(marco)
        self.buttonsForm()

    def buttonsForm(self):

        # Botones de Acciones
        marco_btns = ctk.CTkFrame(master=self.ventana_principal.root,
                                  width=300,
                                  )

        cancel_btn = ctk.CTkButton(marco_btns, text="Cancelar", width=100,
                                   command=lambda: self.ventana_principal.cerrar_ventana())
        select_btn = ctk.CTkButton(marco_btns, text="Seleccionar", width=100, )
        new_btn = ctk.CTkButton(marco_btns, text="Nuevo", width=100,
                                command=lambda: invoice("new", self.ventana_principal), )
        edit_btn = ctk.CTkButton(marco_btns, text="Editar", width=100, )
        delete_btn = ctk.CTkButton(marco_btns, text="Eliminar", width=100, )

        marco_btns.pack(pady=15)

        cancel_btn.grid(row=1, column=0, padx=5, pady=5, )
        edit_btn.grid(row=1, column=1, padx=5, pady=5, )
        new_btn.grid(row=1, column=2, padx=5, pady=5, )

        self.ventana_principal.agregar_widget(marco_btns)

    def dataForm(self, opt=None):

        titulo_ventana = "Nuevo Comprobante"
        self.ventana_principal.cambiar_titulo(titulo_ventana)

        if opt == "new":
            # Variables del Formulario
            invoiceCode = StringVar()
            invoiceDescription = StringVar()
            invoiceObs = StringVar()
            invoiceTypeRet = StringVar()
            invoiceTypeCert = StringVar()
            invoiceTypeDC = StringVar()
            invoiceOp1 = StringVar()
            invoiceOp2 = StringVar()
            invoiceOp3 = StringVar()
            invoiceOp4 = StringVar()
            invoiceCodeA = StringVar()
            invoiceCodeB = StringVar()
            invoiceCodeC = StringVar()
            invoiceCodeE = StringVar()
            invoiceCodeM = StringVar()
            invoiceCodeT = StringVar()
            invoiceCodeO = StringVar()
        elif opt == "edit":
            # Recupera Valores del Formulario desde la Base de Datos
            pass
        else:
            print("ERROR: opcion no valida")

        # Crea el frame y añádelo a la ventana
        marco = ctk.CTkFrame(master=self.ventana_principal.root,
                             width=420,
                             height=380,
                             corner_radius=0,
                             border_width=1,
                             border_color="black",
                             )
        # marco.pack(padx=5, pady=5)

        invoiceCode_label = ctk.CTkLabel(marco, text="Código", ).place(x=10, y=10)
        invoiceCode_entry = ctk.CTkEntry(marco, textvariable=invoiceCode, width=40,
                                         validate="focusout", ).place(x=110, y=10)
        invoiceDescription_label = ctk.CTkLabel(marco, text="Descripción", ).place(x=10, y=40)
        invoiceDescription_entry = ctk.CTkEntry(marco, textvariable=invoiceDescription, width=180).place(x=110, y=40)
        invoiceObs_label = ctk.CTkLabel(marco, text="Observaciones:", ).place(x=10, y=70)
        invoiceObs_entry = ctk.CTkEntry(marco, textvariable=invoiceObs, width=300).place(x=110, y=70)

        invoiceTypeRet_checkbox = ctk.CTkCheckBox(marco, text="Retencion", variable=invoiceTypeRet,
                                                  onvalue="on",
                                                  offvalue="off").place(x=10, y=115)
        invoiceTypeCert_checkbox = ctk.CTkCheckBox(marco, text="Certificado", variable=invoiceTypeCert,
                                                  onvalue="on",
                                                  offvalue="off").place(x=110, y=115)

        invoiceTypeDC_label = ctk.CTkLabel(marco, text="Débito o Crédito (D/C)", )
        invoiceTypeDC_label.place(x=(170 - len(invoiceTypeDC_label.cget("text")) * 6), y=145)
        invoiceTypeDC_entry = ctk.CTkEntry(marco, textvariable=invoiceTypeDC, width=25).place(x=180, y=145)
        invoiceOp1_label = ctk.CTkLabel(marco, text="  Tiene Numeración (S/N) ", )
        invoiceOp1_label.place(x=(170 - len(invoiceOp1_label.cget("text")) * 6), y=175)
        invoiceOp1_entry = ctk.CTkEntry(marco, textvariable=invoiceOp1, width=25).place(x=180, y=175)
        invoiceOp2_label = ctk.CTkLabel(marco, text=" Activo en Compras (S/N) ", )
        invoiceOp2_label.place(x=(170 - len(invoiceOp2_label.cget("text")) * 6), y=205)
        invoiceOp2_entry = ctk.CTkEntry(marco, textvariable=invoiceOp2, width=25).place(x=180, y=205)
        invoiceOp3_label = ctk.CTkLabel(marco, text=" Activo en Ventas (S/N)", )
        invoiceOp3_label.place(x=(170-len(invoiceOp3_label.cget("text"))*6), y=235)
        print(180-len(invoiceOp3_label.cget("text")))
        invoiceOp3_entry = ctk.CTkEntry(marco, textvariable=invoiceOp3, width=25).place(x=180, y=235)
        invoiceOp4_checkbox = ctk.CTkCheckBox(marco, text="Emitido por Controlador Fiscal", variable=invoiceOp4,
                                                   onvalue="on",
                                                   offvalue="off").place(x=10, y=265)

        invoiceCodes_label = ctk.CTkLabel(marco, text="Cód. s/ RG 3685 (AFIP):", font=font_widgets,).place(x=255, y=115)
        invoiceCodeA_label = ctk.CTkLabel(marco, text="Comprobante Tipo A", ).place(x=240, y=145)
        invoiceCodeA_entry = ctk.CTkEntry(marco, textvariable=invoiceCodeA, width=40).place(x=370, y=145)
        invoiceCodeB_label = ctk.CTkLabel(marco, text="Comprobante Tipo B", ).place(x=240, y=175)
        invoiceCodeB_entry = ctk.CTkEntry(marco, textvariable=invoiceCodeA, width=40).place(x=370, y=175)
        invoiceCodeC_label = ctk.CTkLabel(marco, text="Comprobante Tipo C", ).place(x=240, y=205)
        invoiceCodeC_entry = ctk.CTkEntry(marco, textvariable=invoiceCodeA, width=40).place(x=370, y=205)
        invoiceCodeE_label = ctk.CTkLabel(marco, text="Comprobante Tipo E", ).place(x=240, y=235)
        invoiceCodeE_entry = ctk.CTkEntry(marco, textvariable=invoiceCodeA, width=40).place(x=370, y=235)
        invoiceCodeM_label = ctk.CTkLabel(marco, text="Comprobante Tipo M", ).place(x=240, y=265)
        invoiceCodeM_entry = ctk.CTkEntry(marco, textvariable=invoiceCodeA, width=40).place(x=370, y=265)
        invoiceCodeT_label = ctk.CTkLabel(marco, text="Comprobante Tipo T", ).place(x=240, y=295)
        invoiceCodeT_entry = ctk.CTkEntry(marco, textvariable=invoiceCodeA, width=40).place(x=370, y=295)


        #  command=lambda: selectInvoice()
        clear_btn = ctk.CTkButton(marco, text="Borrar", width=80, )
        cancel_btn = ctk.CTkButton(marco, text="Cancelar", width=80,
                                   command=lambda: self.ventana_principal.cerrar_ventana())
        ok_btn = ctk.CTkButton(marco, text="Guardar", width=120,
                               command=lambda: validation_form(self)
                               )

        clear_btn.place(x=12, y=340)
        cancel_btn.place(x=205, y=340)
        ok_btn.place(x=290, y=340)

        self.ventana_principal.agregar_widget(marco)

        def validation_form(self):
            datos = dict()
            error = {}
            count = 0

            if validar.validate_txt(invoiceCode.get(), 1, 4, str):
                datos["Code"] = invoiceCode.get()
            else:
                count += 1
                error[count] = "Código de Comprobante debe contener 1-4 caracteres."

            if validar.validate_txt(invoiceDescription.get(), 1, 24, str):
                datos["Description"] = invoiceCode.get()
            else:
                count += 1
                error[count] = "Descripción de Comprobante debe contener 1-24 caracteres."

            if validar.validar_string(invoiceTypeDC.get(),"DCdc"):
                datos["invoiceTypeDC"] = invoiceTypeDC.get()
            else:
                count += 1
                error[count] = "Debe indicar Débito o Crédito (D/C)."

            print(datos, "Cantidad de elementos: ", len(datos))
            print(error, "Cantidad de elementos: ", len(error))
            msg = ""
            if len(error)>0:
                for txt,i in enumerate(error):
                    msg += "* " + error[i]+"\n"
                    print(i)
                CTkMessagebox(title="Error", message=msg, icon="cancel")
            # else:
            #     CTkMessagebox(title="Error", message=error[1], icon="cancel")
            # Recuperando Datos Del Formulario
            # datos = {
            #     "invoiceCode": invoiceCode_entry.get(),
            # "invoiceDescription": self.invoiceDescription_entry.get(),
            # "invoiceObs": self.invoice_obs.get()
            # invoiceTypeRet = StringVar()
            # invoiceTypeCert = StringVar()
            # invoiceTypeDC = StringVar()
            # invoiceOp1 = StringVar()
            # invoiceOp2 = StringVar()
            # invoiceOp3 = StringVar()
            # invoiceOp4 = StringVar()
            # invoiceCodeA = StringVar()
            # invoiceCodeB = StringVar()
            # invoiceCodeC = StringVar()
            # invoiceCodeE = StringVar()
            # invoiceCodeM = StringVar()
            # invoiceCodeT = StringVar()
            # invoiceCodeO = StringVar()
            # }
            # print(datos)

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
            # NewInvoiceForm(ctk.CTk())

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
