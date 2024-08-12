from tkinter import StringVar
import customtkinter as ctk

class NewCompany(ctk.CTk):
    def __init__(self):
        super().__init__()
        app2 = ctk.CTkToplevel()
        app2.grab_set()
        app2.title('Nueva Empresa')

        # Variables del Formulario
        datos = {
            "id": None,
            "cuit": StringVar(),
            "razon_social": StringVar(),
            "nombre_fantasia": StringVar(),
            "direccion": StringVar(),
            "telefono": StringVar(),
            "TypeDC": StringVar(),
            "Op1": StringVar(),
            "Op2": StringVar(),
            "Op3": StringVar(),
            "Op4": StringVar(),
            "CodeA": StringVar(),
            "CodeB": StringVar(),
            "CodeC": StringVar(),
            "CodeE": StringVar(),
            "CodeM": StringVar(),
            "CodeT": StringVar(),
            "CodeO": StringVar(),
        }

        marco = ctk.CTkFrame(master=app2,
                             width=620,
                             height=420,
                             corner_radius=0,
                             border_width=1,
                             border_color="black",
                             )
        marco.pack()

        # CUIT
        companyCUIT_label = ctk.CTkLabel(marco, text="CUIT",).place(x=10, y=10)
        companyCUIT_entry = ctk.CTkEntry(marco, textvariable=datos['cuit'], width=100).place(x=150, y=10)
        # Razón Social
        companyRZ_label = ctk.CTkLabel(marco, text="Razón Social").place(x=10, y=40)
        companyRZ_entry = ctk.CTkEntry(marco, textvariable=datos['razon_social'], width=300).place(x=150, y=40)
        # Nombre de Fantasia
        companyNF_label = ctk.CTkLabel(marco, text="Nombre de Fantasia",).place(x=10, y=70)
        companyNF_entry = ctk.CTkEntry(marco, textvariable=datos['nombre_fantasia'], width=300).place(x=150, y=70)
        # Dirección
        companyDIR_label = ctk.CTkLabel(marco, text="Dirección",).place(x=10, y=100)
        companyDIR_entry = ctk.CTkEntry(marco, textvariable=datos['direccion'], width=220).place(x=150, y=100)
        # Teléfono
        companyTEL_label = ctk.CTkLabel(marco, text="Teléfono",).place(x=380, y=100)
        companyTEL_entry = ctk.CTkEntry(marco,textvariable=datos['telefono'], width=100).place(x=440, y=100)
        # Número de Dependencia DGI-AFIP
        # companyNDA_label = ctk.CTkLabel(marco, text="Dep. AFIP/DGI",)
        # companyNDA_label.grid(row=4, column=0, padx=5)
        #
        # companyNDA_entry = ctk.CTkEntry(marco,)
        # companyNDA_entry.grid(row=4, column=1, padx=5)
        #
        # # Código de Actividad
        # companyCODA_label = ctk.CTkLabel(marco, text="Cód. Actividad",)
        # companyCODA_label.grid(row=5, column=0, padx=5)
        #
        # companyCODA_entry = ctk.CTkEntry(marco,)
        # companyCODA_entry.grid(row=5, column=1, padx=5)
        #
        # companyCODAD_label = ctk.CTkLabel(marco, text="...",)
        # companyCODAD_label.grid(row=5, column=2, padx=5)
        #
        # # Condición ante el IVA
        # companyIVA_label = ctk.CTkLabel(marco, text="Cond. IVA",)
        # companyIVA_label.grid(row=6, column=0, padx=5)
        #
        # companyIVA_entry = ctk.CTkEntry(marco,)
        # companyIVA_entry.grid(row=6, column=1, padx=5)
        #
        # companyIVAD_label = ctk.CTkLabel(marco, text="...", )
        # companyIVAD_label.grid(row=6, column=2, padx=5)
        #
        # # El que Suscribe...
        # companySUSCR_label = ctk.CTkLabel(marco, text="El que Suscribe",)
        # companySUSCR_label.grid(row=7, column=0, padx=5)
        #
        # companySUSCR_entry = ctk.CTkEntry(marco,)
        # companySUSCR_entry.grid(row=7, column=1, padx=5)
        #
        # # En su Carácter de ...
        # companySUSCC_label = ctk.CTkLabel(marco, text="Carácter",)
        # companySUSCC_label.grid(row=8, column=0, padx=5)
        #
        # companySUSCC_entry = ctk.CTkEntry(marco,)
        # companySUSCC_entry.grid(row=8, column=1, padx=5)
        #
        # # Marco botonera
        # marco_btn = ctk.CTkFrame(marco, )
        # marco_btn.grid(row=9, column=2, columnspan=3)

        # # Crea el botón limpiar formulario
        # btn_limpiar = ctk.CTkButton(marco_btn,
        #                             text="Limpiar...",
        #                             command=lambda: limpiar_form()
        #                             )
        # # Crea el botón cancelar
        # btn_cancelar = ctk.CTkButton(marco_btn,
        #                             text="Cancelar",
        #                             command=lambda: limpiar_form()
        #                             )
        # # Crea el botón de envío
        # btn_guardar = ctk.CTkButton(marco_btn,
        #                             text="Guardar",
        #                             command=lambda: guardar()
        #                             )
        #
        # btn_limpiar.grid(row=0, column=3, padx=8, pady=8)
        # btn_cancelar.grid(row=0, column=4, padx=5, )
        # btn_guardar.grid(row=0, column=5, padx=5, )
        #
        # print("(filas, columnas)", marco.grid_size())
#
#
#
#
# def limpiar_form():
#     pass
# def guardar():
#     pass
#
#
if __name__ == '__main__':
    ventana = NewCompany()
    ventana.mainloop()