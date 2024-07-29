import customtkinter as ctk
from CTkTable import CTkTable



root = ctk.CTk()
values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
table = CTkTable(master=root, row=3, column=3, values=values)
table.pack(expand=True, fill="both", padx=20, pady=20)
def on_hover(event, row):
    row = event.widget.get_selected_row()
    print(f"Fila seleccionada: {row}")

# row=1
print(table.rows)
for row in range(table.rows):
    table.bind("<Enter>", on_hover, row+1)

root.mainloop()
