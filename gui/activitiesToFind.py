import customtkinter as ctk
from tkinter import StringVar, font
from CTkMessagebox import CTkMessagebox
from CTkTable import *

import config
from config import db
from gui.themes.myStyles import *

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None
activity_code = None
activity_description = None


# def get_record(record):
#     query = f"SELECT * FROM activities_eco_f833 WHERE code = '?'"
#     value = (record,)
#     result = db.fetchRecord(query, value)
#     print("valor devuelto: ", result)
#     return result


# def search_records(searchedData):
#     query = f"SELECT * FROM activities_eco_f833 WHERE description_large LIKE ?"
#     value = ('%' + searchedData + '%',)
#     result = db.fetchRecords2(query, value)
#     print("valor devuelto: ", result)
#     return result


def select_activity(objeto, self, e):
    # 'e' tiene los datos pasados por el widget tabla de donde se hizo el  Click
    global selected_row
    global activity_code
    global activity_description

    if selected_row is not None:
        objeto.deselect_row(selected_row)
        self.textBox_info.delete("0.0", "end")  # delete all text

    objeto.select_row(e["row"])
    self.marco_info.grid(row=2)

    selected_row = e["row"]
    activity_code = objeto.get(selected_row, 0)
    activity_description = objeto.get(selected_row, 2)

    print(" CODE Activity Selected: ", activity_code)
    print(e)

    self.textBox_info.insert("0.0", f"Cód: {activity_code} \n")  # insert at line 0 character 0
    self.textBox_info.insert("2.0", f"Des: {activity_description}")
    # Configurar la etiqueta para cambiar el color del texto
    self.textBox_info.tag_config("white", foreground="white")
    # Aplicar la etiqueta a una parte específica del texto
    self.textBox_info.tag_add("white", "1.0", "1.4")
    self.textBox_info.tag_add("white", "2.0", "2.4")


def selection_return(parent, widget):
    parent.asignar_valor('activities', activity_code, activity_description)
    widget.root.destroy()


class ActivitiesToFind:
    def __init__(self, parent):
        self.padre = parent
        self.table = None
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
        self.search_result_label = ctk.CTkLabel(marco_search, text="", )
        search_entry.grid(row=0, column=0, pady=10, padx=10, sticky='e')
        search_btn.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        self.search_result_label.grid(row=1, column=0, padx=10, pady=10, sticky='we')

        marco_search.grid(row=0)

        self.marco_scroll = ctk.CTkScrollableFrame(self.root,
                                                   width=500,
                                                   height=250,
                                                   corner_radius=0,
                                                   border_width=1,
                                                   border_color="black",
                                                   scrollbar_fg_color="black",
                                                   )

        self.marco_info = ctk.CTkFrame(self.root, width=498,
                                       height=50,
                                       corner_radius=0, )
        self.textBox_info = ctk.CTkTextbox(self.marco_info,
                                           width=498, height=70,
                                           text_color='grey')
        self.textBox_info.grid(padx=10, pady=10)

    def search_value(self):

        if self.marco_info is not None:
            self.marco_info.grid_remove()

        search_term = self.searchValue.get()
        query = "SELECT code, description, description_large FROM sys_activities_eco_f833 WHERE description LIKE ?"
        value = ('%' + search_term + '%',)
        result = db.fetchRecords2(query, value)
        print(result)
        numRows = len(result)
        print('Registros devueltos: ', numRows)
        self.search_result_label.configure(text=f'Se encontraron {numRows} coincidencias.',
                                           text_color="lime green",
                                           anchor='w', )

        self.create_table(result)
        self.marco_scroll.grid(row=1)

    def create_table(self, data):
        print('En Creacion Tabla: ', data)
        if self.table is not None:
            self.table.destroy()
        else:
            create_btns(self)
        self.table = CTkTable(master=self.marco_scroll,
                              column=3,
                              values=data,
                              border_width=0,
                              corner_radius=0,
                              command=lambda e: select_activity(self.table, self, e),
                              )
        self.table.edit_column(0, width=100)
        self.table.edit_column(1, width=350, anchor="w")
        self.table.edit_column(2, width=0, )
        self.table.grid(row=0, column=0, )


def create_btns(self):
    # Botones de Acciones
    self.marco_btns = ctk.CTkFrame(self.root,
                                   width=300,
                                   height=150
                                   )
    self.marco_btns.grid(row=3)

    cancel_btn = ctk.CTkButton(self.marco_btns, text="Cancelar", width=100,
                               command=lambda: self.root.destroy(),
                               **style_cancel,
                               )
    select_btn = ctk.CTkButton(self.marco_btns, text="Seleccionar", width=100,
                               command=lambda: selection_return(self.padre, self)
                               if selected_row is not None
                               else CTkMessagebox(title="Error",
                                                  message="Debe seleccionar una Actividad",
                                                  icon="cancel"),
                               **style_select,
                               )

    cancel_btn.grid(row=1, column=1, padx=5, pady=5, )
    select_btn.grid(row=1, column=2, padx=5, pady=5, )


if __name__ == '__main__':
    from config.SQLite_DB import Database

    data = config.DB_SYS
    db = Database(data)

    # ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    ActivitiesToFind('')
    app.mainloop()
