import customtkinter as ctk
from tkinter import font

from CTkMessagebox import CTkMessagebox
from CTkTable import *

# import config
from config import db, DB_SYS


# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None
provinces_code = None
provinces_desc = None


def fetch_records():
    query = "SELECT code, description FROM sys_provinces"
    value = ''
    result = db.fetchRecords(query, value)
    print("fetchall: ", result)
    return result


def get_record(record):
    query = f"SELECT * FROM sys_provinces WHERE code = ?"
    value = (record,)
    result = db.fetchRecord(query, value)
    print("fetchone: ", result)
    return result


def select_provinces(objeto, e):
    # 'e' tiene los datos pasados por el widget tabla de donde se hizo el Click
    global selected_row
    global provinces_code
    global provinces_desc
    try:
        if selected_row is not None:
            objeto.deselect_row(selected_row)

        objeto.select_row(e["row"])
        selected_row = e["row"]
        provinces_code = objeto.get(selected_row, 0)
        provinces_desc = objeto.get(selected_row, 1)
        print(" CODE Selected: ", provinces_code)
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
            provinces_code = ''


def selection_return(parent, widget):
    parent.asignar_valor('provinces', provinces_code, provinces_desc)
    widget.root.destroy()


# =================
#  Clase Principal
# =================
class ProvincesShowAFIP:
    def __init__(self, parent, opt=None):
        self.padre = parent
        self.opt = opt
        self.root = ctk.CTkToplevel()
        self.root.title('Provincias')
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
        # Leer comprobantes desde la base de datos (DB)
        value = fetch_records()
        # Crear tabla con los comprobantes existentes en la DB
        table = CTkTable(master=marco,
                         row=len(value),
                         column=2,
                         values=value,
                         border_width=0,
                         corner_radius=0,
                         command=lambda e: select_provinces(table, e),
                         )

        table.edit_column(0, width=50)
        table.edit_column(1, width=250, anchor="w")
        table.grid(row=0, column=0, )

        marco.grid()
        print(self.opt)
        # Botones de Acciones
        marco_btns = ctk.CTkFrame(master=self.root,
                                  width=300,
                                  )
        close_btn = ctk.CTkButton(marco_btns, text="Cerrar", width=100,
                                  command=lambda: self.root.destroy())
        select_btn = ctk.CTkButton(marco_btns, text="Seleccionar", width=100,
                                   command=lambda: selection_return(self.padre, self)
                                   if selected_row is not None
                                   else CTkMessagebox(title="Error",
                                                      message="Debe seleccionar una Provincia",
                                                      icon="cancel"),
                                   )
        marco_btns.grid(pady=15)
        if self.opt == 'select':
            select_btn.grid(row=1, column=1, padx=5, pady=5, )
        close_btn.grid(row=1, column=2, padx=5, pady=5, )


if __name__ == '__main__':
    from config.SQLite_DB import Database
    from config import DB_SYS

    # data = '../config/iva_data.db'
    data = DB_SYS
    db = Database(data)

    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    ProvincesShowAFIP('', 'select')
    app.mainloop()
