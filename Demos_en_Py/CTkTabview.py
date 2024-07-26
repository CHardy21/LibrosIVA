import tkinter as tk
from tkinter import ttk

import customtkinter as ctk
from CTkTable import *

from tkinter.messagebox import showerror, showinfo

# from cliente import Cliente
# from cliente_dao import ClienteDAO


class TabView(ctk.CTk):
  COLOR_VENTANA = '#1d2d44'

  def __init__(self):
    super().__init__()
    self.id_invoice = None

    app2 = ctk.CTkToplevel()
    app2.title('CTk Tabview')
    app2.grab_set()

    tabview = ctk.CTkTabview(master=app2)
    tabview.pack(padx=20, pady=20)

    tabview.add("tab 1")  # add tab at the end
    tabview.add("tab 2")  # add tab at the end
    tabview.set("tab 2")  # set currently visible tab

    button = ctk.CTkButton(master=tabview.tab("tab 1"))
    button.pack(padx=20, pady=20)




if __name__ == '__main__':
  app = TabView()
  app.mainloop()