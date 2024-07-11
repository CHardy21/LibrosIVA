import customtkinter as ctk

# Ventana principal
principal = ctk.CTk()
principal.title("Primera ventana")
principal.geometry("300x100")

# Cuarta ventana
ventana4 = ctk.CTkToplevel()
ventana4.title("Cuarta ventana")
ventana4.geometry("300x100")

# Tercera ventana
ventana3 = ctk.CTkToplevel()
ventana3.title("Tercera ventana")
ventana3.geometry("300x100")

# Segunda ventana
ventana2 = ctk.CTkToplevel()
ventana2.title("Segunda ventana")
ventana2.geometry("300x100")

principal.mainloop()