from tkinter import StringVar
import customtkinter as ctk

#import comprobanteShow_gui

# Apariencia temporal, luego al finalizar quitar esta linea
ctk.set_appearance_mode("dark")


def selectInvoice():
    print("Seleccionando comprobantes")

    pass





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
    fechaEmision = StringVar()
    fechaReg = StringVar()
    periodo = StringVar()
    concepto = StringVar()
    condIVA = StringVar()
    tipoDoc = StringVar()
    nroDoc = StringVar()
    prov = StringVar()
    neto = StringVar()
    iva = StringVar()
    ivaTotal = StringVar()
    ivaAdic = StringVar()
    concNGExe = StringVar()
    retPerc = StringVar()
    total = StringVar()

    # Título del Formulario
    #title_form_label = ctk.CTkLabel(app2, text="Carga de Comprobantes - COMPRAS", anchor="w")
    #title_form_label.pack()
    # Crea el frame y añádelo a la ventana
    marco = ctk.CTkFrame(app2, width=800, height=500)
    marco.pack(padx=5, pady=5)

    # Diseño de Formulario (Etiquetas Label)
    comprobante_label = ctk.CTkLabel(marco, text="...", )
    proveedor_label = ctk.CTkLabel(marco, text="...", )
    proveedorRS_label = ctk.CTkLabel(marco, text="Razón Social", )
    digPtoVta_label = ctk.CTkLabel(marco, text="Pto.Vta 5 díg", )
    comprTipo_label = ctk.CTkLabel(marco, text="Tipo/Pto.Vta", )
    # comprPtoVta_label = ctk.CTkLabel(marco, text="", )
    comprNro_Label = ctk.CTkLabel(marco, text="Nº", )
    fechaEmision_Label = ctk.CTkLabel(marco, text="F. Emisión", )
    fechaReg_Label = ctk.CTkLabel(marco, text="F. Registración", )
    periodo_Label = ctk.CTkLabel(marco, text="Período", )
    concepto_Label = ctk.CTkLabel(marco, text="Concepto", )
    condIVA_Label = ctk.CTkLabel(marco, text="Cond. IVA", )
    tipoYNroDoc_Label = ctk.CTkLabel(marco, text="Tipo y Nro. doc.", )
    prov_Label = ctk.CTkLabel(marco, text="Provincia", )
    credito_Label = ctk.CTkLabel(marco, text="Total Crédito Fiscal", )
    ivaTotal_Label = ctk.CTkLabel(marco, text="Total I.V.A.", )
    ivaAdic_Label = ctk.CTkLabel(marco, text="Adic. I.V.A.", )
    total_Label = ctk.CTkLabel(marco, text="Total", )

    digPtoVta_checkbox = ctk.CTkCheckBox(marco, text="Pto.Vta 5 díg", variable=digPtoVta, onvalue="on", offvalue="off")

    # Diseño de Formulario (Etiquetas Entry)
    comprobante_entry = ctk.CTkEntry(marco, textvariable=comprobante, width=40)
    proveedor_entry = ctk.CTkEntry(marco, textvariable=proveedor, width=40)
    proveedorRS_entry = ctk.CTkEntry(marco, width=250,)
    comprTipo_entry = ctk.CTkEntry(marco, textvariable=comprTipo, width=23)
    comprPtoVta_entry = ctk.CTkEntry(marco, textvariable=comprPtoVta, width=50)
    comprNro_entry = ctk.CTkEntry(marco, textvariable=comprNro, width=70)
    fechaEmision_entry = ctk.CTkEntry(marco, textvariable=fechaEmision, width=80)
    fechaReg_entry = ctk.CTkEntry(marco, textvariable=fechaEmision, width=70)
    periodo_entry = ctk.CTkEntry(marco, textvariable=fechaEmision, width=70)
    concepto_entry = ctk.CTkEntry(marco, textvariable=concepto, width=250)
    condIVA_entry = ctk.CTkEntry(marco, textvariable=condIVA, width=40)
    tipoDoc_entry = ctk.CTkEntry(marco, textvariable=tipoDoc, width=35)
    nroDoc_entry = ctk.CTkEntry(marco, textvariable=nroDoc, width=100)
    prov_entry = ctk.CTkEntry(marco, textvariable=prov, width=35)
    neto_entry = ctk.CTkEntry(marco, textvariable=neto, width=135)
    iva_entry = ctk.CTkEntry(marco, textvariable=iva, width=135)
    concNGExe_entry = ctk.CTkEntry(marco, textvariable=concNGExe, width=135)
    retPerc_entry = ctk.CTkEntry(marco, textvariable=retPerc, width=135)
    ivaTotal_entry = ctk.CTkEntry(marco, textvariable=ivaTotal, width=135)
    ivaAdic_entry = ctk.CTkEntry(marco, textvariable=ivaAdic, width=135)
    total_entry = ctk.CTkEntry(marco, textvariable=total, width=135)


    # Diseño de Formulario (Etiquetas Button)
    comprobante_btn = ctk.CTkButton(marco, text="Comprobante",  command=lambda: selectInvoice())
    proveedor_btn = ctk.CTkButton(marco, text="Proveedor", )
    neto_btn = ctk.CTkButton(marco, text="Neto/Total", )
    iva_btn = ctk.CTkButton(marco, text="IVA incluido", )
    concNGExe_btn = ctk.CTkButton(marco, text="No Grab./Op.Exenta", )
    retPerc_btn = ctk.CTkButton(marco, text="Ret./Perc./Pgo.a Cta.", )

    # Publicación del Diseño de Formulario (Etiquetas Button)
    comprobante_btn.place(x=10, y=10,)
    proveedor_btn.place(x=10, y=45)
    neto_btn.place(x=50, y=240)
    iva_btn.place(x=50, y=275)
    concNGExe_btn.place(x=50, y=310)
    retPerc_btn.place(x=50, y=345)

    # Publicación del Diseño de Formulario (Etiquetas Label)
    comprobante_label.place(x=170, y=10)
    proveedorRS_label.place(x=230, y=45)
    #digPtoVta_label.place(x=10, y=80)
    digPtoVta_checkbox.place(x=20, y=80)
    comprTipo_label.place(x=170, y=80)
    comprNro_Label.place(x=340, y=80)
    fechaEmision_Label.place(x=470, y=80)
    fechaReg_Label.place(x=470, y=115)
    periodo_Label.place(x=470, y=150)
    concepto_Label.place(x=20, y=150)
    condIVA_Label.place(x=20, y=185)
    tipoYNroDoc_Label.place(x=140, y=185)
    prov_Label.place(x=420, y=185)
    credito_Label.place(x=310, y=275)
    ivaTotal_Label.place(x=150, y=380)
    ivaAdic_Label.place(x=150, y=415)
    total_Label.place(x=150, y=450)
    #
    # # Publicación del Diseño de Formulario (Etiquetas Entry)
    # comprobante_entry.grid(row=0, column=1, padx=5, pady=1, sticky="w")
    proveedor_entry.place(x=170, y=45)
    proveedorRS_entry.place(x=320, y=45)
    comprTipo_entry.place(x=250, y=80)
    comprPtoVta_entry.place(x=280, y=80)
    comprNro_entry.place(x=360, y=80)
    fechaEmision_entry.place(x=560, y=80)
    fechaReg_entry.place(x=560, y=115)
    periodo_entry.place(x=560, y=150)
    concepto_entry.place(x=80, y=150)
    condIVA_entry.place(x=80, y=185)
    tipoDoc_entry.place(x=240, y=185)
    nroDoc_entry.place(x=280, y=185)
    prov_entry.place(x=480, y=185)
    neto_entry.place(x=230, y=240)
    iva_entry.place(x=430, y=275)
    concNGExe_entry.place(x=230, y=310)
    retPerc_entry.place(x=230, y=345)
    ivaTotal_entry.place(x=230, y=380)
    ivaAdic_entry.place(x=230, y=415)
    total_entry.place(x=230, y=450)





# if __name__ == '__main__':
#     ventana = BuyForm()
#     ventana.mainloop()