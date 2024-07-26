import tkinter as tk
from tkinter import ttk

import customtkinter as ctk
from CTkTable import *

from tkinter.messagebox import showerror, showinfo

# from cliente import Cliente
# from cliente_dao import ClienteDAO


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

    table = CTkTable(master=app2,
                     row=3,
                     column=2,
                     values=value,
                     border_width=1,
                     corner_radius=1,
                     command=lambda e: showerror(title='Atencion', message=e))

    table.edit_column(0, width=50)

    table.pack(expand=True, fill="both", padx=20, pady=20)



if __name__ == '__main__':
  app = InvoiceForm()
  app.mainloop()