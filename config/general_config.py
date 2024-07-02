import os
import tkinter as tk
import customtkinter as ctk

# ---> Rutas
dir_config = os.path.dirname(__file__)
# Carpeta principal
dir_ppal = dir_config[0:len(dir_config)-6]
dir_images = os.path.join(dir_ppal, "images")
dir_gui = os.path.join(dir_ppal, "gui")

print(dir_ppal)
print(dir_images)
print(dir_gui)

# Modo de color y tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Fuente para algunos widgets
font_widgets = ('Raleway', 16, tk.font.BOLD)

# Objeto para manejar bases de datos MySQL
#base_datos = sqlbd.BaseDatos(**sqlbd.acceso_bd)



