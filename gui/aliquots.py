import customtkinter as ctk
from tkinter import StringVar, font

from CTkMessagebox import CTkMessagebox
from CTkTable import *

import config
from config import db
import config.functions_grals as fn
from gui.themes.myStyles import *

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None
selected_code = None


def save_record(datos):
    print(datos)
    query = """INSERT INTO invoices (code, description, observations, type_ret, type_cert, type_dc, active_buy, 
    active_sell, numeration, c_fiscal, code_a, code_b, code_c, code_e, code_m, code_t, code_o) VALUES (?, ?, ?, ?, ?, 
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    values = (datos['Code'], datos['Description'], datos['Obs'], datos['TypeRet'], datos['TypeCert'], datos['TypeDC'],
              datos['Op1'], datos['Op2'], datos['Op3'], datos['Op4'], datos['CodeA'], datos['CodeB'], datos['CodeC'],
              datos['CodeE'], datos['CodeM'], datos['CodeT'], datos['CodeO'])

    result = db.insertRecord(query, values)
    if result:
        return True


def update_record(self, datos):
    global selected_row
    global selected_code

    print(datos)
    query = """
        UPDATE _invoices
        SET code = ?, description = ?, observations = ?, type_ret = ?, type_cert = ?, type_dc = ?,
            active_buy = ?, active_sell = ?, numeration = ?, c_fiscal = ?, code_a = ?, code_b = ?,
            code_c = ?, code_e = ?, code_m = ?, code_t = ?, code_o = ?
        WHERE id = ?
    """
    values = (datos['Code'], datos['Description'], datos['Obs'], datos['TypeRet'], datos['TypeCert'],
              datos['TypeDC'], datos['Op1'], datos['Op2'], datos['Op3'], datos['Op4'], datos['CodeA'],
              datos['CodeB'], datos['CodeC'], datos['CodeE'], datos['CodeM'], datos['CodeT'],
              datos['CodeO'], datos['Id'])
    result = db.updateRecord(query, values)

    if result:
        msgbox = CTkMessagebox(title="Ok",
                               message="El registro fue Actualizado correctamente.",
                               icon="check",
                               sound=True,
                               wraplength=400,
                               corner_radius=2,
                               option_1="Aceptar",
                               )
        response = msgbox.get()

        if response == "Aceptar":
            selected_row = None
            invoice_code = ''
            self.ventana_principal.cerrar_ventana()
            invoice()
    else:
        CTkMessagebox(title="Error", message="Ha ocurrido un error.", icon="cancel")


def fetch_records():
    query = "SELECT CODE,DESCRIPTION, IS_GRAL FROM aliquots_iva"
    value = ''
    result = db.fetchRecords(query, value)
    print(result)
    return result


def get_record(record):
    query = "SELECT * FROM aliquots_iva WHERE code = ?"
    value = (record,)
    result = db.fetchRecord(query, value)
    print("Retorna desde alicuots_iva: ", result)
    return result


def get_alicuots_by_date(alicuot):
    print("Leyendo alicuotas por fecha...")
    pass


def select_data(objeto, self, e):
    # 'e' tiene los datos pasados por el widget tabla de donde se hizo el  Click
    global selected_row
    global selected_code

    if selected_row is not None:
        objeto.deselect_row(selected_row)

    objeto.select_row(e["row"])


    selected_row = e["row"]
    selected_code = objeto.get(selected_row, 0)

    self.aliquotGeneral_checkbox.grid(row=0, column=0, padx=10, pady=10)
    self.shows_AliquotsForDate_btn.grid(row=0, column=1, padx=10, )
    valor = int(objeto.get(selected_row, 2))
    self.aliquotGeneral_checkbox.set(1 if valor else 0)

    #make_table_alicuots_by_date(objeto, self, selected_code)

    print(" CODE Selected: ", selected_code)
    print(objeto.get(selected_row, 2))
    print(self.__class__.__name__)
    get_alicuots_by_date(selected_code)


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


def delete_invoice(self):
    global selected_row
    global selected_code
    print("Eliminar Registro: ", invoice_code)
    query = f"DELETE FROM invoices WHERE code='{invoice_code}'"
    result = db.removeRecord(query)
    if result:
        msgbox = CTkMessagebox(title="Ok",
                               message="El registro fue borrado correctamente.",
                               icon="check",
                               sound=True,
                               wraplength=400,
                               corner_radius=2,
                               option_1="Aceptar",
                               )
        response = msgbox.get()

        if response == "Aceptar":
            selected_row = None
            invoice_code = ''
            self.ventana_principal.cerrar_ventana()
            invoice()
        else:
            print("Click 'Yes' to exit!")

def make_table_alicuots_by_date(objeto, self, data):


    value = fetch_records()

    marco_alicuotsByDate = ctk.CTkScrollableFrame(master=self.marco_info,
                                                  width=300,
                                                  corner_radius=0,
                                                  border_width=1,
                                                  border_color="black",
                                                  scrollbar_fg_color="black", )
    marco_alicuotsByDate.grid_rowconfigure(0, weight=1)
    marco_alicuotsByDate.grid_columnconfigure(0, weight=1)

    table_alicuotsByDate = CTkTable(master=marco_alicuotsByDate,
                                    row=len(value),
                                    column=5,
                                    values=value,
                                    border_width=0,
                                    corner_radius=0,
                                    # command=lambda e: select_data(table, self, e),
                                    )
    table_alicuotsByDate.edit_column(0, width=50)
    table_alicuotsByDate.edit_column(1, width=250, anchor="w")
    table_alicuotsByDate.edit_column(2, width=0)
    table_alicuotsByDate.grid(row=0, column=0, )

    marco_alicuotsByDate.grid()


# =================
#  Clase Principal
# =================
class Aliquots:
    def __init__(self, option=None):
        self.option = option
        self.root = ctk.CTkToplevel()
        self.root.title('Alícuotas de IVA')
        self.root.grab_set()
        self.root.config(padx=10, pady=10)
        self.root.resizable(False, False)  # Evitar que la ventana se expanda
        # self.root.protocol("WM_DELETE_WINDOW", lambda: None)  # Evitar que la ventana se cierre

        marco_scroll = ctk.CTkScrollableFrame(master=self.root,
                                              width=300,
                                              corner_radius=0,
                                              border_width=1,
                                              border_color="black",
                                              scrollbar_fg_color="black", )
        marco_scroll.grid_rowconfigure(0, weight=1)
        marco_scroll.grid_columnconfigure(0, weight=1)
        marco_scroll.grid()

        value = fetch_records()  # Leer info desde la base de datos (DB)
        # Crear tabla con la info existente en la DB
        table = CTkTable(master=marco_scroll,
                         row=len(value),
                         column=3,
                         values=value,
                         border_width=0,
                         corner_radius=0,
                         command=lambda e: select_data(table, self, e), )
        table.edit_column(0, width=50)
        table.edit_column(1, width=250, anchor="w")
        table.edit_column(2, width=0)
        table.grid(row=0, column=0, )

        self.marco_info = ctk.CTkFrame(self.root, width=316,
                                       height=50,
                                       border_width=1,
                                       border_color="black",
                                       corner_radius=0, )
        self.marco_info.grid_propagate(False)
        # self.marco_info.grid_configure(ipady=10)



        self.aliquotGeneral_checkbox = ctk.CTkCheckBox(self.marco_info,
                                                       text="Tasa General",
                                                       # variable=datos['TypeRet'],
                                                       onvalue=1,
                                                       offvalue=0)
        self.shows_AliquotsForDate_btn = ctk.CTkButton(self.marco_info, text="Ver Alic. por Fecha",
                                                       width=120,
                                                       command=lambda: get_alicuots_by_date(), )


        self.marco_info.grid()


        self.make_buttons()

    def make_buttons(self):
        marco_btns = ctk.CTkFrame(master=self.root,
                                  width=520,
                                  height=420,
                                  corner_radius=0,
                                  fg_color='transparent',
                                  )
        marco_btns.grid_rowconfigure(0, weight=1)
        marco_btns.grid_columnconfigure(0, weight=1)

        clear_btn = ctk.CTkButton(marco_btns, text="Vaciar", width=120,
                                  command=lambda: limpiar_form(marco),
                                  **style_clear)
        cancel_btn = ctk.CTkButton(marco_btns, text="Cancelar", width=120,
                                   # fg_color='orange',
                                   # hover_color='dark orange',
                                   command=lambda: self.ventana_principal.cerrar_ventana(),
                                   **style_cancel)
        ok_btn = ctk.CTkButton(marco_btns, text="Guardar", width=120,
                               compound='right',
                               command=lambda: validation_form(self, datos, opt),
                               **style_ok
                               )
        # marco_btns.grid_columnconfigure(index=0, minsize=240, )
        # marco_btns.grid_columnconfigure(index=1, minsize=140, )
        # marco_btns.grid_columnconfigure(index=2, minsize=140, )
        # clear_btn.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        cancel_btn.grid(row=0, column=1, padx=5, pady=5, sticky='n')
        ok_btn.grid(row=1, column=1, padx=5, pady=5, sticky='n')
        marco_btns.grid(row=0, column=1, sticky='n')


if __name__ == '__main__':
    from config.SQLite_DB import Database

    data = config.DB_SYS
    db = Database(data)
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    Aliquots('')
    app.mainloop()
