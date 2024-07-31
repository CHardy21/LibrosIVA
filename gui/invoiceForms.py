import tkinter
from tkinter import ttk

import customtkinter as ctk
from CTkTable import *

from tkinter.messagebox import showerror

import sqlite3
import os
from config.SQLite_DB import Database

# Apariencia temporal, luego al finalizar quitar esta linea
ctk.set_appearance_mode("dark")

db = Database("../config/iva_data.db")
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


class InvoiceForm(ctk.CTk):

    def __init__(self, opt=None):
        super().__init__()
        self.code_invoice = None
        print(opt)
        app2 = ctk.CTkToplevel()
        app2.title('Comprobantes')
        app2.grab_set()
        app2.config(padx=10, pady=10)
        # marco = ctk.CTkFrame(master=app2, width=400, height=250,)
        marco = ctk.CTkScrollableFrame(master=app2,
                                       width=300,
                                       height=250,
                                       corner_radius=0,
                                       border_width=1,
                                       border_color="black",
                                       scrollbar_fg_color="black",
                                       )

        marco.grid_rowconfigure(0, weight=1)
        marco.grid_columnconfigure(0, weight=1)

        # recuperando comprobantes desde la base de datos (DB)
        value = fetch_records()
        # crea la tabla con los comprobantes existentes en la DB
        table = CTkTable(master=marco,
                         row=len(value),
                         column=2,
                         values=value,
                         border_width=0,
                         corner_radius=0,
                         command=lambda e: select_invoice(table, e),
                         # command=lambda e: showerror(title='Atencion', message=e)
                         )

        # table.edit_column(0, width=1, )
        table.edit_column(0, width=50)
        table.edit_column(1, width=250, anchor="w")

        marco.pack()
        # marco.grid(row=0, column=0, columnspan=2)
        table.grid(row=0, column=0, )

        # Botones de Acciones
        marco_btns = ctk.CTkFrame(app2, )

        cancel_btn = ctk.CTkButton(marco_btns, text="Cancelar", )
        select_btn = ctk.CTkButton(marco_btns, text="Seleccionar", )
        new_btn = ctk.CTkButton(marco_btns, text="Nuevo", )
        edit_btn = ctk.CTkButton(marco_btns, text="Editar", )
        marco_btns.pack(pady=15)
        cancel_btn.grid(row=1, column=0, padx=5, pady=5, )
        edit_btn.grid(row=1, column=1, padx=5, pady=5, )
        new_btn.grid(row=1, column=2, padx=5, pady=5, )
        # select_btn.grid(row=1, column=3, padx=5, pady=5, )

        # for row in range(table.rows):
        #     for col in range(table.columns):
        #         table.get(row, col).bind("<Enter>", lambda event, r=row: on_enter(event, r))
        # table.bind("<Enter>", lambda event, r=row: on_enter(event, r))
        #     table.bind("<Leave>", lambda event, r=row: on_leave(event, r))

        def on_enter(event, row):
            table.select_row(row)

        # def on_leave(event, row):
        #     table.deselect_row(row)
def add_btns():
    pass




# def fetch_records():
#     query = "SELECT CODE,DESCRIPTION FROM invoices"
#     f = db.fetchRecord(query)
#     return f
    # global count
    # for rec in f:
    #     tv.insert(parent='', index='0', iid=count, values=(rec[0], rec[1]))
    #     count += 1
    # tv.after(400, refreshData)






if __name__ == '__main__':
    app = InvoiceForm("shows")
    # app = InvoiceFormTest()
    app.mainloop()
