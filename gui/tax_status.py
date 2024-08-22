import customtkinter as ctk
from tkinter import StringVar, font

from CTkMessagebox import CTkMessagebox
from CTkTable import *

from config import db
import config.functions_grals as fn

# Fuente para algunos widgets
font_widgets = ('Raleway', 12, font.BOLD)
selected_row = None
tax_status_code = None


def select_tax_status(objeto, e):
    # 'e' tiene los datos pasados por el widget tabla de donde se hizo el Click
    global selected_row
    global tax_status_code
    try:
        if selected_row is not None:
            objeto.deselect_row(selected_row)

        objeto.select_row(e["row"])
        selected_row = e["row"]
        tax_status_code = objeto.get(selected_row, 0)
        print(" CODE Selected: ", tax_status_code)
        # print(e)
    except:
        msgbox = CTkMessagebox(title="Error",
                               header=True,
                               message="Ha ocurrido un error desconocido.",
                               icon="warning",
                               sound=True,
                               wraplength=400,
                               option_1="Aceptar",
                               )
        response = msgbox.get()
        if response == "Aceptar":
            selected_row = None
            tax_status_code = ''


def fetch_records():
    query = "SELECT code, description FROM tax_status"
    result = db.fetchRecords(query)
    print("fetchall: ", result)
    return result


def get_record(record):
    query = f"SELECT * FROM tax_status WHERE code = '{record}'"
    result = db.fetchRecord(query)
    print("fetchone: ", result)
    return result


