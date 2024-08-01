import os
import customtkinter as ctk
from tkinter.font import BOLD

from config.SQLite_DB import Database

# ---> Rutas
dir_config = os.path.dirname(__file__)
# Carpeta principal
dir_ppal = dir_config[0:len(dir_config) - 6]
dir_gui = os.path.join(dir_ppal, "gui")
dir_images = os.path.join(dir_gui, "images")

print(dir_ppal)
print(dir_gui)
print(dir_images)

# Configurando Apariencia General de la App
# Modo de color y tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
# Fuente para algunos widgets
font_widgets = ('Raleway', 16, BOLD)

# Objeto para manejar bases de datos MySQL
#base_datos = sqlbd.BaseDatos(**sqlbd.acceso_bd)
data = "../config/iva_data.db"
db = Database(data)
