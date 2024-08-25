import customtkinter as ctk
from tkinter import StringVar, font

from CTkMessagebox import CTkMessagebox
from CTkTable import *

from config import db
import config.functions_grals as fn

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None
activity_code = None


def fetch_records():
    query = ("SELECT code,description FROM activities_eco_f833 LIMIT 50")
    result = db.fetchRecords(query)
    print(result)
    return result


def get_record(record):
    query = f"SELECT * FROM activities_eco_f833 WHERE code = '{record}'"
    result = db.fetchRecord(query)
    print("valor devuelto: ", result)
    return result


def select_activity(objeto, e):
    # 'e' tiene los datos pasados por el widget tabla de donde se hizo el  Click
    global selected_row
    global activity_code

    if selected_row is not None:
        objeto.deselect_row(selected_row)

    objeto.select_row(e["row"])
    selected_row = e["row"]
    activity_code = objeto.get(selected_row, 0)
    print(" CODE Activity Selected: ", activity_code)
    print(e)


def selection_return(self, widget):
    self.ventana_principal.asignar_valor(self.valor_seleccionado)
    widget.cerrar_ventana()
    print('activity_code ', activity_code)
    return activity_code


# =================
#  Clase Principal
# =================
class ActivitiesWindow:
    def __init__(self, root):
        self.root = ctk.CTkToplevel()
        self.root.title('Actividades Económicas')
        self.root.grab_set()
        self.root.config(padx=10, pady=10)
        # Evitar que la ventana se expanda
        self.root.resizable(False, False)
        # Evitar que la ventana se cierre
        # self.root.protocol("WM_DELETE_WINDOW", lambda: None)

    def agregar_widget(self, widget):
        widget.pack()

    def agregar_widget2(self, widget, **kwargs):
        widget.grid(**kwargs)

    def cerrar_ventana(self):
        self.root.winfo_parent()
        self.root.destroy()

    def cambiar_titulo(self, titulo=None):
        self.root.title(titulo)


# =================
# Clase Secundaria.
# =================
# En esta clase, los métodos configuran los widget que se muestran en
# las distintas ventanas relacionadas con los comprobantes.
class ActivitiesWidgets:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal

    def listForm(self):
        marco_search = ctk.CTkFrame(master=self.ventana_principal.root,
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
        # Agregar widget creados en la Clase Principal

        search_entry.grid(row=0, column=0, pady=10, padx=10, sticky='e')
        search_btn.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        self.ventana_principal.agregar_widget2(marco_search)

        marco = ctk.CTkScrollableFrame(master=self.ventana_principal.root,
                                       width=500,
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
                         command=lambda e: select_activity(table, e),
                         )

        table.edit_column(0, width=100)
        table.edit_column(1, width=250, anchor="w")
        table.grid(row=0, column=0, )

        # Agregar widget creado en la Clase Principal
        self.ventana_principal.agregar_widget2(marco)

        # Botones de Acciones
        marco_btns = ctk.CTkFrame(master=self.ventana_principal.root,
                                  width=300,
                                  )

        cancel_btn = ctk.CTkButton(marco_btns, text="Cancelar", width=100,
                                   command=lambda: self.ventana_principal.cerrar_ventana())
        select_btn = ctk.CTkButton(marco_btns, text="Seleccionar", width=100,
                                   command=lambda: selection_return(self.ventana_principal)
                                   if selected_row is not None
                                   else CTkMessagebox(title="Error",
                                                      message="Debe seleccionar un Comprobante para editar",
                                                      icon="cancel"),
                                   )

        marco_btns.grid()

        cancel_btn.grid(row=1, column=1, padx=5, pady=5, )
        select_btn.grid(row=1, column=2, padx=5, pady=5, )

        # Agregar widget creados en la Clase Principal
        self.ventana_principal.agregar_widget2(marco_btns)


# ===================================================================
#  Métodos que manejan la creación de widget de las distintas ventanas
# ===================================================================

def create_window():
    # Crear la ventana principal
    root = ctk.CTk()
    ventana_principal = ActivitiesWindow(root)
    # Crear y agregar widgets desde la clase secundaria
    crear_widgets = ActivitiesWidgets(ventana_principal)
    return crear_widgets


def activities(opt=None, ventana_principal=None):
    crear_widgets = create_window()
    crear_widgets.listForm()




if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    activities()
    app.mainloop()
