from tkinter import *

frame = Tk()
# Elimina la sombra y arrastra la barra.
# Nota: Debe usarse antes de las llamadas wm, de lo contrario, se eliminarán.
frame.overrideredirect(True)

frame.call("wm", "attributes", ".", "-topmost", "true")  # Mantenga siempre la ventana encima de los demás
frame.geometry("300x300+500+250")  # Establezca el desplazamiento desde la esquina superior izquierda de la pantalla,
# así como el tamaño
# frame.call("wm", "attributes", ".", "-transparent", "true")  # Remove shadow from window
# frame.call("wm", "attributes", ".", "-fullscreen", "true")  # Fullscreen mode
# frame.call("wm", "attributes", ".", "-alpha", "0.9")  # Window Opacity 0.0-1.0
# frame.call("wm", "attributes", ".", "-modified", "0.9")  # Toggles modified state of the close-window icon.

frame.mainloop()
