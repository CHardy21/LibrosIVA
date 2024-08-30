import customtkinter as ctk
from tkinter import StringVar, font

from CTkMessagebox import CTkMessagebox
from CTkTable import *

from config import db

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None
activity_code = None
activity_description = None


def fetch_records():
    query = "SELECT code,description FROM activities_eco_f833 LIMIT 50"
    result = db.fetchRecords(query)
    print(result)
    return result


def get_record(record):
    query = f"SELECT * FROM activities_eco_f833 WHERE code = '{record}'"
    result = db.fetchRecord(query)
    print("valor devuelto: ", result)
    return result


def search_records(searchedData):
    query = f"SELECT * FROM activities_eco_f833 WHERE description_large LIKE ?"
    value = ('%' + searchedData + '%',)
    result = db.fetchRecords2(query, value)
    print("valor devuelto: ", result)
    return result


def select_activity(objeto, e):
    # 'e' tiene los datos pasados por el widget tabla de donde se hizo el  Click
    global selected_row
    global activity_code
    global activity_description

    if selected_row is not None:
        objeto.deselect_row(selected_row)

    objeto.select_row(e["row"])
    selected_row = e["row"]
    activity_code = objeto.get(selected_row, 0)
    activity_description = objeto.get(selected_row, 1)
    print(" CODE Activity Selected: ", activity_code)
    print(e)


def selection_return(parent, widget):
    parent.asignar_valor('activities', activity_code, activity_description)
    widget.root.destroy()


class ActivitiesToFind:
    def __init__(self, parent):
        self.padre = parent
        self.root = ctk.CTkToplevel()
        self.root.title('Actividades Económicas')
        self.root.grab_set()
        self.root.config(padx=10, pady=10)
        self.root.resizable(False, False)  # Evitar que la ventana se expanda
        # self.root.protocol("WM_DELETE_WINDOW", lambda: None)  # Evitar que la ventana se cierre
        print('Parent: ', parent)
        self.searchValue = StringVar()

        marco_search = ctk.CTkFrame(self.root,
                                    width=518,
                                    height=50,
                                    corner_radius=0,
                                    )
        search_entry = ctk.CTkEntry(master=marco_search,
                                    width=360,
                                    textvariable=self.searchValue,
                                    )
        search_btn = ctk.CTkButton(master=marco_search,
                                   width=120,
                                   text='Buscar',
                                   command=lambda: self.search_value())
        # Agregar widget
        search_entry.grid(row=0, column=0, pady=10, padx=10, sticky='e')
        search_btn.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        marco_search.grid()

        self.marco_scroll = ctk.CTkScrollableFrame(self.root,
                                            width=500,
                                            height=250,
                                            corner_radius=0,
                                            border_width=1,
                                            border_color="black",
                                            scrollbar_fg_color="black",
                                            )

        # Leer comprobantes desde la base de datos (DB)
        # value = fetch_records()
        # Crear tabla con los comprobantes existentes en la DB
        self.table = CTkTable(master=self.marco_scroll,
                              row=10,
                              column=2,
                              # values=value,
                              border_width=0,
                              corner_radius=0,
                              command=lambda e: select_activity(self.table, e),
                              )
        self.table.edit_column(0, width=100)
        self.table.edit_column(1, width=250, anchor="w")
        self.table.grid(row=0, column=0, )
        # Agregar widget creado en la Clase Principal
        # self.marco_scroll.grid()

    def search_value(self):
        search_term = self.searchValue.get()
        query = "SELECT code, description FROM sys_activities_eco_f833 WHERE description LIKE ?"
        value = ('%' + search_term + '%',)
        result = db.fetchRecords2(query, value)
        print(result)
        print('Registros devueltos: ', len(result))
        # self.table.configure(row=len(result))
        # self.table.update_values(result)
        # self.marco_scroll.grid()
        # self.update_table(result)

    def update_table(self, data):

        # Limpiar la tabla antes de agregar nuevos datos
        for item in self.table.get():
            self.table.delete_row(item)
        # Agregar nuevos datos a la tabla
        for fila in data:
            self.table.add_row(values=(fila[0], fila[1]))


if __name__ == '__main__':
    from config.SQLite_DB import Database

    data = '../config/iva_data.db'
    db = Database(data)

    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    ActivitiesToFind('')
    app.mainloop()
