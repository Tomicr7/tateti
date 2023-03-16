from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk

root = Tk()

def boton_apretado(self, col, fila):
        if self.boca:
            imagen = imga
            texto = "Boca"
            turno = "Boca"
        else:
            imagen = img1a
            texto = "River"
            turno = "River"

def bloqueo():
    boton["state"] = tk.DISABLED
    
boton = Button(root, text="click", command=bloqueo)
boton.pack()
    
root.mainloop()
