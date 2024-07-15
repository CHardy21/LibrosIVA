import tkinter as tk

import gui.mng_gui


#import app
#from gui.mng_gui import menuEvents


class Menu:
    def __init__(self, parent):
        self.parent = parent
        self.menu_bar = tk.Menu(parent)
        parent.config(menu=self.menu_bar)

        # Creando los Elementos de la barra de menus
        menu_inicio = tk.Menu(self.menu_bar, tearoff=False)
        menu_empresa = tk.Menu(self.menu_bar, tearoff=False)
        menu_registracion = tk.Menu(self.menu_bar, tearoff=False)
        menu_liquidacion = tk.Menu(self.menu_bar, tearoff=False)
        menu_emision = tk.Menu(self.menu_bar, tearoff=False)
        menu_utilidades = tk.Menu(self.menu_bar, tearoff=False)
        menu_ayuda = tk.Menu(self.menu_bar, tearoff=False)

        # Creando los sub-menu de cada Elemento
        # Sub-menu Inicio
        menu_inicio.add_command(label="Nueva Empresa...", accelerator="Ctrl+N",
                                command=lambda: gui.mng_gui.menuEvents("NewCompany"))
        menu_inicio.add_command(label="Seleccionar Datos de Trabajo",
                                command=lambda: gui.mng_gui.menuEvents("workData"))
        menu_inicio.add_separator()
        menu_inicio.add_command(label="Comprobantes")
        menu_inicio.add_command(label="Condiciones Fiscales")
        menu_inicio.add_command(label="Alícuota")
        menu_inicio.add_command(label="Retencionres / Percepciones / Pagos a Cuenta")
        menu_inicio.add_command(label="Imp. Déb. / Créd. Bancarios")
        menu_inicio.add_command(label="Parámetros Monotributo")
        menu_inicio.add_separator()
        menu_inicio.add_command(label="Datos Generales")
        menu_inicio.add_separator()
        menu_inicio.add_command(label="Salir", accelerator="Alt+F4", command=lambda: quit())

        # Sub-menu Empresas
        menu_empresa.add_command(label="Nueva Empresa...", accelerator="Ctrl+N",
                                 command=lambda: gui.mng_gui.menuEvents("NewCompany"))
        menu_empresa.add_command(label="Editar Empresa")
        menu_empresa.add_command(label="Seleccionar Empresa")
        menu_empresa.add_separator()
        menu_empresa.add_command(label="Puntos de Ventas")
        menu_empresa.add_command(label="Tipos de Movimientos")
        menu_empresa.add_command(label="Conceptos No Grabados / Op. Exentas")
        menu_empresa.add_command(label="Clientes")
        menu_empresa.add_command(label="Proveedores")
        menu_empresa.add_command(label="Stock Agropecuario")

        # Sub-menu Registración
        menu_registracion.add_command(label="Compras")
        menu_registracion.add_command(label="Ventas")
        menu_registracion.add_separator()
        menu_registracion.add_command(label="Compras Agropecuarios")
        menu_registracion.add_command(label="Ventas Agropecuarios")
        menu_registracion.add_command(label="Stock Agropecuario")
        menu_registracion.add_separator()
        menu_registracion.add_command(label="Consultas")

        # Sub-menu Liquidación
        menu_liquidacion.add_command(label="Mensual")
        menu_liquidacion.add_command(label="Controles Finales")

        # Sub-menu Emisión
        menu_emision.add_command(label="Compras")
        menu_emision.add_command(label="Ventas")
        menu_emision.add_command(label="Libro IVA Digital")
        menu_emision.add_command(label="Resumen de Compras y Venta")
        menu_emision.add_command(label="Liquidación")
        menu_emision.add_command(label="Retenciones y Percepciones")

        # Sub-menu utilidades
        menu_utilidades.add_command(label="Cómputos Imp. sobre Déb / Cred. Bancarios")
        menu_utilidades.add_separator()
        menu_utilidades.add_command(label="Importación de Datos")
        menu_utilidades.add_command(label="Resguardar / Restaurar")
        menu_utilidades.add_separator()
        menu_utilidades.add_command(label="Varios")
        menu_utilidades.add_command(label="Depurar")

        # Sub-menu Ayuda
        menu_ayuda.add_command(label="Acerca de...")

        self.menu_bar.add_cascade(menu=menu_inicio, label="Inicio")
        self.menu_bar.add_cascade(menu=menu_empresa, label="Empresa")
        self.menu_bar.add_cascade(menu=menu_registracion, label="Registración")
        self.menu_bar.add_cascade(menu=menu_liquidacion, label="Liquidación")
        self.menu_bar.add_cascade(menu=menu_emision, label="Emisión")
        self.menu_bar.add_cascade(menu=menu_utilidades, label="Utilidades")
        self.menu_bar.add_cascade(menu=menu_ayuda, label="Ayuda")
