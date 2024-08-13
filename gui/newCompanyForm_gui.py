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
            'id': StringVar(),
            'cuit': StringVar(),
            'company_name': StringVar(),
            'fantasy_name': StringVar(),
            'working_path': StringVar(),
            'address': StringVar(),
            'phone': StringVar(),
            'dependency_afip': StringVar(),
            'activity_code': StringVar(),
            'iva_conditions': StringVar(),
            'month_close': StringVar(),
            'taxpayer_type': StringVar(),
            'undersigned': StringVar(),
            'undersigned_character': StringVar()
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
        companyCUIT_entry = ctk.CTkEntry(marco, textvariable=datos['cuit'], width=100).place(x=115, y=10)
        # Razón Social
        companyRZ_label = ctk.CTkLabel(marco, text="Razón Social").place(x=10, y=40)
        companyRZ_entry = ctk.CTkEntry(marco, textvariable=datos['company_name'], width=300).place(x=115, y=40)
        # Nombre de Fantasia
        companyNF_label = ctk.CTkLabel(marco, text="Nombre Fantasia",).place(x=10, y=70)
        companyNF_entry = ctk.CTkEntry(marco, textvariable=datos['fantasy_name'], width=300).place(x=115, y=70)
        # Dirección
        companyDIR_label = ctk.CTkLabel(marco, text="Dirección",).place(x=10, y=100)
        companyDIR_entry = ctk.CTkEntry(marco, textvariable=datos['address'], width=220).place(x=115, y=100)
        # Teléfono
        companyTEL_label = ctk.CTkLabel(marco, text="Teléfono",).place(x=350, y=100)
        companyTEL_entry = ctk.CTkEntry(marco, textvariable=datos['phone'], width=100).place(x=415, y=100)
        # Número de Dependencia DGI-AFIP
        companyNDA_label = ctk.CTkLabel(marco, text="Dep. AFIP/DGI",).place(x=10, y=130)
        companyNDA_entry = ctk.CTkEntry(marco, textvariable=datos['dependency_afip'], width=40).place(x=115, y=130)
        # Código de Actividad
        companyCODA_label = ctk.CTkLabel(marco, text="Cód. Actividad",).place(x=10, y=160)
        companyCODA_entry = ctk.CTkEntry(marco, textvariable=datos['activity_code'], width=60).place(x=115, y=160)
        companyCODAD_label = ctk.CTkLabel(marco, text="...",).place(x=185, y=160)
        # Condición ante el IVA
        companyIVA_label = ctk.CTkLabel(marco, text="Cond. IVA",).place(x=10, y=190)
        companyIVA_entry = ctk.CTkEntry(marco, textvariable=datos['iva_conditions'], width=40).place(x=115, y=190)
        companyIVAD_label = ctk.CTkLabel(marco, text="...", ).place(x=165, y=190)
        # El que Suscribe...
        companySUSCR_label = ctk.CTkLabel(marco, text="El que Suscribe",).place(x=10, y=220)
        companySUSCR_entry = ctk.CTkEntry(marco, textvariable=datos['undersigned'], width=300).place(x=115, y=220)
        # En su Carácter de ...
        companySUSCC_label = ctk.CTkLabel(marco, text="Carácter",).place(x=10, y=250)
        companySUSCC_entry = ctk.CTkEntry(marco, textvariable=datos['undersigned_character'], width=200).place(x=115, y=250)

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