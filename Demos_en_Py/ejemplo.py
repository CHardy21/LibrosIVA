import customtkinter as ctk

class MiVentana:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("400x150")

    def dataForm(self):
        # Crear Entry y botón
        self.mi_entry = ctk.CTkEntry(self.app)
        self.mi_boton = ctk.CTkButton(self.app, text="Cambiar valor", command=self.cambiar_valor)

        self.mi_entry.pack(padx=20, pady=20)
        self.mi_boton.pack()

    def cambiar_valor(self):
        nuevo_valor = "Nuevo valor"  # Puedes obtener este valor de donde desees
        self.mi_entry.delete(0, 'end')
        self.mi_entry.insert(0, nuevo_valor)

    def iniciar_aplicacion(self):
        self.app.mainloop()

if __name__ == "__main__":
    ventana = MiVentana()
    ventana.dataForm()
    ventana.iniciar_aplicacion()
