from tkinter import StringVar, font
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from CTkTable import *

from config import db
import config.functions_grals as fn
from gui.activitiesToFind import ActivitiesToFind
from gui.taxStatusShow import TaxStatusShow

font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None
company_code = None
secondaryWin = None
# principalWin = None


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
    result = db.fetchRecords(query, value='')
    print(result)
    return result


def get_record(record):
    query = "SELECT * FROM company WHERE cuit = ?"
    value = (record,)
    result = db.fetchRecord(query, value)
    print("valor devuelto por DB: ", result)
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
    query = f"DELETE FROM company WHERE cuit='{company_code}'"
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


def get_secondary_data(table, dato, value):
    query = f"SELECT * FROM {table} WHERE  {dato} = ?"
    value = (value,)
    result = db.fetchRecord(query, value)
    print("valor devuelto por DB: ", result)
    return result


# =================
#  Clase Principal
# =================
class CompanyWindow:

    def __init__(self, root):
        self.root = ctk.CTkToplevel()
        self.root.title('Empresas')
        self.root.grab_set()
        self.root.config(padx=4, pady=4)
        # Evitar que la ventana se expanda
        self.root.resizable(False, False)
        # Evitar que la ventana se cierre
        # self.root.protocol("WM_DELETE_WINDOW", lambda: None)
        self.valor_seleccionado = None
        # self.widgetUpdate = None
        # self.principalWin = self

    def agregar_widget(self, widget):
        widget.pack()

    def agregar_widget2(self, widget, **kwargs):
        widget.grid(**kwargs)

    def cerrar_ventana(self):
        print(self.root.winfo_parent())
        self.root.destroy()

    def min_max_ventana(self, action):
        if action == 'min':
            self.root.iconify()
        elif action == 'restore':
            self.root.deiconify()

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
                                   command=lambda: delete_company(self)
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
        statusEntry = 'normal'
        # opt="new" - Muestra el formulario vacío.
        # opt="edit" - Muestra el formulario con los datos del registro seleccionado para ser editado
        if opt == "new":
            titulo_ventana = "Nueva Empresa"
            self.ventana_principal.cambiar_titulo(titulo_ventana)
            # Inicializa el dict datos[...] con las Variables del Formulario
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
            statusEntry = 'disabled'

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
        companyCUIT_entry = ctk.CTkEntry(marco, textvariable=datos['cuit'], width=100, state=statusEntry)
        companyCUIT_entry.place(x=115, y=10)
        companyCUIT_entry.focus()
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
        self.companyCODA_entry = ctk.CTkEntry(marco, textvariable=datos['activity_code'], width=60)
        self.companyCODA_entry.place(x=115, y=160)
        self.companyCODAD_label = ctk.CTkLabel(marco, text="...", )
        self.companyCODAD_label.place(x=200, y=160)
        btn_searchCA = ctk.CTkButton(marco, width=8, height=8,
                                     corner_radius=25, text='?',
                                     command=lambda: abrir_ventana_sec2(self, 'activities'), )
        btn_searchCA.place(x=180, y=164, )

        # Condición ante el IVA
        companyIVA_label = ctk.CTkLabel(marco, text="Cond. IVA", ).place(x=10, y=190)
        self.companyIVA_entry = (ctk.CTkEntry(marco, textvariable=datos['iva_conditions'], width=40))
        self.companyIVA_entry.place(x=115, y=190)
        self.companyIVAD_label = (ctk.CTkLabel(marco, text="...", ))
        self.companyIVAD_label.place(x=180, y=190)
        btn_searchIC = ctk.CTkButton(marco, width=8, height=8,
                                     corner_radius=1_000_000, text='?',
                                     command=lambda: abrir_ventana_sec2(self, 'taxstatus'), )
        btn_searchIC.place(x=160, y=194, )

        month_default = datos['month_close'].get()

        print('=> ', month_default)

        # Mes de cierre...
        companyMonthClose_label = ctk.CTkLabel(marco, text="Mes de cierre:", ).place(x=10, y=220)
        companyMonthClose_entry = ctk.CTkEntry(marco, textvariable=datos['month_close'], width=30).place(x=115, y=220)

        # El que Suscribe...
        companySUSCR_label = ctk.CTkLabel(marco, text="El que Suscribe", ).place(x=10, y=250)
        companySUSCR_entry = ctk.CTkEntry(marco, textvariable=datos['undersigned'], width=200).place(x=115, y=250)
        # En su Carácter de ...
        companySUSCC_label = ctk.CTkLabel(marco, text="Carácter", ).place(x=10, y=280)
        companySUSCC_entry = ctk.CTkEntry(marco, textvariable=datos['undersigned_character'], width=200).place(x=115,
                                                                                                               y=280)
        self.marco_taxpayer = ctk.CTkFrame(master=self.ventana_principal.root,
                                           width=180,
                                           height=360,
                                           corner_radius=0,
                                           border_width=1,
                                           )
        self.marco_taxpayer.place(x=360, y=190, )
        self.taxPayer_label = ctk.CTkLabel(self.marco_taxpayer, text="Tipo de Contribuyente", ).grid(pady=2)
        # Crear una variable para los botones de radio
        self.radio_var = ctk.IntVar()

        # Crear los botones de radio
        self.taxPayer_RadioB1 = ctk.CTkRadioButton(self.marco_taxpayer, text=" General ", variable=self.radio_var,
                                                   value=1, )
        self.taxPayer_RadioB2 = ctk.CTkRadioButton(self.marco_taxpayer, text=" Gran Contribuyente ",
                                                   variable=self.radio_var,
                                                   value=2, )
        self.taxPayer_RadioB3 = ctk.CTkRadioButton(self.marco_taxpayer, text=" Monotributo ", variable=self.radio_var,
                                                   value=3, )
        self.taxPayer_RadioB1.grid(padx=4, pady=4, sticky='w')
        self.taxPayer_RadioB2.grid(padx=4, pady=4, sticky='w')
        self.taxPayer_RadioB3.grid(padx=4, pady=4, sticky='w')

        marco_btns = ctk.CTkFrame(master=self.ventana_principal.root,
                                  width=520,
                                  height=420,
                                  corner_radius=0,
                                  fg_color='transparent',
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
        marco_btns.grid_columnconfigure(index=0, minsize=240, )
        marco_btns.grid_columnconfigure(index=1, minsize=140, )
        marco_btns.grid_columnconfigure(index=2, minsize=140, )
        clear_btn.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        cancel_btn.grid(row=0, column=1, padx=5, pady=5, sticky='e')
        ok_btn.grid(row=0, column=2, padx=5, pady=5, sticky='e')

        self.ventana_principal.agregar_widget2(marco, row=0, column=0)
        self.ventana_principal.agregar_widget2(marco_btns, row=1, column=0, pady=5)

        if opt == 'edit':
            data = get_secondary_data('sys_activities_eco_f833', 'code', self.companyCODA_entry.get())
            self.asignar_valor('activities', data[1], data[2])
            print('companyIVA_entry: ', self.companyIVA_entry.get())
            data2 = get_secondary_data('tax_status', 'code', self.companyIVA_entry.get())
            self.asignar_valor('taxstatus', data2[1], data2[2])

            pass

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

            if len(datos['fantasy_name']) == 0:
                datos['fantasy_name'] = datos['company_name']

            if not fn.validate_txt(datos['address'], 5, 50, str):
                count += 1
                error[count] = "Debe escribir un domicilio."
            print('-- ', datos['activity_code'])

            if datos['activity_code'] != '':
                if fn.validate_codActividad(db, datos['activity_code']):
                    pass
                else:
                    count += 1
                    error[count] = "Debe escribir un Código de Actividad Válido."
            else:
                count += 1
                error[count] = "Debe escribir un Código de Actividad Válido."

            if not fn.validate_condIVA(db, datos['iva_conditions']):
                count += 1
                error[count] = "Condición ante IVA No Válido."

            if not fn.verificar_rango(datos['month_close'], (0, 13)):
                count += 1
                error[count] = "Mes de cierre No Válido."

            # if not validar.validar_string(datos['Op3'], "SNsn"):
            #     count += 1
            #     error[count] = "Debe indicar si esta activo para Ventas (S/N)."

            print("'Resultado de la Validación'")
            print(datos, "Cantidad de elementos:      ", len(datos))
            print(error, "Cant. Errores de Validacón: ", len(error))

            if len(error) > 0:
                for txt, i in enumerate(error):
                    msg += "* " + error[i] + "\n"
                CTkMessagebox(header=True,
                              title="Error",
                              message=msg,
                              icon="cancel",
                              sound=True,
                              wraplength=400,
                              option_1="Aceptar",
                              )
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

        def abrir_ventana_sec2(self, secondaryWin):
            print('Abriendo ventana secundaria de Consulta...{}')
            self.ventana_principal.min_max_ventana('min')
            if secondaryWin == 'activities':
                ventana_secundaria = ActivitiesToFind(self)
            if secondaryWin == 'taxstatus':
                ventana_secundaria = TaxStatusShow(self)
            # Maximizando la ventana
            # self.after(1, self.wm_state, 'zoomed')

    def asignar_valor(self, ventana, valor, description):
        self.ventana_principal.min_max_ventana('restore')
        # Función recibe los valores de lo seleccionado en la ventana secundaria y actualiza
        # el formulario actual
        print("Valor Recibido de ventana secundaria: ", valor)
        match ventana:
            case "activities":
                self.companyCODA_entry.delete(0, ctk.END)
                self.companyCODA_entry.insert(0, valor)
                self.companyCODAD_label.configure(text=description)
            case "taxstatus":
                self.companyIVA_entry.delete(0, ctk.END)
                self.companyIVA_entry.insert(0, valor)
                self.companyIVAD_label.configure(text=description)

        # widgets_secundarios = self.ventana_principal.root.winfo_children()
        # for widget in widgets_secundarios:
        #     print(f"Nombre del widget: {widget.winfo_class()}")
        #     print(f"Nombre del widget: {widget.winfo_children()}")


# ===================================================================
#  Método que maneja la creación de widget de las distintas ventanas
# ================actualizar_entry===================================================

def create_window():
    global principalWin
    # Crear la ventana principal
    root = ctk.CTk()
    ventana_principal = CompanyWindow(root)
    # Crear widgets desde la clase secundaria
    crear_widgets = CompanyWidgets(ventana_principal)
    principalWin = root
    return crear_widgets


def company(opt=None, ventana_principal=None):
    match opt:
        case "new":
            # Cerrar la ventana actual
            if ventana_principal is not None:
                ventana_principal.cerrar_ventana()
            crear_widgets = create_window()
            crear_widgets.dataForm("new")
            print("*** ", ventana_principal)
            # crear_widgets.ventana_principal.root.mainloop()

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
