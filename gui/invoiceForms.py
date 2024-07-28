import tkinter

import customtkinter as ctk
from CTkTable import *

from tkinter.messagebox import showerror

import sqlite3
import os
from config.SQLite_DB import Database

# Apariencia temporal, luego al finalizar quitar esta linea
ctk.set_appearance_mode("dark")

db = Database("../config/iva_data.db")


class InvoiceForm(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.id_invoice = None

        app2 = ctk.CTkToplevel()
        app2.title('Comprobantes')
        app2.grab_set()
        app2.config(padx=10, pady=10)
        # marco = ctk.CTkFrame(master=app2, width=400, height=250,)
        marco = ctk.CTkScrollableFrame(master=app2,
                                       width=400,
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
                         column=3,
                         values=value,
                         border_width=0,
                         corner_radius=0,

                         command=lambda e: showerror(title='Atencion', message=e))

        table.edit_column(0, width=1, )
        table.edit_column(1, width=50)
        table.edit_column(2, width=350)


        marco.pack()

        table.grid(row=0, column=0,)


def fetch_records():
    query = "SELECT ID,CODE,DESCRIPTION FROM invoices"
    result = db.fetchRecord(query)
    print(result)
    return result


if __name__ == '__main__':
    app = InvoiceForm()
    app.mainloop()
