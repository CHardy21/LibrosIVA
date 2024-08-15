import tkinter as tk


class MyDialog:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.parent = parent
        self.top.title("Salir")

        tk.Label(self.top, text="¿Está seguro?").grid(row=0, column=0, columnspan=2)

        self.button1 = tk.Button(self.top, text="Si, salir de la app.", command=self.salir)
        self.button2 = tk.Button(self.top, text="No, solo minimizar.", command=self.minimizar)
        self.button1.grid(row=1, column=0, padx=5, pady=5)
        self.button2.grid(row=1, column=1, padx=5, pady=5)

    def salir(self):
        self.top.destroy()
        self.parent.destroy()

    def minimizar(self):
        self.top.destroy()
        self.parent.iconify()


class MyApp:
    def __init__(self, parent):
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        d = MyDialog(root)
        self.parent.wait_window(d.top)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

# https://es.stackoverflow.com/questions/104691/c%c3%b3mo-manejar-el-evento-de-cerrar-ventana-en-tkinter
#  https://es.stackoverflow.com/questions/474859/c%c3%b3mo-iniciar-la-ventana-ra%c3%adz-como-cuadro-de-di%c3%a1logo-o-solo-con-el-bot%c3%b3n-cerrar