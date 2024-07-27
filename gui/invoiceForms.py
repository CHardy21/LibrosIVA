import customtkinter as ctk
from CTkTable import *

from tkinter.messagebox import showerror

import sqlite3
import os
from config.SQLite_DB import Database

# from config.db_sys.SQLite_DB import Database

# Obtenemos la raíz de la carpeta del proyecto
carpeta_principal = os.path.dirname(__file__)

carpeta_respaldo = os.path.join(carpeta_principal, "config/db_sys/iva_data.db")
# from cliente import Cliente
# from cliente_dao import ClienteDAO
db = Database("../config/iva_data.db")
# conx = sqlite3.connect("../config/iva_data.db")

class InvoiceForm(ctk.CTk):
   def __init__(self):
        super().__init__()
        self.id_invoice = None

        app2 = ctk.CTkToplevel()
        app2.title('Comprobantes')
        app2.grab_set()

        # self.configurar_ventana()
        # self.configurar_grid()
        # self.mostrar_titulo()
        # self.mostrar_formulario()
        # self.cargar_tabla()
        # self.mostrar_botones()

        value = [["FACT", "Factura", 3, 4, 5],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5]]

        fetch_records()

        table = CTkTable(master=app2,
                         row=3,
                         column=2,
                         values=value,
                         border_width=1,
                         corner_radius=1,
                         command=lambda e: showerror(title='Atencion', message=e))

        table.edit_column(0, width=50)

        table.pack(expand=True, fill="both", padx=20, pady=20)

def fetch_records():
    query = "SELECT ID,CODE,DESCRIPTION FROM invoices"
    print(query)
    result = db.fetchRecord(query)

    print(result)
        # global count
        # for rec in f:
        #     tv.insert(parent='', index='0', iid=count, values=(rec[0], rec[1], rec[2], rec[3]))
        #     count += 1
        # tv.after(400, refreshData)


if __name__ == '__main__':
  app = InvoiceForm()
  app.mainloop()