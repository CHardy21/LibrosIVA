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


def load_data(self, start, limit):
    query = "SELECT code,description FROM sys_activities_eco_f833 LIMIT ? OFFSET ?"
    value = (limit, start)
    result = db.fetchRecords2(query, value)
    for fila in result:
        self.table.insert("", "end", values=fila)


def fetch_records():
    query = "SELECT code,description FROM sys_activities_eco_f833 LIMIT 50"
    result = db.fetchRecords(query)
    print(result)
    return result


def get_record(record):
    query = f"SELECT * FROM activities_eco_f833 WHERE code = '{record}'"
    result = db.fetchRecord(query)
    print("valor devuelto: ", result)
    return result


def search_records(searchedData):
    pass


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


class ActivitiesShows:
    def __init__(self, parent):
        self.padre = parent
        self.root = ctk.CTkToplevel()
        self.root.title('Actividades Económicas')
        self.root.grab_set()
        self.root.config(padx=10, pady=10)
        self.root.resizable(False, False)  # Evitar que la ventana se expanda
        # self.root.protocol("WM_DELETE_WINDOW", lambda: None)  # Evitar que la ventana se cierre
        print('Parent: ', parent)

        marco_search = ctk.CTkFrame(self.root,
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
        # Agregar widget
        search_entry.grid(row=0, column=0, pady=10, padx=10, sticky='e')
        search_btn.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        marco_search.grid()

        self.marco = ctk.CTkScrollableFrame(self.root,
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
        self.table = CTkTable(master=self.marco,
                              # row=len(value),
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
        self.marco.grid()

        self.load_data(0, 20)

        # Botones de Acciones
        marco_btns = ctk.CTkFrame(self.root,
                                  width=300,
                                  )
        cancel_btn = ctk.CTkButton(marco_btns, text="Cancelar", width=100,
                                   command=lambda: self.root.destroy())
        select_btn = ctk.CTkButton(marco_btns, text="Seleccionar", width=100,
                                   command=lambda: selection_return(self.padre, self)
                                   if selected_row is not None
                                   else CTkMessagebox(title="Error",
                                                      message="Debe seleccionar un Comprobante para editar",
                                                      icon="cancel"),
                                   )
        marco_btns.grid()
        cancel_btn.grid(row=1, column=1, padx=5, pady=5, )
        select_btn.grid(row=1, column=2, padx=5, pady=5, )

        self.marco._parent_canvas.bind("<Configure>", self.on_scroll)

    def load_data(self, start, limit):
        query = "SELECT code,description FROM sys_activities_eco_f833 LIMIT ? OFFSET ?"
        value = (limit, start)
        result = db.fetchRecords2(query, value)
        for fila in result:
            self.table.add_row(values=fila)

    def on_scroll(self, event):
        print("Event on_scroll run ")
        # Detectar si se ha llegado al final del scroll
        if self.marco._parent_canvas.yview()[1] == 1.0:
            # Cargar más datos
            current_count = len(self.table.get())
            self.load_data(current_count, 20)


if __name__ == '__main__':
    from config.SQLite_DB import Database

    data = '../config/iva_data.db'
    db = Database(data)

    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    ActivitiesShows('')
    app.mainloop()
