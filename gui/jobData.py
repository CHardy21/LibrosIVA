from tkinter import StringVar
import customtkinter as ctk
from gui.themes.myStyles import *

from config import db
import config.functions_grals as fn
from gui.themes.myStyles import *


class SelectCompany(ctk.CTk):
    def __init__(self):

        super().__init__()
        app2 = ctk.CTkToplevel()
        app2.grab_set()

        app2.title('Datos de Trabajo')
        #
        # Variables del Formulario
        companyRS = StringVar()
        companyCUIT = StringVar()
        companyPerMonth = StringVar()
        companyPerYear = StringVar()

        # Crea el frame y añádelo a la ventana
        marco = ctk.CTkFrame(app2, height=180, width=340, )
        marco.pack(padx=5, pady=5)

        companyRS_label = ctk.CTkLabel(marco, text="Razón Social", ).place(x=10, y=10)
        self.companyRS_entry = (ctk.CTkEntry(marco, textvariable=companyRS, width=200))
        self.companyRS_entry.place(x=100, y=10)

        btn_searchRS = ctk.CTkButton(marco, width=8, height=8,
                                     corner_radius=25, text='?',
                                     command=lambda: self.abrir_ventana_sec2(self, 'activities'), )
        btn_searchRS.place(x=305, y=14, )

        companyCUIT_label = ctk.CTkLabel(marco, text="CUIT", ).place(x=10, y=45)
        companyCUIT_entry = ctk.CTkEntry(marco, textvariable=companyCUIT, width=90).place(x=100, y=45)
        companyPer_label = ctk.CTkLabel(marco, text="Período:", ).place(x=10, y=80)
        companyPerMonth_label = ctk.CTkLabel(marco, text="Mes", ).place(x=80, y=80)
        companyPerMonth_entry = ctk.CTkEntry(marco, textvariable=companyPerMonth, width=30).place(x=110, y=80)
        companyPerYear_label = ctk.CTkLabel(marco, text="Año", ).place(x=150, y=80)
        companyPerYear_entry = ctk.CTkEntry(marco, textvariable=companyPerYear, width=45).place(x=180, y=80)

        #  command=lambda: selectInvoice()
        clear_btn = ctk.CTkButton(marco, text="Vaciar", width=80, **style_clear)
        cancel_btn = ctk.CTkButton(marco, text="Cancelar", width=100, **style_cancel)
        ok_btn = ctk.CTkButton(marco, text="Confirmar", width=100, **style_ok)

        clear_btn.place(x=10, y=140)
        cancel_btn.place(x=120, y=140)
        ok_btn.place(x=230, y=140)

    def abrir_ventana_sec2(self, secondaryWin):
        print('Abriendo ventana secundaria de Consulta...{}')
        self.min_max_ventana('min')
        if secondaryWin == 'activities':
            ventana_secundaria = ActivitiesToFind(self)
        if secondaryWin == 'taxstatus':
            ventana_secundaria = TaxStatusShow(self)
        # Maximizando la ventana
        # self.after(1, self.wm_state, 'zoomed')

    def min_max_ventana(self, action):
        if action == 'min':
            self.iconify()
        elif action == 'restore':
            self.deiconify()


if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    ventana = SelectCompany()
    ventana.mainloop()