def save_record(datos):
    print(datos)
    query = """
    NSERT INTO tax_status (code,description,detail_buy,detail_sell,monotributo,magnetic_bracket) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    values = (datos['Code'], datos['description'], datos['detail_buy'], datos['detail_sell'], datos['monotributo'],
              datos['magnetic_bracket'])

    result = db.insertRecord(query, values)
    if result:
        return True


def update_record(self, datos):
    print(datos)
    query = """
        UPDATE tax_status
        SET code = ?, description = ?,detail_buy = ?, detail_sell = ?,
        monotributo = ?, magnetic_bracket= ?
        WHERE id = ?
    """
    values = (datos['code'], datos['description'], datos['detail_buy'], datos['detail_sell'], datos['monotributo'],
              datos['magnetic_bracket'], datos['id'])
    result = db.updateRecord(query, values)

    if result:
        msgbox = CTkMessagebox(title="Actualizando Condiciones Fiscales",
                               header=True,
                               message="Condición Fiscal fue actualizada correctamente.",
                               icon="check",
                               sound=True,
                               wraplength=400,
                               option_1="Aceptar",
                               )
        response = msgbox.get()
        if response == "Aceptar":
            self.ventana_principal.cerrar_ventana()
            tax_status()
    else:
        print("=> ERROR con DB...(Front MSG)")


def delete_tax_status(self):
    global selected_row
    global tax_status_code
    print("Eliminar Registro: ", tax_status_code)

    if selected_row is None:
        CTkMessagebox(title="Error",
                      message="Debe seleccionar un registro para Borrar",
                      icon="cancel")
        return

    query = f"DELETE FROM tax_statu WHERE code='{tax_status_code}'"
    # query = ""
    result = db.removeRecord(query)

    if result:
        msgbox = CTkMessagebox(title="Borrar Condición Fiscal",
                               header=True,
                               message="El registro fue borrado correctamente.",
                               icon="check",
                               sound=True,
                               wraplength=400,
                               option_1="Aceptar",
                               )
        response = msgbox.get()
        if response == "Aceptar":
            selected_row = None
            tax_status_code = ''
            self.ventana_principal.cerrar_ventana()
            tax_status()
    else:
        print("=> ERROR con DB...(Front MSG)")


# =================
#  Clase Principal
# =================
class TaxStatusWindow:
    def __init__(self, root):
        self.root = ctk.CTkToplevel()
        self.root.title('Condiciones Fiscales')
        self.root.grab_set()
        self.root.config(padx=10, pady=10)
        # Evitar que la ventana se expanda
        self.root.resizable(False, False)
        # Evitar que la ventana se minimice
        self.root.protocol("WM_DELETE_WINDOW", lambda: None)

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
class TaxStatusWidgets:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal

    def listForm(self):
        marco = ctk.CTkScrollableFrame(master=self.ventana_principal.root,
                                       width=300,
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
                         column=2,
                         values=value,
                         border_width=0,
                         corner_radius=0,
                         command=lambda e: select_tax_status(table, e),
                         )

        table.edit_column(0, width=50)
        table.edit_column(1, width=250, anchor="w")
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
                                   command=lambda: delete_tax_status(self)
                                   )
        new_btn = ctk.CTkButton(marco_btns, text="Nuevo", width=100,
                                command=lambda: tax_status("new", self.ventana_principal), )
        edit_btn = ctk.CTkButton(marco_btns, text="Editar", width=100,
                                 command=lambda: tax_status("edit", self.ventana_principal)
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
            titulo_ventana = "Nueva Condición Fiscal"
            self.ventana_principal.cambiar_titulo(titulo_ventana)
            # Inicializa el dict datos[...] con las Variables del Formulario
            datos = {
                'id': None,
                'code': StringVar(),
                'description': StringVar(),
                'detail_buy': StringVar(),
                'detail_sell': StringVar(),
                'monotributo': StringVar(),
                'magnetic_bracket': StringVar(),
            }

        elif opt == "edit":
            titulo_ventana = "Editar Condición Fiscal"
            self.ventana_principal.cambiar_titulo(titulo_ventana)
            print("Editar Code: ", selected_row, " - ", tax_status_code)
            # Recupera Valores del Formulario desde la DB y se carga al dict datos[...]
            result = get_record(tax_status_code)
            datos = {
                'id': StringVar(value=result[0]),
                'code': StringVar(value=result[1]),
                'description': StringVar(value=result[2]),
                'detail_buy': StringVar(value=result[3]),
                'detail_sell': StringVar(value=result[4]),
                'monotributo': StringVar(value=result[5]),
                'magnetic_bracket': StringVar(value=result[6]),
            }

        else:
            print("ERROR: opcion no valida")

        # Crea el frame con el formulario y lo añade a la ventana
        marco = ctk.CTkFrame(master=self.ventana_principal.root,
                             width=425,
                             height=260,
                             corner_radius=0,
                             border_width=1,
                             border_color="black",
                             )

        code_label = ctk.CTkLabel(marco, text="Código", ).place(x=10, y=10)
        code_entry = ctk.CTkEntry(marco, textvariable=datos['code'], width=47,
                                  validate="focusout", ).place(x=110, y=10)
        description_label = ctk.CTkLabel(marco, text="Descripción", ).place(x=10, y=40)
        description_entry = ctk.CTkEntry(marco, textvariable=datos['description'], width=180).place(x=110, y=40)

        discrimination_label = ctk.CTkLabel(marco, text="¿Discrimina IVA?", ).place(x=30, y=70)

        marco_discr = ctk.CTkFrame(marco,
                                   width=200,
                                   height=80,
                                   corner_radius=0,
                                   border_width=1,
                                   )
        marco_discr.place(x=10, y=95)

        detailBuy_checkbox = ctk.CTkCheckBox(marco_discr,
                                             text=" Al comprar",
                                             variable=datos['detail_buy'],
                                             onvalue="1",
                                             offvalue="0").place(x=10, y=10)
        detailSell_checkbox = ctk.CTkCheckBox(marco_discr,
                                              text=" Al vender",
                                              variable=datos['detail_sell'],
                                              onvalue="1",
                                              offvalue="0").place(x=10, y=45)

        monotributo_checkbox = ctk.CTkCheckBox(marco,
                                               text=" monotributo",
                                               variable=datos['monotributo'],
                                               onvalue="1",
                                               offvalue="0").place(x=240, y=110)

        magneticBracket_label = ctk.CTkLabel(marco, text="Cód. Soporte Magnético", ).place(x=240, y=140)
        magneticBracket_entry = ctk.CTkEntry(marco, textvariable=datos['magnetic_bracket'], width=30).place(x=380,
                                                                                                            y=140)

        separador_horizontal = ctk.CTkFrame(marco, height=2, width=400, )
        separador_horizontal.place(x=10, y=200)

        clear_btn = ctk.CTkButton(marco, text="Vaciar", width=80,
                                  fg_color='transparent',
                                  command=lambda: limpiar_form(marco))
        cancel_btn = ctk.CTkButton(marco, text="Cancelar", width=80,
                                   command=lambda: self.ventana_principal.cerrar_ventana())
        ok_btn = ctk.CTkButton(marco, text="Guardar", width=120,
                               command=lambda: validation_form(self, datos, opt)
                               )

        clear_btn.place(x=12, y=215)
        cancel_btn.place(x=205, y=215)
        ok_btn.place(x=290, y=215)

        self.ventana_principal.agregar_widget(marco)

        def validation_form(self, dataForm, opt):

            if dataForm['id'] is not None:
                value = dataForm['id'].get()  # Accede al método get() aquí
            else:
                value = ""  # Maneja el caso en que dataForm['Id'] es None, o sea cuando opt = "new"

            # Recuperando Datos Del Formulario
            datos = {
                'id': value,
                'code': dataForm['code'].get().upper(),
                'description': dataForm['description'].get(),
                'detail_buy': dataForm['detail_buy'].get(),
                'detail_sell': dataForm['detail_sell'].get(),
                'monotributo': dataForm['monotributo'].get(),
                'magnetic_bracket': dataForm['magnetic_bracket'].get(),
            }
            error = {}
            count = 0
            msg = ""

            # Validando los Datos del Formulario
            if not fn.validate_txt(datos['code'], 1, 4, str):
                count += 1
                error[count] = "Código de Condición debe contener 1-4 caracteres."

            if not fn.validate_txt(datos['description'], 1, 24, str):
                count += 1
                error[count] = "Descripción debe contener 1-24 caracteres."

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
                if opt == "new":
                    save_record(datos)
                elif opt == "edit":
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
#  Métodos que manejan la creación de widget de las distintas ventanas
# ===================================================================

def create_window():
    # Crear la ventana principal
    root = ctk.CTk()
    ventana_principal = TaxStatusWindow(root)
    # Crear y agregar widgets desde la clase secundaria
    crear_widgets = TaxStatusWidgets(ventana_principal)
    return crear_widgets


def tax_status(opt=None, ventana_principal=None):
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
    tax_status()
    app.mainloop()
