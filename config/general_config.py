import os
import customtkinter as ctk
from tkinter.font import BOLD

from config.SQLite_DB import Database

# ---> Definición de Rutas del sistema
DIR_CONFIG = os.path.dirname(__file__)
# Carpeta principal
DIR_ROOT = DIR_CONFIG[0:len(DIR_CONFIG) - 6]
DIR_GUI = os.path.join(DIR_ROOT, "gui")
DIR_IMAGES = os.path.join(DIR_GUI, "images")
DIR_THEMES = os.path.join(DIR_GUI, "themes")
DIR_JOBDATA = os.path.join(DIR_ROOT, "data")

DB_SYS = os.path.join(DIR_CONFIG, "iva_data.db")

# Configurando Apariencia General de la App
my_theme = 'myBlue.json'
theme_path = os.path.join(DIR_THEMES, my_theme)

# theme_path = 'blue'
appearance = 'dark'
# Modo de color y tema
ctk.set_appearance_mode(appearance)
ctk.set_default_color_theme(theme_path)
# Fuente para algunos widgets
font_widgets = ('Raleway', 16, BOLD)

# Objeto para manejar bases de datos MySQL
# data = "../config/iva_data.db"
db = Database(DB_SYS)

# print(DB_SYS)