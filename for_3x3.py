import tkinter as tk

def tunavez():
    boton["state"] = tk.DISABLED
    

boton = tk.Button(text="¡Hola, mundo!", command=tunavez)
boton.place(x=50, y=50)
