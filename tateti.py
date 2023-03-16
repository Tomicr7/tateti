from tkinter import *
import tkinter
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image,ImageTk
from functools import partial

import sqlite3


class Tateti:
    db_name = 'Tateti.db'
    def __init__(self):
        self.colores = {
            "Boca":["blue","gold"],
            "River":["red","white"]
                        }
        ventana = tkinter.Tk()
        ventana.title("tateti")
        tabla_botones = []
        img = Image.open("boca.png")
        img = img.resize((50,60), Image.Resampling.LANCZOS)
        self.imga = ImageTk.PhotoImage(img)
        img1 = Image.open("river.png")
        img1 = img1.resize((50, 60), Image.Resampling.LANCZOS)
        self.img1a = ImageTk.PhotoImage(img1)
        self.tabla_botones = []
        self.river = True
        self.boca = False
    
        for i in range(3):
            fila_botones = []    
            for j in range(3):
                b = tkinter.Button(ventana, command=partial(self.boton_apretado, i, j), height=4, width=5)
                b.grid(row=i, column=j)
                fila_botones.append(b)
            self.tabla_botones.append(fila_botones)
        print(self.tabla_botones)
        ventana.mainloop()
        
        
    def bloqueo(self):
        self.boton["state"] = tk.DISABLED 
    
    def boton_apretado(self, col, fila):
        
        if self.boca:
            imagen = self.imga
            texto = "Boca"
            self.turno = "Boca"
        else:
            imagen = self.img1a
            texto = "River"
            self.turno = "River"
        
        self.tabla_botones[col][fila].config(text=texto, image=imagen, command=partial(self.bloqueo), height=63, width=65)
        self.chequearGanador(self.tabla_botones)
        self.boca = not self.boca
    
    def chequearGanador(self, tabla_botones):
        titulo = ""
        if self.tabla_botones[0][0].cget("text") and self.tabla_botones[0][0].cget("text") == self.tabla_botones[0][1].cget("text") and self.tabla_botones[0][1].cget("text") == self.tabla_botones[0][2].cget("text"):
            #messagebox.showinfo(message="¡Gano " + self.turno + "!", title="ganador")
            titulo="¡Gano " + self.turno + "!"
        if self.tabla_botones[1][0].cget("text") and self.tabla_botones[1][0].cget("text") == self.tabla_botones[1][1].cget("text") and self.tabla_botones[1][1].cget("text") == self.tabla_botones[1][2].cget("text"):
            #messagebox.showinfo(message="!Gano " + self.turno + "!", title="ganador")
            titulo="¡Gano " + self.turno + "!"
        if self.tabla_botones[2][0].cget("text") and self.tabla_botones[2][0].cget("text") == self.tabla_botones[2][1].cget("text") and self.tabla_botones[2][1].cget("text") == self.tabla_botones[2][2].cget("text"):
            #messagebox.showinfo(message="¡Gano " + self.turno + "!", title="ganador")
            titulo="¡Gano " + self.turno + "!"
        if self.tabla_botones[0][0].cget("text") and self.tabla_botones[0][0].cget("text") == self.tabla_botones[1][0].cget("text") and self.tabla_botones[1][0].cget("text") == self.tabla_botones[2][0].cget("text"):
            #messagebox.showinfo(message="¡Gano " + self.turno + "!", title="ganador")
            titulo="¡Gano " + self.turno + "!"
        if self.tabla_botones[0][1].cget("text") and self.tabla_botones[0][1].cget("text") == self.tabla_botones[1][1].cget("text") and self.tabla_botones[1][1].cget("text") == self.tabla_botones[2][1].cget("text"):
            #messagebox.showinfo(message="¡Gano " + self.turno + "!", title="ganador")
            titulo="¡Gano " + self.turno + "!"
        if self.tabla_botones[0][2].cget("text") and self.tabla_botones[0][2].cget("text") == self.tabla_botones[1][2].cget("text") and self.tabla_botones[1][2].cget("text") == self.tabla_botones[2][2].cget("text"):
            #messagebox.showinfo(message="¡Gano " + self.turno + "!", title="ganador")
            titulo="¡Gano " + self.turno + "!"
        if self.tabla_botones[0][0].cget("text") and self.tabla_botones[0][0].cget("text") == self.tabla_botones[1][1].cget("text") and self.tabla_botones[1][1].cget("text") == self.tabla_botones[2][2].cget("text"):
            #messagebox.showinfo(message="¡Gano " + self.turno + "!", title="ganador")
            titulo="¡Gano " + self.turno + "!"
        if self.tabla_botones[0][2].cget("text") and self.tabla_botones[0][2].cget("text") == self.tabla_botones[1][1].cget("text") and self.tabla_botones[1][1].cget("text") == self.tabla_botones[2][0].cget("text"):
            #messagebox.showinfo(message="¡Gano " + self.turno + "!",  title="ganador")
            titulo="¡Gano " + self.turno + "!"
            
        if titulo:
            ventana2 = tkinter.Tk()
            ventana2.title(titulo)
            ventana2.geometry("244x150")
            ventana2.config(bg=self.colores[self.turno][0])
            
            
            Label(ventana2,text = 'NOMBRE: ', bg=self.colores[self.turno][1]).pack(padx=10,pady=0,fill=tk.X)
            self.nombre = Entry(ventana2,bg=self.colores[self.turno][1])
            self.nombre.pack()
            
        # Entrada de mi equipo


        # Boton de guardar 
            ttk.Button(ventana2,text = 'guardar', command = self.add_ganador).pack()
            
            
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
            
                
        query = 'SELECT * FROM GANADOR ORDER BY name DESC'
        db_rows = self.run_query(query)
        # datos de llenado
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[1])
     # Validación de entrada de usuario
    def validation(self):
        return len(self.nombre.get())
             
    def add_ganador(self):
        if self.validation():
            query = 'INSERT INTO GANADOR VALUES(NULL, ?, ?)'
            parameters =  (self.nombre.get(), self.turno)
            self.run_query(query, parameters)
            self.nombre.delete(0, END)
            
        
            
            
ttt = Tateti()

