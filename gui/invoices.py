import customtkinter as ctk
from tkinter import StringVar, font
from CTkTable import *

from config import db

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None


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
    def borrar_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

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
                                command=lambda: invoice("new",self.ventana_principal),)
        edit_btn = ctk.CTkButton(marco_btns, text="Editar", width=100,)
        delete_btn = ctk.CTkButton(marco_btns, text="Eliminar", width=100, )

        marco_btns.pack(pady=15)

        cancel_btn.grid(row=1, column=0, padx=5, pady=5, )
        edit_btn.grid(row=1, column=1, padx=5, pady=5, )
        new_btn.grid(row=1, column=2, padx=5, pady=5, )

        self.ventana_principal.agregar_widget(marco_btns)

# Clase para el formulario de nuevo comprobante
class NewInvoiceForm:
    def __init__(self, root):
        self.root = ctk.CTkToplevel()
        self.root.title('Nuevo Comprobante')
        self.root.grab_set()
        self.root.config(padx=10, pady=10)

        self.create_form()

    def create_form(self):
        # Aquí puedes agregar los widgets para el formulario
        label_code = ctk.CTkLabel(self.root, text="Código:")
        label_code.pack(pady=5)
        entry_code = ctk.CTkEntry(self.root)
        entry_code.pack(pady=5)

        label_description = ctk.CTkLabel(self.root, text="Descripción:")
        label_description.pack(pady=5)
        entry_description = ctk.CTkEntry(self.root)
        entry_description.pack(pady=5)

        save_btn = ctk.CTkButton(self.root, text="Guardar", command=self.save_invoice)
        save_btn.pack(pady=10)

    def save_invoice(self):
        # Aquí puedes agregar la lógica para guardar el nuevo comprobante
        print("Guardar nuevo comprobante")


# Método que maneja la creación de widget de las distintas ventanas
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
            # crear_widgets.newForm()
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
