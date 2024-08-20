import customtkinter as ctk
from tkinter import StringVar, font

from CTkMessagebox import CTkMessagebox
from CTkTable import *

from config import db
import config.functions_grals as fn

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None
company_code = None


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


def fetch_records():
    query = "SELECT cuit, fantasy_name, company_name FROM company"
    result = db.fetchRecords(query)
    print(result)
    return result


def get_record(record):
    query = f"SELECT * FROM company WHERE cuit = '{record}'"
    result = db.fetchRecord(query)
    print("valor devuelto: ", result)
    return result


def save_record(self, datos):
    print(datos)
    query = """
            INSERT INTO company 
            (cuit,company_name,fantasy_name,working_path,address,phone,dependency_afip,activity_code,iva_conditions,
            month_close,taxpayer_type,undersigned,undersigned_character) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
    values = (datos['cuit'], datos['company_name'], datos['fantasy_name'], datos['working_path'], datos['address'],
              datos['phone'], datos['dependency_afip'], datos['activity_code'], datos['iva_conditions'],
              datos['month_close'], datos['taxpayer_type'], datos['undersigned'], datos['undersigned_character'])

    result = db.insertRecord(query, values)

    if result:
        msgbox = CTkMessagebox(title="Nueva Empresa",
                               header=True,
                               message="La Empresa fue creada correctamente.",
                               icon="check",
                               sound=True,
                               wraplength=400,
                               option_1="Aceptar",
                               )
        response = msgbox.get()
        if response == "Aceptar":
            self.ventana_principal.cerrar_ventana()
            company()
    else:
        print("=> ERROR con DB...(Front MSG)")


def update_record(self, datos):
    print(datos)
    query = """
        UPDATE company
        SET cuit=?, company_name=?, fantasy_name=?, working_path=?, address=?,phone=?, dependency_afip=?,
        activity_code=?, iva_conditions=?, month_close=?, taxpayer_type=?, undersigned=?, undersigned_character=?
        WHERE id = ?
    """
    values = (datos['cuit'], datos['company_name'], datos['fantasy_name'], datos['working_path'], datos['address'],
              datos['phone'], datos['dependency_afip'], datos['activity_code'], datos['iva_conditions'],
              datos['month_close'], datos['taxpayer_type'], datos['undersigned'], datos['undersigned_character'],
              datos['id'])

    result = db.updateRecord(query, values)

    if result:
        msgbox = CTkMessagebox(title="Actualizando datos Empresa",
                               header=True,
                               message="La Empresa fue actualizada correctamente.",
                               icon="check",
                               sound=True,
                               wraplength=400,
                               option_1="Aceptar",
                               )
        response = msgbox.get()
        if response == "Aceptar":
            self.ventana_principal.cerrar_ventana()
            company()
    else:
        print("=> ERROR con DB...(Front MSG)")


def delete_company(self):
    print("Eliminar Registro: ", company_code)
    query = f"DELETE FROM invoices WHERE code='{company_code}'"
    result = db.removeRecord(query)

    if result:
        msgbox = CTkMessagebox(title="Eliminar Empresa",
                               header=True,
                               message="La Empresa fue eliminada correctamente.",
                               icon="check",
                               sound=True,
                               wraplength=400,
                               option_1="Aceptar",
                               )
        response = msgbox.get()
        if response == "Aceptar":
            self.ventana_principal.cerrar_ventana()
            company()
    else:
        print("=> ERROR con DB...(Front MSG)")

# =================
#  Clase Principal
# =================
class CompanyWindow:
    def __init__(self, root):
        self.root = ctk.CTkToplevel()
        self.root.title('Empresas')
        self.root.grab_set()
        self.root.config(padx=4, pady=4)

    def agregar_widget(self, widget):
        widget.pack()

    def agregar_widget2(self, widget):
        widget.grid()

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
                                  width=500,
                                  )

        cancel_btn = ctk.CTkButton(marco_btns, text="Cancelar", width=100,
                                   command=lambda: self.ventana_principal.cerrar_ventana())
        delete_btn = ctk.CTkButton(marco_btns, text="Borrar", width=100,
                                   command=lambda: delete_invoice(self)
                                   if selected_row is not None
                                   else CTkMessagebox(title="Error",
                                                      message="Debe seleccionar una Empresa para Borrar",
                                                      icon="cancel"),
                                   )
        new_btn = ctk.CTkButton(marco_btns, text="Nuevo", width=100,
                                command=lambda: company("new", self.ventana_principal), )
        edit_btn = ctk.CTkButton(marco_btns, text="Editar", width=100,
                                 command=lambda: company("edit", self.ventana_principal)
                                 if selected_row is not None
                                 else CTkMessagebox(title="Error",
                                                    message="Debe seleccionar una Empresa para editar",
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

        elif opt == "edit":
            titulo_ventana = "Editar Empresa"
            self.ventana_principal.cambiar_titulo(titulo_ventana)
            print("Editar Code: ", selected_row, " - ", company_code)
            # Recupera Valores del Formulario desde la DB y se carga al dict datos[...]
            result = get_record(company_code)
            # Variables del Formulario
            datos = {
                'id': StringVar(value=result[0]),
                'cuit': StringVar(value=result[1]),
                'company_name': StringVar(value=result[2]),
                'fantasy_name': StringVar(value=result[3]),
                'working_path': StringVar(value=result[4]),
                'address': StringVar(value=result[5]),
                'phone': StringVar(value=result[6]),
                'dependency_afip': StringVar(value=result[7]),
                'activity_code': StringVar(value=result[8]),
                'iva_conditions': StringVar(value=result[9]),
                'month_close': StringVar(value=result[10]),
                'taxpayer_type': StringVar(value=result[11]),
                'undersigned': StringVar(value=result[12]),
                'undersigned_character': StringVar(value=result[13])
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

        marco.grid_rowconfigure(0, weight=1)
        marco.grid_columnconfigure(0, weight=1)
        # CUIT
        companyCUIT_label = ctk.CTkLabel(marco, text="CUIT", ).place(x=10, y=10)
        companyCUIT_entry = ctk.CTkEntry(marco, textvariable=datos['cuit'], width=100).place(x=115, y=10)
        # Razón Social
        companyRZ_label = ctk.CTkLabel(marco, text="Razón Social").place(x=10, y=40)
        companyRZ_entry = ctk.CTkEntry(marco, textvariable=datos['company_name'], width=300).place(x=115, y=40)
        # Nombre de Fantasia
        companyNF_label = ctk.CTkLabel(marco, text="Nombre Fantasia", ).place(x=10, y=70)
        companyNF_entry = ctk.CTkEntry(marco, textvariable=datos['fantasy_name'], width=300).place(x=115, y=70)
        # Dirección
        companyDIR_label = ctk.CTkLabel(marco, text="Dirección", ).place(x=10, y=100)
        companyDIR_entry = ctk.CTkEntry(marco, textvariable=datos['address'], width=220).place(x=115, y=100)
        # Teléfono
        companyTEL_label = ctk.CTkLabel(marco, text="Teléfono", ).place(x=350, y=100)
        companyTEL_entry = ctk.CTkEntry(marco, textvariable=datos['phone'], width=100).place(x=415, y=100)
        # Número de Dependencia DGI-AFIP
        companyNDA_label = ctk.CTkLabel(marco, text="Dep. AFIP/DGI", ).place(x=10, y=130)
        companyNDA_entry = ctk.CTkEntry(marco, textvariable=datos['dependency_afip'], width=40).place(x=115, y=130)
        # Código de Actividad
        companyCODA_label = ctk.CTkLabel(marco, text="Cód. Actividad", ).place(x=10, y=160)
        companyCODA_entry = ctk.CTkEntry(marco, textvariable=datos['activity_code'], width=60).place(x=115, y=160)
        companyCODAD_label = ctk.CTkLabel(marco, text="...", ).place(x=185, y=160)
        # Condición ante el IVA
        companyIVA_label = ctk.CTkLabel(marco, text="Cond. IVA", ).place(x=10, y=190)
        companyIVA_entry = ctk.CTkEntry(marco, textvariable=datos['iva_conditions'], width=40).place(x=115, y=190)
        companyIVAD_label = ctk.CTkLabel(marco, text="...", ).place(x=165, y=190)
        # El que Suscribe...
        companySUSCR_label = ctk.CTkLabel(marco, text="El que Suscribe", ).place(x=10, y=220)
        companySUSCR_entry = ctk.CTkEntry(marco, textvariable=datos['undersigned'], width=300).place(x=115, y=220)
        # En su Carácter de ...
        companySUSCC_label = ctk.CTkLabel(marco, text="Carácter", ).place(x=10, y=250)
        companySUSCC_entry = ctk.CTkEntry(marco, textvariable=datos['undersigned_character'], width=200).place(x=115,
                                                                                                               y=250)

        marco_btns = ctk.CTkFrame(master=self.ventana_principal.root,
                                  width=620,
                                  height=420,
                                  corner_radius=0,
                                  fg_color='transparent'
                                  )
        marco_btns.grid_rowconfigure(0, weight=1)
        marco_btns.grid_columnconfigure(0, weight=1)

        clear_btn = ctk.CTkButton(marco_btns, text="Vaciar", width=120,
                                  fg_color='transparent',
                                  command=lambda: limpiar_form(marco))
        cancel_btn = ctk.CTkButton(marco_btns, text="Cancelar", width=120,
                                   fg_color='orange',
                                   hover_color='dark orange',
                                   command=lambda: self.ventana_principal.cerrar_ventana())
        ok_btn = ctk.CTkButton(marco_btns, text="Guardar", width=120,
                               fg_color='green',
                               hover_color='dark green',
                               compound='right',
                               command=lambda: validation_form(self, datos, opt)
                               )

        clear_btn.grid(row=0, column=0, columnspan=2, padx=15, pady=5, )
        cancel_btn.grid(row=0, column=2, padx=10, pady=5, )
        ok_btn.grid(row=0, column=3, padx=15, pady=5, )

        print(marco.grid_slaves())
        self.ventana_principal.agregar_widget2(marco)
        self.ventana_principal.agregar_widget2(marco_btns)

        def validation_form(self, dataForm, optt):

            if dataForm['id'] is not None:
                value = dataForm['id'].get()  # Accede al método get() aquí
            else:
                value = ""  # Maneja el caso en que dataForm['Id'] es None, o sea cuando opt = "new"

            # Recuperando Datos Del Formulario
            datos = {
                'id': value,
                'cuit': dataForm['cuit'].get(),
                'company_name': dataForm['company_name'].get(),
                'fantasy_name': dataForm['fantasy_name'].get(),
                'working_path': dataForm['working_path'].get(),
                'address': dataForm['address'].get(),
                'phone': dataForm['phone'].get(),
                'dependency_afip': dataForm['dependency_afip'].get(),
                'activity_code': dataForm['activity_code'].get(),
                'iva_conditions': dataForm['iva_conditions'].get(),
                'month_close': dataForm['month_close'].get(),
                'taxpayer_type': dataForm['taxpayer_type'].get(),
                'undersigned': dataForm['undersigned'].get(),
                'undersigned_character': dataForm['undersigned_character'].get()
            }

            error = {}
            count = 0
            msg = ""

            # Validando los Datos del Formulario
            if not fn.validar_cuit(datos['cuit']):
                count += 1
                error[count] = "CUIT incorrecto."

            if not fn.validate_txt(datos['company_name'], 5, 50, str):
                count += 1
                error[count] = "Razón Social debe contener 5-50 caracteres."

            # if not validar.validar_string(datos['TypeDC'], "DCdc"):
            #     count += 1
            #     error[count] = "Debe indicar Débito o Crédito (D/C)."
            #
            # if not validar.validar_string(datos['Op1'], "SNsn "):
            #     count += 1
            #     error[count] = "Debe indicar si tiene numeración (S/N)."
            #
            # if not validar.validar_string(datos['Op2'], "SNsn"):
            #     count += 1
            #     error[count] = "Debe indicar si esta activo para Compras (S/N)."
            #
            # if not validar.validar_string(datos['Op3'], "SNsn"):
            #     count += 1
            #     error[count] = "Debe indicar si esta activo para Ventas (S/N)."

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
                    save_record(self, datos)

                elif optt == "edit":
                    update_record(self, datos)


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

def create_window():
    # Crear la ventana principal
    root = ctk.CTk()
    ventana_principal = CompanyWindow(root)
    # Crear widgets desde la clase secundaria
    crear_widgets = CompanyWidgets(ventana_principal)
    return crear_widgets


def company(opt=None, ventana_principal=None):
    match opt:
        case "new":
            # Cerrar la ventana actual
            if ventana_principal is not None:
                ventana_principal.cerrar_ventana()
            crear_widgets = create_window()
            crear_widgets.dataForm("new")

        case "edit":
            # Cerrar la ventana actual
            ventana_principal.cerrar_ventana()
            crear_widgets = create_window()
            crear_widgets.dataForm("edit")

        case _:
            crear_widgets = create_window()
            crear_widgets.listForm()


if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    company()
    app.mainloop()
