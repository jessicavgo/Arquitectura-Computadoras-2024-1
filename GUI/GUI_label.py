# Importamos módulo de tkinter, lo llamaremos tk dentro del código
import tkinter as tk

# crearemos una ventana principal, la llamaremos window
# dentro de tkinter, (tk) está el método Tk que permite crear esta ventana

window = tk.Tk()

# Añadimos un primer widget (label, es una etiqueta que puede llevar texto o imagen)
greeting = tk.Label(text="Soy un label widget!")

# leemos imagen
logo = tk.PhotoImage(file="pythonlogo.png")
# ponemos la imagen en la etiqueta
w1 = tk.Label(window, image=logo)
w1.pack()

# etiqueta con colores personalizados
label = tk.Label(
    text="Soy una etiqueta!",
    foreground="yellow",
    background="#555555",  # color puede escribirse en RGB, como hexadecimal
    width=15,
    height=15  # la unidad es el ancho y alto del caracter 0
)
label.pack()
# lista de colores disponibles
# http://dominiquethiebaut.com/dftwiki3/images/3/3d/TkInterColorCharts.png


greeting.pack()

# Al final del código añadimos mainloop, asi nuestra GUI estará esperando acción del usuario
# esta espera es un ciclo llamado "event loop", también bloqueará python para ejecutar otro codigo
# hasta que se cierre esta ventana
window.mainloop()

# listado de widgets
# https://www.tutorialspoint.com/python/python_gui_programming.htm
