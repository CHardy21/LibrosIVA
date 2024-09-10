import customtkinter as ctk
from tkinter import StringVar, font
from CTkMessagebox import CTkMessagebox
from CTkTable import *

from config import db

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None
code = None
description = None


def load_data(self, start, limit):
    query = "SELECT code,description FROM sys_invoices_types LIMIT ? OFFSET ?"
    value = (limit, start)
    result = db.fetchRecords2(query, value)
    for fila in result:
        self.table.insert("", "end", values=fila)


def fetch_records():
    query = "SELECT code,description FROM sys_invoices_types"
    value = ''
    result = db.fetchRecords(query, value)
    # print(result)
    return result


# def get_record(record):
#     query = f"SELECT * FROM activities_eco_f833 WHERE code = '{record}'"
#     result = db.fetchRecord(query)
#     print("valor devuelto: ", result)
#     return result


def select_invoice(objeto, e):
    # 'e' tiene los datos pasados por el widget tabla de donde se hizo el Click
    global selected_row
    global code
    global description

    if selected_row is not None:
        objeto.table.deselect_row(selected_row)
        objeto.textBox_info.delete("0.0", "end")  # delete all text

    objeto.table.select_row(e["row"])
    selected_row = e["row"]
    code = objeto.table.get(selected_row, 0)
    description = objeto.table.get(selected_row, 1)
    # print(" CODE Selected: ", code)
    # print(e)

    objeto.textBox_info.insert("0.0", f"Cód: {code} \n")  # insert at line 0 character 0
    objeto.textBox_info.insert("2.0", f"Des: {description}")
    # Configurar la etiqueta para cambiar el color del texto
    objeto.textBox_info.tag_config("white", foreground="white")
    # Aplicar la etiqueta a una parte específica del texto
    objeto.textBox_info.tag_add("white", "1.0", "1.4")
    objeto.textBox_info.tag_add("white", "2.0", "2.4")



def selection_return(parent, widget):
    parent.asignar_valor('invoicesAFIP', code, description)
    widget.root.destroy()


class InvoicesShowAFIP:
    def __init__(self, parent):
        self.padre = parent
        self.root = ctk.CTkToplevel()
        self.root.title('Tipos de Comprobantes (AFIP)')
        self.root.grab_set()
        self.root.config(padx=10, pady=10)
        self.root.resizable(False, False)  # Evitar que la ventana se expanda
        # self.root.protocol("WM_DELETE_WINDOW", lambda: None)  # Evitar que la ventana se cierre

        self.marco = ctk.CTkScrollableFrame(self.root,
                                            width=500,
                                            height=250,
                                            corner_radius=0,
                                            border_width=1,
                                            border_color="black",
                                            scrollbar_fg_color="black",
                                            )

        # Leer comprobantes desde la base de datos (DB)
        value = fetch_records()
        # Crear tabla con los comprobantes existentes en la DB
        self.table = CTkTable(master=self.marco,
                              row=len(value),
                              column=2,
                              values=value,
                              border_width=0,
                              corner_radius=0,
                              command=lambda e: select_invoice(self, e),
                              )
        self.table.edit_column(0, width=80)
        self.table.edit_column(1, width=270, anchor="w")
        self.table.grid(row=0, column=0, )

        self.marco.grid()

        self.marco_info = ctk.CTkFrame(self.root, width=498,
                                       height=50,
                                       corner_radius=0, )
        self.textBox_info = ctk.CTkTextbox(self.marco_info,
                                           width=498, height=70,
                                           text_color='grey')

        self.textBox_info.grid(padx=10, pady=10)
        self.marco_info.grid()

        # Botones de Acciones
        marco_btns = ctk.CTkFrame(self.root, width=300,)
        close_btn = ctk.CTkButton(marco_btns, text="Cerrar", width=100,
                                  command=lambda: self.root.destroy())
        select_btn = ctk.CTkButton(marco_btns, text="Seleccionar", width=100,
                                   command=lambda: selection_return(self.padre, self)
                                   if selected_row is not None
                                   else CTkMessagebox(title="Error",
                                                      message="Debe seleccionar un Comprobante para editar",
                                                      icon="cancel"),
                                   )
        marco_btns.grid()
        select_btn.grid(row=1, column=1, padx=5, pady=5, )
        close_btn.grid(row=1, column=2, padx=5, pady=5, )

        # self.marco._parent_canvas.bind("<Configure>", self.on_scroll)

    # def load_data(self, start, limit):
    #     query = "SELECT code,description FROM sys_activities_eco_f833 LIMIT ? OFFSET ?"
    #     value = (limit, start)
    #     result = db.fetchRecords2(query, value)
    #     for fila in result:
    #         self.table.add_row(values=fila)

    # def on_scroll(self, event):
    #     print("Event on_scroll run ")
    #     # Detectar si se ha llegado al final del scroll
    #     if self.marco._parent_canvas.yview()[1] == 1.0:
    #         # Cargar más datos
    #         current_count = len(self.table.get())
    #         self.load_data(current_count, 20)


if __name__ == '__main__':
    from config.SQLite_DB import Database

    data = '../config/iva_data.db'
    db = Database(data)

    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    InvoicesShowAFIP('')
    app.mainloop()
