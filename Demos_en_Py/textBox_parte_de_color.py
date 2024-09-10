import customtkinter as ctk

# Crear la ventana principal
root = ctk.CTk()

# Crear el CTkTextbox
textbox = ctk.CTkTextbox(root, width=400, height=200)
textbox.pack(padx=20, pady=20)

# Insertar texto en el CTkTextbox
textbox.insert("0.0", "Este es un texto de ejemplo.\nPuedes cambiar el color de una parte del texto.")

# Configurar la etiqueta para cambiar el color del texto
textbox.tag_config("rojo", foreground="red")
textbox.tag_config("azul", foreground="blue")

# Aplicar la etiqueta a una parte específica del texto
textbox.tag_add("rojo", "1.10", "1.15")  # Cambia "ejemplo" a rojo
textbox.tag_add("azul", "2.7", "2.13")   # Cambia "cambiar" a azul

# Ejecutar la aplicación
root.mainloop()
