# import customtkinter as ctk
# from CTkTable import *
# import sqlite3
#
# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#
#         self.title("Ejemplo de Carga Perezosa")
#         self.geometry("600x400")
#
#         # Crear el CTkScrollableFrame
#         self.scrollable_frame = ctk.CTkScrollableFrame(self, width=580, height=380)
#         self.scrollable_frame.pack(pady=10)
#
#         # Crear la tabla dentro del CTkScrollableFrame
#         self.table = CTkTable(self.scrollable_frame, columns=("ID", "Nombre", "Email"))
#         self.table.pack()
#
#         # Conectar a la base de datos
#         self.conexion = sqlite3.connect('ejemplo.db')
#         self.cursor = self.conexion.cursor()
#
#         # Cargar los primeros datos
#         self.load_data(0, 20)
#
#         # Vincular el evento de desplazamiento
#         self.scrollable_frame.bind("<Configure>", self.on_scroll)
#
#     def load_data(self, start, limit):
#         self.cursor.execute("SELECT * FROM usuarios LIMIT ? OFFSET ?", (limit, start))
#         resultados = self.cursor.fetchall()
#         for fila in resultados:
#             self.table.insert("", "end", values=fila)
#
#     def on_scroll(self, event):
#         # Detectar si se ha llegado al final del scroll
#         if self.scrollable_frame.yview()[1] == 1.0:
#             # Cargar más datos
#             current_count = len(self.table.get_children())
#             self.load_data(current_count, 20)
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

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
    query = "SELECT code,description FROM activities_eco_f833 LIMIT ? OFFSET ?"
    value = (limit, start)
    result = db.fetchRecords2(query, value)
    for fila in result:
        self.table.insert("", "end", values=fila)


def fetch_records():
    query = "SELECT code,description FROM activities_eco_f833 LIMIT 15"
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
        self.marco_scroll.grid()

        value = fetch_records()

        self.table = CTkTable(master=self.marco_scroll,
                              # row=20,
                              column=2,
                              values=value,
                              border_width=0,
                              corner_radius=0,
                              command=lambda e: select_activity(self.table, e),
                              )

        self.table.edit_column(0, width=100)
        self.table.edit_column(1, width=250, anchor="w")
        self.table.grid(row=0, column=0, )

        # self.load_data(0, 20)

        # Crear un scrollbar y asociarlo al marco desplazable
        self.scrollbar = ctk.CTkScrollbar(self.root, command=self.marco_scroll._parent_canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.marco_scroll._parent_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Comprobar la posición del scrollbar
        # self.root.after(100, self.check_scroll_position)
        self.marco_scroll.bind("<Configure>", self.on_scroll)
    def check_scroll_position(self):
        if self.marco_scroll._parent_canvas.yview()[1] == 1.0:
            print("El scrollbar está en la parte inferior.")
        else:
            print("El scrollbar no está en la parte inferior.")
        self.root.after(100, self.check_scroll_position)


    def load_data(self, start, limit):
        query = "SELECT code,description FROM activities_eco_f833 LIMIT ? OFFSET ?"
        value = (limit, start)
        result = db.fetchRecords2(query, value)
        print(len(result))
        count = 0
        for fila in result:
            # print(fila)
            print(f'Fila: {count}', fila[0], fila[1])
            self.table.add_row(values=(fila[0], fila[1]))
            count += 1

    def on_scroll(self, event):
        # Detectar si se ha llegado al final del scroll
        if self.marco_scroll._parent_canvas.yview()[1] == 1.0:
            self.marco_scroll._parent_canvas.yview_moveto(0.5)
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
