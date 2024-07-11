from tkinter import StringVar
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# Apariencia temporal, luego al finalizar quitar esta linea
ctk.set_appearance_mode("dark")

class invoiceShow:
    app3 = ctk.CTkToplevel()
    app3.title('Comprobantes')
    #app3.grab_set()

    # create a list box
    langs = ('Java', 'C#', 'C', 'C++', 'Python',
             'Go', 'JavaScript', 'PHP', 'Swift')

    var = tk.Variable(value=langs)

    listbox = tk.Listbox(
        app3,
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

    #app3.mainloop()

#invoiceShow()