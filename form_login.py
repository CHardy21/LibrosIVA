import tkinter as tk


#Creación de la ventana principal
root = tk.Tk()
#Título de la ventana
root.title("Aprendiendo Estilos y Marcos")
root.geometry("600x400")

marco = tk.LabelFrame(root, text="Marco en la ventana principal",)
marco.pack()

#Entrada de datos
entrada = tk.Entry(marco,
                   bg="DeepSkyBlue",
                   border=3,
                   foreground="red"
                   )
entrada.pack(pady=10)
entrada.insert(0,"Escriba su nombre...")
entrada.bind("<Button-1>", lambda e: entrada.delete(0, tk.END))

#Función para el botón
def enviar():
    nombre = entrada.get()  # Obtiene y almacena el texto de la entrada
    tk.Label(marco,
             text=f"Hola {nombre}",
             ).pack()
    entrada.delete(0, tk.END)
    entrada.insert(0,"Escriba su nombre...")

#Botón de enviar
boton = tk.Button(marco,
                  text="Enviar",
                  command=enviar,
                  bg="salmon",
                  ).pack()

#Bucle de ejecución
root.mainloop()