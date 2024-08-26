import tkinter as tk
from tkinter import ttk

def abrir_ventana_secundaria():
    # Crear una ventana secundaria.
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.config(width=300, height=200)

    # Simula una lista de datos (puedes reemplazar esto con tus datos reales).
    datos = ["Dato 1", "Dato 2", "Dato 3"]

    # Crear una lista desplegable (combobox) con los datos.
    combobox = ttk.Combobox(ventana_secundaria, values=datos)
    combobox.pack(padx=20, pady=20)

    def seleccionar_dato():
        # Obtener el valor seleccionado.
        valor_seleccionado = combobox.get()

        # Actualizar el entry en la ventana principal.
        entry_principal.delete(0, tk.END)  # Borrar el contenido actual.
        entry_principal.insert(0, valor_seleccionado)  # Insertar el nuevo valor.

        # Cerrar la ventana secundaria.
        ventana_secundaria.destroy()

    # Crear un botón para seleccionar el dato.
    boton_seleccionar = ttk.Button(ventana_secundaria, text="Seleccionar", command=seleccionar_dato)
    boton_seleccionar.pack()


# Crear la ventana principal.
ventana_principal = tk.Tk()
entry_principal = tk.Entry()
entry_principal.pack()
abrir_ventana_secundaria()
print(entry_principal)
ventana_principal.mainloop()
