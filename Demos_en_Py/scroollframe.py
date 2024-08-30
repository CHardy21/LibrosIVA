import customtkinter as ctk
from CTkTable import CTkTable

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=400, height=300)
        self.scrollable_frame.pack(expand=True, fill="both", padx=20, pady=20)

        self.valores = [
            [1, 2, 3],
            [4, 5, 6],
            [1, 2, 3],
            [4, 5, 6],
            [1, 2, 3],
            [4, 5, 6],
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        self.tabla = CTkTable(master=self.scrollable_frame, values=self.valores)
        self.tabla.pack(expand=True, fill="both", padx=20, pady=20)

        self.scrollable_frame._parent_canvas.bind("<Configure>", self.check_scroll_position)
        self.scrollable_frame._parent_canvas.bind("<MouseWheel>", self.on_mouse_wheel)

        self.loading = False

    def check_scroll_position(self, event=None):
        if not self.loading and self.scrollable_frame._parent_canvas.yview()[1] == 1.0:
            self.loading = True
            self.cargar_mas_datos()

    def on_mouse_wheel(self, event):
        if self.loading:
            return "break"

    def cargar_mas_datos(self):
        # Simula la carga de más datos
        nuevos_datos = [
            [10, 11, 12],
            [13, 14, 15],
            [16, 17, 18],
            [10, 11, 12],
            [13, 14, 15],
            [10, 11, 12],
            [13, 14, 15],            [10, 11, 12],
            [13, 14, 15],            [10, 11, 12],
            [13, 14, 15],            [10, 11, 12],
            [13, 14, 15],            [10, 11, 12],
            [13, 14, 15],            [10, 11, 12],
            [13, 14, 15],            [10, 11, 12],
            [13, 14, 15],            [10, 11, 12],
            [13, 14, 15],            [10, 11, 12],
            [13, 14, 15],
        ]
        for fila in nuevos_datos:
            self.tabla.add_row(values=fila)

        # Mueve el scrollbar hacia arriba para evitar más cargas inmediatas
        self.scrollable_frame._parent_canvas.yview_moveto(0.8)
        self.loading = False

app = App()
app.mainloop()
