from tkinter import StringVar
import customtkinter as ctk

class NewCompany(ctk.CTk):
    def __init__(self):
        super().__init__()
        app2 = ctk.CTkToplevel()
        app2.grab_set()

        app2.title('Sistema de Registración IVA 1.0')
        # self.configure(fg_color=App.COLOR_VENTANA)
        # self.iconbitmap(os.path.join(conf.dir_images, App.ICONO_VENTANA))

        # Configurar donde se muestra la ventana de la App
        #ancho_app = 900
        #alto_app = 400
        # Pantalla
        # ancho_pantalla = self.winfo_screenwidth()
        # alto_pantalla = self.winfo_screenheight()
        #
        # coordenadas_x = int((ancho_pantalla / 2) - (ancho_app / 2))
        # coordenadas_y = int((alto_pantalla / 2) - (alto_app / 2)) - 37

        # self.geometry("{}x{}+{}+{}".format(ancho_app, alto_app, coordenadas_x, coordenadas_y))
        #
        # # Maximizando la ventana
        # self.after(1, self.wm_state, 'zoomed')



#     app2 = ctk.CTkToplevel()
#     app2.title('Módulo Empresas')
#     app2.grab_set()
#
        # Variables del Formulario
        cuit = StringVar()

        # Título del Formulario
        title_form_label = ctk.CTkLabel(app2, text="Crear Empresa Nueva", anchor="e")
        title_form_label.pack()
        # Crea el frame y añádelo a la ventana
        marco = ctk.CTkFrame(app2, )
        marco.pack(padx=5, pady=5)

        # CUIT
        companyCUIT_label = ctk.CTkLabel(marco, text="CUIT",).grid(row=0, column=0, padx=5, sticky="e")
        companyCUIT_entry = ctk.CTkEntry(marco, textvariable=cuit, width=90)
        companyCUIT_entry.grid(row=0, column=1, padx=5, pady=1, sticky="w")

        # Razón Social
        companyRZ_label = ctk.CTkLabel(marco, text="Razón Social")
        companyRZ_label.grid(row=1, column=0, padx=5, sticky="e")

        companyRZ_entry = ctk.CTkEntry(marco,)
        companyRZ_entry.grid(row=1, column=1, padx=5, pady=1, columnspan=2, sticky="w",)

        # Nombre de Fantasia
        companyNF_label = ctk.CTkLabel(marco, text="Nombre de Fantasia",)
        companyNF_label.grid(row=2, column=0, padx=5)

        companyNF_entry = ctk.CTkEntry(marco,)
        companyNF_entry.grid(row=2, column=1, padx=5, sticky="w")

        # Dirección
        companyDIR_label = ctk.CTkLabel(marco, text="Dirección",)
        companyDIR_label.grid(row=3, column=0, padx=5)

        companyDIR_entry = ctk.CTkEntry(marco,)
        companyDIR_entry.grid(row=3, column=1, padx=5)

        # Teléfono
        companyTEL_label = ctk.CTkLabel(marco, text="Teléfono",)
        companyTEL_label.grid(row=3, column=2, padx=5)

        companyTEL_entry = ctk.CTkEntry(marco,)
        companyTEL_entry.grid(row=3, column=3, padx=5)

        # Número de Dependencia DGI-AFIP
        companyNDA_label = ctk.CTkLabel(marco, text="Dep. AFIP/DGI",)
        companyNDA_label.grid(row=4, column=0, padx=5)

        companyNDA_entry = ctk.CTkEntry(marco,)
        companyNDA_entry.grid(row=4, column=1, padx=5)

        # Código de Actividad
        companyCODA_label = ctk.CTkLabel(marco, text="Cód. Actividad",)
        companyCODA_label.grid(row=5, column=0, padx=5)

        companyCODA_entry = ctk.CTkEntry(marco,)
        companyCODA_entry.grid(row=5, column=1, padx=5)

        companyCODAD_label = ctk.CTkLabel(marco, text="...",)
        companyCODAD_label.grid(row=5, column=2, padx=5)

        # Condición ante el IVA
        companyIVA_label = ctk.CTkLabel(marco, text="Cond. IVA",)
        companyIVA_label.grid(row=6, column=0, padx=5)

        companyIVA_entry = ctk.CTkEntry(marco,)
        companyIVA_entry.grid(row=6, column=1, padx=5)

        companyIVAD_label = ctk.CTkLabel(marco, text="...", )
        companyIVAD_label.grid(row=6, column=2, padx=5)

        # El que Suscribe...
        companySUSCR_label = ctk.CTkLabel(marco, text="El que Suscribe",)
        companySUSCR_label.grid(row=7, column=0, padx=5)

        companySUSCR_entry = ctk.CTkEntry(marco,)
        companySUSCR_entry.grid(row=7, column=1, padx=5)

        # En su Carácter de ...
        companySUSCC_label = ctk.CTkLabel(marco, text="Carácter",)
        companySUSCC_label.grid(row=8, column=0, padx=5)

        companySUSCC_entry = ctk.CTkEntry(marco,)
        companySUSCC_entry.grid(row=8, column=1, padx=5)

        # Marco botonera
        marco_btn = ctk.CTkFrame(marco, )
        marco_btn.grid(row=9, column=2, columnspan=3)

        # Crea el botón limpiar formulario
        btn_limpiar = ctk.CTkButton(marco_btn,
                                    text="Limpiar...",
                                    command=lambda: limpiar_form()
                                    )
        # Crea el botón cancelar
        btn_cancelar = ctk.CTkButton(marco_btn,
                                    text="Cancelar",
                                    command=lambda: limpiar_form()
                                    )
        # Crea el botón de envío
        btn_guardar = ctk.CTkButton(marco_btn,
                                    text="Guardar",
                                    command=lambda: guardar()
                                    )

        btn_limpiar.grid(row=0, column=3, padx=8, pady=8)
        btn_cancelar.grid(row=0, column=4, padx=5, )
        btn_guardar.grid(row=0, column=5, padx=5, )

        print("(filas, columnas)", marco.grid_size())
#
#     app2.mainloop()
#
#
# def limpiar_form():
#     pass
# def guardar():
#     pass
#
#
# if __name__ == '__main__':
#     ventana_login = NewCompany()