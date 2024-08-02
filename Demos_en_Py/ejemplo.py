import tkinter as tk

def cerrar_ventana():
    root.destroy()

root = tk.Tk()
root.title("Ventana Principal")

boton_cerrar = tk.Button(root, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack(pady=20)

root.mainloop()
