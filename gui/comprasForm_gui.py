from tkinter import StringVar
import customtkinter as ctk

# Apariencia temporal, luego al finalizar quitar esta linea
ctk.set_appearance_mode("dark")


class BuyForm:
    app2 = ctk.CTkToplevel()
    app2.title('Compras')
    app2.grab_set()
    altoFila = 35

    # Variables del Formulario
    comprobante = StringVar()
    proveedor = StringVar()
    digPtoVta = StringVar()
    comprPtoVta = StringVar()
    comprTipo = StringVar()
    comprNro = StringVar()
    lote = StringVar()
    fecheEmision = StringVar()
    fechaReg = StringVar()
    periodo = StringVar()
    concepto = StringVar()
    condIVA = StringVar()
    tipoDoc = StringVar()
    nroDoc = StringVar()
    prov = StringVar()
    neto = StringVar()
    iva = StringVar()
    concNGExe = StringVar()
    retPerc = StringVar()
    total = StringVar()

    # Título del Formulario
    title_form_label = ctk.CTkLabel(app2, text="Carga de Comprobantes - COMPRAS", anchor="e")
    title_form_label.pack()
    # Crea el frame y añádelo a la ventana
    marco = ctk.CTkFrame(app2, width=800, height=400)
    marco.pack(padx=5, pady=5)

    # Diseño de Formulario (Etiquetas Label)
    comprobante_label = ctk.CTkLabel(marco, text="...", )
    proveedor_label = ctk.CTkLabel(marco, text="...", )
    proveedorRS_label = ctk.CTkLabel(marco, text="Razón Social", )
    digPtoVta_label = ctk.CTkLabel(marco, text="Pto.Vta 5 díg", )
    comprTipo_label = ctk.CTkLabel(marco, text="Tipo/Pto.Vta", )
    # comprPtoVta_label = ctk.CTkLabel(marco, text="", )
    comprNro_Label = ctk.CTkLabel(marco, text="Nº", )

    # Diseño de Formulario (Etiquetas Entry)
    comprobante_entry = ctk.CTkEntry(marco, textvariable=comprobante, width=40)
    proveedor_entry = ctk.CTkEntry(marco, textvariable=proveedor, width=40)
    proveedorRS_entry = ctk.CTkEntry(marco, width=400,)
    comprTipo_entry = ctk.CTkEntry(marco, textvariable=comprTipo, width=23)
    comprPtoVta_entry = ctk.CTkEntry(marco, textvariable=comprPtoVta, width=50)
    comprNro_entry = ctk.CTkEntry(marco, textvariable=comprNro, width=100)

    # Diseño de Formulario (Etiquetas Button)
    comprobante_btn = ctk.CTkButton(marco, text="Comprobante", )
    proveedor_btn = ctk.CTkButton(marco, text="Proveedor", )

    # Publicación del Diseño de Formulario (Etiquetas Button)
    comprobante_btn.place(x=10, y=10)
    proveedor_btn.place(x=10, y=45)

    # Publicación del Diseño de Formulario (Etiquetas Label)
    comprobante_label.place(x=170, y=10)
    proveedorRS_label.place(x=230, y=45)
    digPtoVta_label.place(x=10, y=80)
    comprTipo_label.place(x=170, y=80)
    comprNro_Label.place(x=340, y=80)
    #
    # # Publicación del Diseño de Formulario (Etiquetas Entry)
    # comprobante_entry.grid(row=0, column=1, padx=5, pady=1, sticky="w")
    proveedor_entry.place(x=170, y=45)
    proveedorRS_entry.place(x=320, y=45)
    comprTipo_entry.place(x=250, y=80)
    comprPtoVta_entry.place(x=280, y=80)
    comprNro_entry.place(x=360, y=80)

    app2.mainloop()
