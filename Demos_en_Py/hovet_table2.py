import customtkinter as ctk
from CTkTable import CTkTable

def on_enter(event, row):
    for col in range(table.columns):
        widget = widgets[row][col]
        widget.configure(bg_color="lightblue")

def on_leave(event, row):
    for col in range(table.columns):
        widget = widgets[row][col]
        widget.configure(bg_color="white")

root = ctk.CTk()
values = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
table = CTkTable(master=root, row=3, column=5, values=values)
table.pack(expand=True, fill="both", padx=20, pady=20)

widgets = []
for row in range(table.rows):
    row_widgets = []
    for col in range(table.columns):
        print(f"{row} - {col}")
        widget = table.grid_slaves(row=row, column=col)[0]
        widget.bind("<Enter>", lambda event, r=row: on_enter(event, r))
        widget.bind("<Leave>", lambda event, r=row: on_leave(event, r))
        row_widgets.append(widget)
    widgets.append(row_widgets)

root.mainloop()
