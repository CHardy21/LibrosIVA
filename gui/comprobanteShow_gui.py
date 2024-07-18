from tkinter import StringVar
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# Apariencia temporal, luego al finalizar quitar esta linea
ctk.set_appearance_mode("dark")

class InvoiceForm(ctk.CTk):
    def __init__(self):
        super().__init__()
        app2 = ctk.CTkToplevel()
        app2.grab_set()

        app2.title('Comprobantes')

        # create a list box
        langs = ('Java', 'C#', 'C', 'C++', 'Python',
                 'Go', 'JavaScript', 'PHP', 'Swift')

        var = tk.Variable(value=langs)

        listbox = tk.Listbox(
            app2,
            listvariable=var,
            height=6,
            selectmode=tk.EXTENDED
        )

        listbox.pack(expand=True, fill=tk.BOTH)


        def items_selected(event):
            # get all selected indices
            selected_indices = listbox.curselection()
            # get selected items
            selected_langs = ",".join([listbox.get(i) for i in selected_indices])
            msg = f'You selected: {selected_langs}'
            #showinfo(title='Information', message=msg)


        listbox.bind('<<ListboxSelect>>', items_selected)

if __name__ == '__main__':
    ventana = InvoiceForm()
    ventana.mainloop()