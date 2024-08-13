import customtkinter as ctk
from tkinter import StringVar, font

from CTkMessagebox import CTkMessagebox
from CTkTable import *

from config import db
import gui.invoices_functions as validar

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None
company_code = None


def save_record(datos):
    print(datos)
    query = """INSERT INTO invoices (code, description, observations, type_ret, type_cert, type_dc, active_buy, 
    active_sell, numeration, c_fiscal, code_a, code_b, code_c, code_e, code_m, code_t, code_o) VALUES (?, ?, ?, ?, ?, 
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    values = (datos['Code'], datos['Description'], datos['Obs'], datos['TypeRet'], datos['TypeCert'], datos['TypeDC'],
              datos['Op1'], datos['Op2'], datos['Op3'], datos['Op4'], datos['CodeA'], datos['CodeB'], datos['CodeC'],
              datos['CodeE'], datos['CodeM'], datos['CodeT'], datos['CodeO'])

    result = db.insertRecord(query, values)
    if result:
        return True


def update_record(datos):
    print(datos)
    query = """
        UPDATE invoices
        SET code = ?, description = ?, observations = ?, type_ret = ?, type_cert = ?, type_dc = ?,
            active_buy = ?, active_sell = ?, numeration = ?, c_fiscal = ?, code_a = ?, code_b = ?,
            code_c = ?, code_e = ?, code_m = ?, code_t = ?, code_o = ?
        WHERE id = ?
    """
    values = (datos['Code'], datos['Description'], datos['Obs'], datos['TypeRet'], datos['TypeCert'],
              datos['TypeDC'], datos['Op1'], datos['Op2'], datos['Op3'], datos['Op4'], datos['CodeA'],
              datos['CodeB'], datos['CodeC'], datos['CodeE'], datos['CodeM'], datos['CodeT'],
              datos['CodeO'], datos['Id'])
    result = db.updateRecord(query, values)

    if result:
        return True


def fetch_records():
    query = "SELECT cuit, fantasy_name, company_name FROM company"
    result = db.fetchRecords(query)
    print(result)
    return result


def get_record(record):
    query = f"SELECT * FROM invoices WHERE code = '{record}'"
    result = db.fetchRecord(query)
    print("valor devuelto: ", result)
    return result


def select_company(objeto, e):
    # 'e' tiene los datos pasados por el widget tabla de donde se hizo el  Click
    global selected_row
    global company_code

    if selected_row is not None:
        objeto.deselect_row(selected_row)

    objeto.select_row(e["row"])
    selected_row = e["row"]
    company_code = objeto.get(selected_row, 0)
    print(" CODE Company Selected: ", company_code)
    print(e)


def delete_company(self):
    print("Eliminar Registro: ", company_code)
    query = f"DELETE FROM invoices WHERE code='{company_code}'"
    result = db.removeRecord(query)
    if result:
        CTkMessagebox(title="Ok", message="El registro fue borrado correctamente.", icon="check", sound=True)
        self.ventana_principal.cerrar_ventana()


# =================
#  Clase Principal
# =================
class CompanyWindow:
    def __init__(self, root):
        self.root = ctk.CTkToplevel()
        self.root.title('Empresas')
        self.root.grab_set()
        self.root.config(padx=10, pady=10)

    def agregar_widget(self, widget):
        widget.pack()

    def cerrar_ventana(self):
        self.root.winfo_parent()
        self.root.destroy()

    def cambiar_titulo(self, titulo=None):
        self.root.title(titulo)


# =================
# Clase Secundaria.
# =================
# En esta clase, los métodos configuran los widget que se muestran en
# las distintas ventanas relacionadas con los comprobantes.
class CompanyWidgets:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal

    def listForm(self):
        marco = ctk.CTkScrollableFrame(master=self.ventana_principal.root,
                                       width=500,
                                       height=250,
                                       corner_radius=0,
                                       border_width=1,
                                       border_color="black",
                                       scrollbar_fg_color="black",
                                       )
        marco.grid_rowconfigure(0, weight=1)
        marco.grid_columnconfigure(0, weight=1)
        # Leer comprobantes desde la base de datos (DB)
        value = fetch_records()
        # Crear tabla con los comprobantes existentes en la DB
        table = CTkTable(master=marco,
                         row=len(value),
                         column=3,
                         values=value,
                         border_width=0,
                         corner_radius=0,
                         command=lambda e: select_company(table, e),
                         )

        table.edit_column(0, width=100)
        table.edit_column(1, width=200, anchor="w")
        table.edit_column(2, width=200, anchor="w")
        table.grid(row=0, column=0, )

        # Agregar widget creado en la Clase Principal
        self.ventana_principal.agregar_widget(marco)

        # Botones de Acciones
        marco_btns = ctk.CTkFrame(master=self.ventana_principal.root,
                                  width=300,
                                  )

        cancel_btn = ctk.CTkButton(marco_btns, text="Cancelar", width=100,
                                   command=lambda: self.ventana_principal.cerrar_ventana())
        delete_btn = ctk.CTkButton(marco_btns, text="Borrar", width=100,
                                   command=lambda: delete_invoice(self)
                                   if selected_row is not None
                                   else CTkMessagebox(title="Error",
                                                      message="Debe seleccionar un Comprobante para Borrar",
                                                      icon="cancel"),
                                   )
        new_btn = ctk.CTkButton(marco_btns, text="Nuevo", width=100,
                                command=lambda: invoice("new", self.ventana_principal), )
        edit_btn = ctk.CTkButton(marco_btns, text="Editar", width=100,
                                 command=lambda: invoice("edit", self.ventana_principal)
                                 if selected_row is not None
                                 else CTkMessagebox(title="Error",
                                                    message="Debe seleccionar un Comprobante para editar",
                                                    icon="cancel"),
                                 )

        marco_btns.pack(pady=15)

        delete_btn.grid(row=1, column=0, padx=15, pady=5, )
        cancel_btn.grid(row=1, column=1, padx=5, pady=5, )
        edit_btn.grid(row=1, column=2, padx=5, pady=5, )
        new_btn.grid(row=1, column=3, padx=5, pady=5, )

        # Agregar widget creados en la Clase Principal
        self.ventana_principal.agregar_widget(marco_btns)

    def dataForm(self, opt=None):
        datos = {}
        # opt="new" - Muestra el formulario vacío.
        # opt="edit" - Muestra el formulario con los datos del registro seleccionado para ser editado
        if opt == "new":
            titulo_ventana = "Nueva Empresa"
            self.ventana_principal.cambiar_titulo(titulo_ventana)
            # Inicializa el dict datos[...] con las Variables del Formulario
            datos = {
                "Id": None,
                "CUIT": StringVar(),
                "Description": StringVar(),
                "Obs": StringVar(),
                "TypeRet": StringVar(),
                "TypeCert": StringVar(),
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

        elif opt == "edit":
            titulo_ventana = "Editar Empresa"
            self.ventana_principal.cambiar_titulo(titulo_ventana)
            print("Editar Code: ", selected_row, " - ", company_code)
            # Recupera Valores del Formulario desde la DB y se carga al dict datos[...]
            result = get_record(company_code)
            datos = {
                "Id": StringVar(value=result[0]),
                "CUIT": StringVar(value=result[1]),
                "Description": StringVar(value=result[2]),
                "Obs": StringVar(value=result[3]),
                "TypeRet": StringVar(value=result[4]),
                "TypeCert": StringVar(value=result[5]),
                "TypeDC": StringVar(value=result[6]),
                "Op1": StringVar(value=result[7]),
                "Op2": StringVar(value=result[8]),
                "Op3": StringVar(value=result[9]),
                "Op4": StringVar(value=result[10]),
                "CodeA": StringVar(value=result[11]),
                "CodeB": StringVar(value=result[12]),
                "CodeC": StringVar(value=result[13]),
                "CodeE": StringVar(value=result[14]),
                "CodeM": StringVar(value=result[15]),
                "CodeT": StringVar(value=result[16]),
                "CodeO": StringVar(value=result[17]),
            }

        else:
            print("ERROR: opcion no valida")

        # Crea el frame con el formulario y lo añade a la ventana
        marco = ctk.CTkFrame(master=self.ventana_principal.root,
                             width=520,
                             height=420,
                             corner_radius=0,
                             border_width=1,
                             border_color="black",
                             )

        # CUIT
        companyCUIT_label = ctk.CTkLabel(marco, text="CUIT", ).place(x=10, y=10)
        companyCUIT_entry = ctk.CTkEntry(marco, textvariable=datos['CUIT'], width=100).place(x=50, y=10)

        #
        # # Razón Social
        # companyRZ_label = ctk.CTkLabel(marco, text="Razón Social")
        # companyRZ_label.grid(row=1, column=0, padx=5, sticky="e")
        #
        # companyRZ_entry = ctk.CTkEntry(marco,)
        # companyRZ_entry.grid(row=1, column=1, padx=5, pady=1, columnspan=2, sticky="w",)
        #
        # # Nombre de Fantasia
        # companyNF_label = ctk.CTkLabel(marco, text="Nombre de Fantasia",)
        # companyNF_label.grid(row=2, column=0, padx=5)
        #
        # companyNF_entry = ctk.CTkEntry(marco,)
        # companyNF_entry.grid(row=2, column=1, padx=5, sticky="w")
        #
        # # Dirección
        # companyDIR_label = ctk.CTkLabel(marco, text="Dirección",)
        # companyDIR_label.grid(row=3, column=0, padx=5)
        #
        # companyDIR_entry = ctk.CTkEntry(marco,)
        # companyDIR_entry.grid(row=3, column=1, padx=5)
        #
        # # Teléfono
        # companyTEL_label = ctk.CTkLabel(marco, text="Teléfono",)
        # companyTEL_label.grid(row=3, column=2, padx=5)
        #
        # companyTEL_entry = ctk.CTkEntry(marco,)
        # companyTEL_entry.grid(row=3, column=3, padx=5)
        #
        # # Número de Dependencia DGI-AFIP
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
        clear_btn = ctk.CTkButton(marco, text="Vaciar", width=80,
                                  command=lambda: limpiar_form(marco))
        cancel_btn = ctk.CTkButton(marco, text="Cancelar", width=80,
                                   command=lambda: self.ventana_principal.cerrar_ventana())
        ok_btn = ctk.CTkButton(marco, text="Guardar", width=120,
                               command=lambda: validation_form(self, datos, opt)
                               )

        clear_btn.place(x=12, y=370)
        cancel_btn.place(x=205, y=370)
        ok_btn.place(x=290, y=370)

        self.ventana_principal.agregar_widget(marco)

        def validation_form(self, dataForm, optt):

            if dataForm['Id'] is not None:
                value = dataForm['Id'].get()  # Accede al método get() aquí
            else:
                value = ""  # Maneja el caso en que dataForm['Id'] es None, o sea cuando opt = "new"

            # Recuperando Datos Del Formulario
            datos = {
                "Id": value,
                "Code": dataForm['Code'].get().upper(),
                "Description": dataForm['Description'].get(),
                "Obs": dataForm['Obs'].get(),
                "TypeRet": dataForm['TypeRet'].get(),
                "TypeCert": dataForm['TypeCert'].get(),
                "TypeDC": dataForm['TypeDC'].get().upper(),
                "Op1": dataForm['Op1'].get().upper(),
                "Op2": dataForm['Op2'].get().upper(),
                "Op3": dataForm['Op3'].get().upper(),
                "Op4": dataForm['Op4'].get(),
                "CodeA": dataForm['CodeA'].get(),
                "CodeB": dataForm['CodeB'].get(),
                "CodeC": dataForm['CodeC'].get(),
                "CodeE": dataForm['CodeE'].get(),
                "CodeM": dataForm['CodeM'].get(),
                "CodeT": dataForm['CodeT'].get(),
                "CodeO": dataForm['CodeO'].get(),
            }
            error = {}
            count = 0
            msg = ""

            # Validando los Datos del Formulario
            if not validar.validate_txt(datos['Code'], 1, 4, str):
                count += 1
                error[count] = "Código de Comprobante debe contener 1-4 caracteres."

            if not validar.validate_txt(datos['Description'], 1, 24, str):
                count += 1
                error[count] = "Descripción de Comprobante debe contener 1-24 caracteres."

            if not validar.validar_string(datos['TypeDC'], "DCdc"):
                count += 1
                error[count] = "Debe indicar Débito o Crédito (D/C)."

            if not validar.validar_string(datos['Op1'], "SNsn "):
                count += 1
                error[count] = "Debe indicar si tiene numeración (S/N)."

            if not validar.validar_string(datos['Op2'], "SNsn"):
                count += 1
                error[count] = "Debe indicar si esta activo para Compras (S/N)."

            if not validar.validar_string(datos['Op3'], "SNsn"):
                count += 1
                error[count] = "Debe indicar si esta activo para Ventas (S/N)."

            print("'Resultado de la Validación'")
            print(datos, "Cantidad de elementos:      ", len(datos))
            print(error, "Cant. Errores de Validacón: ", len(error))

            if len(error) > 0:
                for txt, i in enumerate(error):
                    msg += "* " + error[i] + "\n"
                CTkMessagebox(title="Error", message=msg, icon="cancel")
            else:
                print("Se validaron todos los Datos.")
                if optt == "new":
                    save = save_record(datos)
                    if save:
                        CTkMessagebox(title="Ok", message="El registro fue guardado correctamente.", icon="check", )
                        self.ventana_principal.cerrar_ventana()
                    else:
                        CTkMessagebox(title="Error", message="Ha ocurrido un error.", icon="cancel")
                elif optt == "edit":
                    print("La edicion fue exiosa (Ahora cree la funcion update_record()  :)")
                    print(datos)
                    update = update_record(datos)
                    if update:
                        CTkMessagebox(title="Ok", message="El registro fue Actualizado correctamente.", icon="check", )
                        self.ventana_principal.cerrar_ventana()
                    else:
                        CTkMessagebox(title="Error", message="Ha ocurrido un error.", icon="cancel")

        def limpiar_form(widget):
            widgets = widget.winfo_children()
            print(widgets)
            for entry in widgets:
                if isinstance(entry, ctk.CTkEntry):
                    entry.delete(0, ctk.END)  # Borrar el valor actual
                    entry.insert(0, '')  # Insertar el nuevo valor
                    # print(entry.winfo_name())


# ===================================================================
#  Método que maneja la creación de widget de las distintas ventanas
# ===================================================================
def company(opt=None, ventana_principal=None):
    # # Crear la ventana principal
    # root = ctk.CTk()
    # ventana_principal = InvoiceWindow(root)
    # # Crear y agregar widgets desde la clase secundaria
    # crear_widgets = InvoiceWidgets(ventana_principal)

    match opt:
        case "new":
            # Cerrar la ventana actual y abrir una nueva para el formulario
            ventana_principal.cerrar_ventana()
            root = ctk.CTk()
            ventana_principal = CompanyWindow(root)
            # Crear y agregar widgets desde la clase secundaria
            crear_widgets = CompanyWidgets(ventana_principal)
            crear_widgets.dataForm("new")

        case "edit":
            # Cerrar la ventana actual y abrir una nueva para el formulario
            ventana_principal.cerrar_ventana()
            root = ctk.CTk()
            ventana_principal = CompanyWindow(root)
            # Crear y agregar widgets desde la clase secundaria
            crear_widgets = CompanyWidgets(ventana_principal)
            crear_widgets.dataForm("edit")

        case _:
            # Crear la ventana principal
            root = ctk.CTk()
            ventana_principal = CompanyWindow(root)
            # Crear y agregar widgets desde la clase secundaria
            crear_widgets = CompanyWidgets(ventana_principal)
            crear_widgets.listForm()


if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    company()
    app.mainloop()
