import customtkinter as ctk
from CTkTable import *

def on_hover(event, table, row):
    print(event, "--",row)
    # for col in range(table.columns):
    #     print(row)
    #     table.edit_column(row, bg_color="red")
    # row1 = table.get_row(row)
    # print(f"Fila seleccionada: {row1}")

def on_leave(event, table, row):
    for col in range(table.columns):
        table.edit_row(row, bg_color="white")

root = ctk.CTk()
values = [[1, 2, 3, 4, 5], [11, 12, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35], [1, 2, 3, 4, 5]]
table = CTkTable(master=root, row=5, column=5, values=values)
table.pack(expand=True, fill="both", padx=20, pady=20)

for row in range(table.rows):
    print("->", row)

    table.bind("<Enter>", lambda event, r=row: on_hover(event, table, row))
    # table.bind("<Leave>", lambda event, r=row: on_leave(event, table, r))

root.mainloop()
