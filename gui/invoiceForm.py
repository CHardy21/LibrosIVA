import tkinter.font as tkf
from tkinter import StringVar, font
import customtkinter as ctk

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, tkf.BOLD)

class InvoiceForm(ctk.CTk):
    def __init__(self):
        super().__init__()
        app2 = ctk.CTkToplevel()
        app2.grab_set()

        app2.title('Comprobantes')
        #
        # Variables del Formulario
        invoiceCode = StringVar()
        invoiceDescription = StringVar()
        invoiceObs = StringVar()
        invoiceTypeRet = StringVar()
        invoiceTypeCert = StringVar()
        invoiceTypeDC = StringVar()
        invoiceOp1 = StringVar()
        invoiceOp2 = StringVar()
        invoiceOp3 = StringVar()
        invoiceOp4 = StringVar()
        invoiceCodeA = StringVar()
        invoiceCodeB = StringVar()
        invoiceCodeC = StringVar()
        invoiceCodeE = StringVar()
        invoiceCodeM = StringVar()
        invoiceCodeT = StringVar()
        invoiceCodeO = StringVar()

        # Crea el frame y añádelo a la ventana
        marco = ctk.CTkFrame(app2, height=380, width=420,)
        marco.pack(padx=5, pady=5)


        invoiceCode_label = ctk.CTkLabel(marco, text="Código",).place(x=10, y=10)
        invoiceCode_entry = ctk.CTkEntry(marco, textvariable=invoiceCode, width=40).place(x=110, y=10)
        invoiceDescription_label = ctk.CTkLabel(marco, text="Descripción", ).place(x=10, y=40)
        invoiceDescription_entry = ctk.CTkEntry(marco, textvariable=invoiceDescription, width=180).place(x=110, y=40)
        invoiceObs_label = ctk.CTkLabel(marco, text="Observaciones:", ).place(x=10, y=70)
        invoiceObs_entry = ctk.CTkEntry(marco, textvariable=invoiceObs, width=300).place(x=110, y=70)

        invoiceTypeRet_checkbox = ctk.CTkCheckBox(marco, text="Retencion", variable=invoiceTypeRet,
                                                  onvalue="on",
                                                  offvalue="off").place(x=10, y=115)
        invoiceTypeCert_checkbox = ctk.CTkCheckBox(marco, text="Certificado", variable=invoiceTypeCert,
                                                  onvalue="on",
                                                  offvalue="off").place(x=110, y=115)

        invoiceTypeDC_label = ctk.CTkLabel(marco, text="Débito o Crédito (D/C)", )
        invoiceTypeDC_label.place(x=(170 - len(invoiceTypeDC_label.cget("text")) * 6), y=145)
        invoiceTypeDC_entry = ctk.CTkEntry(marco, textvariable=invoiceTypeDC, width=25).place(x=180, y=145)
        invoiceOp1_label = ctk.CTkLabel(marco, text="  Tiene Numeración (S/N) ", )
        invoiceOp1_label.place(x=(170 - len(invoiceOp1_label.cget("text")) * 6), y=175)
        invoiceOp1_entry = ctk.CTkEntry(marco, textvariable=invoiceOp1, width=25).place(x=180, y=175)
        invoiceOp2_label = ctk.CTkLabel(marco, text=" Activo en Compras (S/N) ", )
        invoiceOp2_label.place(x=(170 - len(invoiceOp2_label.cget("text")) * 6), y=205)
        invoiceOp2_entry = ctk.CTkEntry(marco, textvariable=invoiceOp2, width=25).place(x=180, y=205)
        invoiceOp3_label = ctk.CTkLabel(marco, text=" Activo en Ventas (S/N)", )
        invoiceOp3_label.place(x=(170-len(invoiceOp3_label.cget("text"))*6), y=235)
        print(180-len(invoiceOp3_label.cget("text")))
        invoiceOp3_entry = ctk.CTkEntry(marco, textvariable=invoiceOp3, width=25).place(x=180, y=235)
        invoiceOp4_checkbox = ctk.CTkCheckBox(marco, text="Emitido por Controlador Fiscal", variable=invoiceOp4,
                                                   onvalue="on",
                                                   offvalue="off").place(x=10, y=265)

        invoiceCodes_label = ctk.CTkLabel(marco, text="Cód. s/ RG 3685 (AFIP):", font=font_widgets,).place(x=255, y=115)
        invoiceCodeA_label = ctk.CTkLabel(marco, text="Comprobante Tipo A", ).place(x=240, y=145)
        invoiceCodeA_entry = ctk.CTkEntry(marco, textvariable=invoiceCodeA, width=40).place(x=370, y=145)
        invoiceCodeB_label = ctk.CTkLabel(marco, text="Comprobante Tipo B", ).place(x=240, y=175)
        invoiceCodeB_entry = ctk.CTkEntry(marco, textvariable=invoiceCodeA, width=40).place(x=370, y=175)
        invoiceCodeC_label = ctk.CTkLabel(marco, text="Comprobante Tipo C", ).place(x=240, y=205)
        invoiceCodeC_entry = ctk.CTkEntry(marco, textvariable=invoiceCodeA, width=40).place(x=370, y=205)
        invoiceCodeE_label = ctk.CTkLabel(marco, text="Comprobante Tipo E", ).place(x=240, y=235)
        invoiceCodeE_entry = ctk.CTkEntry(marco, textvariable=invoiceCodeA, width=40).place(x=370, y=235)
        invoiceCodeM_label = ctk.CTkLabel(marco, text="Comprobante Tipo M", ).place(x=240, y=265)
        invoiceCodeM_entry = ctk.CTkEntry(marco, textvariable=invoiceCodeA, width=40).place(x=370, y=265)
        invoiceCodeT_label = ctk.CTkLabel(marco, text="Comprobante Tipo T", ).place(x=240, y=295)
        invoiceCodeT_entry = ctk.CTkEntry(marco, textvariable=invoiceCodeA, width=40).place(x=370, y=295)


        #  command=lambda: selectInvoice()
        clear_btn = ctk.CTkButton(marco, text="Borrar", width=80,)
        cancel_btn = ctk.CTkButton(marco, text="Cancelar", width=80, command=lambda: self.destroy())
        ok_btn = ctk.CTkButton(marco, text="Guardar", width=120,)

        clear_btn.place(x=12, y=340)
        cancel_btn.place(x=205, y=340)
        ok_btn.place(x=290, y=340)



if __name__ == '__main__':
    ventana = InvoiceForm()
    ventana.mainloop()
