import customtkinter as ctk
from CTkTable import CTkTable



root = ctk.CTk()
values = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
table = CTkTable(master=root, row=3, column=5, values=values)
def on_hover(event):
    # row = table.get(event.widget.row, 0)
    print(f"Fila seleccionada: {event}")

for row in range(3):
    table.edit_row(row, hover=True)
    print(row)
    table.bind("<Enter>", on_hover)

table.pack(expand=True, fill="both", padx=20, pady=20)
root.mainloop()
