import customtkinter as ctk
from tkinter import font

from CTkMessagebox import CTkMessagebox
from CTkTable import *

import config
from config import db
from gui.themes.myStyles import *

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None
tax_status_code = None
tax_status_desc = None


def fetch_records():
    query = "SELECT code, description FROM tax_status"
    value = ''
    result = db.fetchRecords(query, value)
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
    global tax_status_desc
    try:
        if selected_row is not None:
            objeto.deselect_row(selected_row)

        objeto.select_row(e["row"])
        selected_row = e["row"]
        tax_status_code = objeto.get(selected_row, 0)
        tax_status_desc = objeto.get(selected_row, 1)
        print(" CODE Selected: ", tax_status_code)
        # print(e)
    except:
        msgbox = CTkMessagebox(title="Error",
                               header=True,
                               message="Ha ocurrido un error desconocido.",
                               icon="warning",
                               sound=True,
                               wraplength=400,
                               option_1="Aceptar",
                               )
        response = msgbox.get()
        if response == "Aceptar":
            selected_row = None
            tax_status_code = ''


def selection_return(parent, widget):
    parent.asignar_valor('taxstatus', tax_status_code, tax_status_desc)
    widget.root.destroy()


# =================
#  Clase Principal
# =================
class TaxStatusShow:
    def __init__(self, parent):
        self.padre = parent
        self.root = ctk.CTkToplevel()
        self.root.title('Condiciones Fiscales')
        self.root.grab_set()
        self.root.config(padx=10, pady=10)
        # Evitar que la ventana se expanda
        self.root.resizable(False, False)
        # Evitar que la ventana se cierre
        # self.root.protocol("WM_DELETE_WINDOW", lambda: None)

        marco = ctk.CTkScrollableFrame(master=self.root,
                                       width=300,
                                       height=250,
                                       corner_radius=0,
                                       border_width=1,
                                       border_color="black",
                                       scrollbar_fg_color="black",
                                       )
        # marco.grid_rowconfigure(0, weight=1)
        # marco.grid_columnconfigure(0, weight=1)
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

        marco.grid()

        # Botones de Acciones
        marco_btns = ctk.CTkFrame(master=self.root,
                                  width=300,
                                  )
        cancel_btn = ctk.CTkButton(marco_btns, text="Cancelar", width=100,
                                   command=lambda: self.root.destroy(),
                                   **style_cancel)
        select_btn = ctk.CTkButton(marco_btns, text="Seleccionar", width=100,
                                   command=lambda: selection_return(self.padre, self)
                                   if selected_row is not None
                                   else CTkMessagebox(title="Error",
                                                      message="Debe seleccionar un tipo de contribuyente",
                                                      icon="cancel"),
                                   )

        marco_btns.grid(pady=15)
        cancel_btn.grid(row=1, column=1, padx=5, pady=5, )
        select_btn.grid(row=1, column=2, padx=5, pady=5, )


if __name__ == '__main__':
    from config.SQLite_DB import Database

    # data = '../config/iva_data.db'
    db = Database(config.DB_SYS)

    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    TaxStatusShow('')
    app.mainloop()
