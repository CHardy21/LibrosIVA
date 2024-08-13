import os
import customtkinter as ctk
from PIL import Image

import config.general_config as conf
import gui.menu_gui as menu

from gui.invoices import invoice
from gui.company import company

from gui.selectCompanyForm_gui import SelectCompany


class Login:
    def __init__(self):
        # Creación de la ventana principal
        self.root = ctk.CTk()
        self.root.title("CHardy© Estudios Contables - Login")
        self.root.iconbitmap(os.path.join(conf.dir_images, "CH.ico"))
        self.root.geometry("400x500")  # Tamaño de la ventana
        self.root.resizable(False, False)  # Bloqueo de redimensión de ventana en alto y ancho

        # Contenido de la ventana principal
        # Carga de la imagen
        logo = ctk.CTkImage(
            light_image=Image.open((os.path.join(conf.dir_images, "logo_claro.png"))),  # Imagen modo claro
            dark_image=Image.open((os.path.join(conf.dir_images, "logo_oscuro.png"))),  # Imagen modo oscuro
            size=(250, 250))  # Tamaño de las imágenes

        # Etiqueta para mostrar la imagen
        etiqueta = ctk.CTkLabel(master=self.root,
                                image=logo,
                                text="")
        etiqueta.pack(pady=15)

        # Campos de texto
        # Usuario
        ctk.CTkLabel(self.root, text="Usuario").pack()
        self.usuario = ctk.CTkEntry(self.root)
        self.usuario.insert(0, "Ej:Laura")
        self.usuario.bind("<Button-1>", lambda e: self.usuario.delete(0, "end"))
        self.usuario.pack()

        # Contraseña
        ctk.CTkLabel(self.root, text="Contraseña").pack()
        self.contrasena = ctk.CTkEntry(self.root)
        self.contrasena.insert(0, "*******")
        self.contrasena.bind("<Button-1>", lambda e: self.contrasena.delete(0, "end"))
        self.contrasena.pack()

        # Botón de envío
        ctk.CTkButton(self.root, text="Entrar", command=self.validar).pack(pady=10)

        # Bucle de ejecución
        self.root.mainloop()

    # Función para validar el login
    def validar(self):
        obtener_usuario = self.usuario.get()  # Obtenemos el nombre de usuario
        obtener_contrasena = self.contrasena.get()  # Obtenemos la contraseña

        # Verifica si el valor que tiene el usuario o la contraseña o ambos no coinciden
        # if obtener_usuario == sqlbd.acceso_bd["user"] or obtener_contrasena == sqlbd.acceso_bd["password"]:
        #     # En caso de tener ya un elemento "info_login" (etiqueta) creado, lo borra
        #     if hasattr(self, "info_login"):
        #         self.info_login.configure(text="Usuario o contraseña incorrectos.")
        #     else:
        #         # Crea esta etiqueta siempre que el login sea incorrecto
        #         self.info_login = ctk.CTkLabel(self.root, text="Usuario o contraseña incorrectos.")
        #         self.info_login.pack()
        # else:
        #     # En caso de tener ya un elemento "info_login" (etiqueta) creado, lo borra
        #     if hasattr(self, "info_login"):
        #         self.info_login.configure(text=f"Hola, {obtener_usuario}. Espere unos instantes...")
        #     else:
        #         # Crea esta etiqueta siempre que el login sea correcto
        #         self.info_login = ctk.CTkLabel(self.root, text=f"Hola, {obtener_usuario}. Espere unos instantes...")
        #         self.info_login.pack()
        # Se destruye la ventana de login
        self.root.destroy()
        # Se instancia la ventana de opciones del programa
        #ventana_opciones = VentanaOpciones()
        app = App()


class App(ctk.CTk):
    COLOR_VENTANA = '#1d2d44'
    ICONO_VENTANA = "CH.ico"
    IMAGEN_FONDO_VENTANA = "VladStudio027.jpg"

    def __init__(self):
        super().__init__()
        #self.app = tk.Tk()

        self.title('Sistema de Registración IVA 1.0')
        self.configure(fg_color=App.COLOR_VENTANA)
        self.iconbitmap(os.path.join(conf.dir_images, App.ICONO_VENTANA))

        # Configurar donde se muestra la ventana de la App
        ancho_app = 900
        alto_app = 400
        # Pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        coordenadas_x = int((ancho_pantalla / 2) - (ancho_app / 2))
        coordenadas_y = int((alto_pantalla / 2) - (alto_app / 2)) - 37

        self.geometry("{}x{}+{}+{}".format(ancho_app, alto_app, coordenadas_x, coordenadas_y))

        # Maximizando la ventana
        # self.after(1, self.wm_state, 'zoomed')

        menu.Menu(self)

        self.mainloop()


def on_click_menu(event):
    print("Click en MENU: ", event)
    if event == "NewCompany":
        form = company('new')
    if event == "workData":
        form = SelectCompany()
    if event == "invoices":
        form = invoice()

    pass
