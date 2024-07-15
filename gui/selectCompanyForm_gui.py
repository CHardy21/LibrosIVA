from tkinter import StringVar
import customtkinter as ctk


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
        marco = ctk.CTkFrame(app2, height=180, width=340,)
        marco.pack(padx=5, pady=5)


        companyRS_label = ctk.CTkLabel(marco, text="Razón Social",).place(x=10, y=10)
        companyRS_entry = ctk.CTkEntry(marco, textvariable=companyRS, width=200).place(x=100, y=10)
        companyCUIT_label = ctk.CTkLabel(marco, text="CUIT", ).place(x=10, y=45)
        companyCUIT_entry = ctk.CTkEntry(marco, textvariable=companyCUIT, width=90).place(x=100, y=45)
        companyPer_label = ctk.CTkLabel(marco, text="Período:", ).place(x=10, y=80)
        companyPerMonth_label = ctk.CTkLabel(marco, text="Mes", ).place(x=80, y=80)
        companyPerMonth_entry = ctk.CTkEntry(marco, textvariable=companyPerMonth, width=30).place(x=110, y=80)
        companyPerYear_label = ctk.CTkLabel(marco, text="Año", ).place(x=150, y=80)
        companyPerYear_entry = ctk.CTkEntry(marco, textvariable=companyPerYear, width=45).place(x=180, y=80)

        #  command=lambda: selectInvoice()
        ok_btn = ctk.CTkButton(marco, text="Confirmar", width=60,)
        clear_btn = ctk.CTkButton(marco, text="Borrar", width=60,)
        cancel_btn = ctk.CTkButton(marco, text="Cancelar", width=60,)

        ok_btn.place(x=60, y=140)
        clear_btn.place(x=145, y=140)
        cancel_btn.place(x=220, y=140)



if __name__ == '__main__':
    ventana = SelectCompany()
    ventana.mainloop()
