import customtkinter as ctk

ctk.set_appearance_mode("dark")

class NewCompany:
    app2 = ctk.CTkToplevel()
    app2.title('Módulo Empresas')
    app2.grab_set()

    # Crea el frame y añádelo a la ventana
    marco = ctk.CTkFrame(app2)
    marco.pack(padx=5, pady=5)

    # Razón Social
    companyRZ_label = ctk.CTkLabel(marco, text="Razón Social", anchor="w")
    companyRZ_label.grid(row=0, column=0, padx=5)

    companyRZ_entry = ctk.CTkEntry(marco,)
    companyRZ_entry.grid(row=0, column=1, padx=5, columnspan=2, sticky="w")

    # Nombre de Fantasia
    companyNF_label = ctk.CTkLabel(marco, text="Nombre de Fantasia",)
    companyNF_label.grid(row=1, column=0, padx=5)

    companyNF_entry = ctk.CTkEntry(marco,)
    companyNF_entry.grid(row=1, column=1, padx=5)

    # CUIT
    companyCUIT_label = ctk.CTkLabel(marco, text="CUIT",)
    companyCUIT_label.grid(row=2, column=0, padx=5)

    companyCUIT_entry = ctk.CTkEntry(marco,)
    companyCUIT_entry.grid(row=2, column=1, padx=5)

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

    # Condición ante el IVA
    companyIVA_label = ctk.CTkLabel(marco, text="Cód. Actividad",)
    companyIVA_label.grid(row=6, column=0, padx=5)

    companyIVA_entry = ctk.CTkEntry(marco,)
    companyIVA_entry.grid(row=6, column=1, padx=5)




    app2.mainloop()




if __name__ == '__main__':
    ventana_login = NewCompany()