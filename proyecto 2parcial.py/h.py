import tkinter as tk
from tkinter import ttk as ttk
from tkinter import *

window=tk.Tk()
window.resizable(0,0)

def reporte():
    frame.grid_forget()
    frame3.grid(column=0, row=0)
    filtro=ttk.Combobox(frame3, state="readonly", values=["Día","Semana","Mes","Año"])
    filtro.grid(column=0, row=6)
    eleccion=filtro.get()
    print(eleccion)
    tk.Button(frame3, text="Volver", command=verdenuevo).grid(column=0, row=2)

def multar():
    frame.grid_forget()
    frame2.grid(column=0, row=0)
    
    #Aqui empieza el OptionMenu
    variable = StringVar()
    variable.set("Value")
    choices = ['Multa', 'Multa 2', 'Multa 3']
    OptionMenu(frame2, variable, * choices).grid(column=0, row=0, columnspan=2)
    
    #Textos y entradas
    tk.Label(frame2,text="Fecha : ").grid(column=0, row=1) #Texto de fecha
    fechaentrada=tk.Entry(frame2,justify="right")
    fechaentrada.grid(column=1, row=1)
    
    tk.Label(frame2, text="Nombre : ").grid(column=0, row=2) #Texto de nombre
    nombreentrada=tk.Entry(frame2, justify="right")
    nombreentrada.grid(column=1, row=2)
    
    tk.Label(frame2, text="Hora : ").grid(column=0, row=3) #Texto de hora
    horaentrada=tk.Entry(frame2, justify="right")
    horaentrada.grid(column=1, row=3)
    
    tk.Label(frame2, text="Matrícula : ").grid(column=0, row=4) #Texto de matrícula
    matriculaentrada=tk.Entry(frame2, justify="right")
    matriculaentrada.grid(column=1, row=4)
    
    tk.Label(frame2, text="Sexo : ").grid(column=0, row=5) #Texto de sexo
    tiposexo=ttk.Combobox(frame2, width=17, state="readonly", values=["Hombre","Mujer","Otre"])
    tiposexo.grid(column=1, row=5)
    
    #Botones
    tk.Button(frame2, text="Enviar", width=25).grid(column=0, row=6, columnspan=2) #Botón para enviar
    tk.Button(frame2, text="Volver", width=25, command=verdenuevo).grid(column=0, row=7, columnspan=2) #Botón para volver

#verdenuevo para volver
def verdenuevo():
    frame2.grid_forget()
    frame3.grid_forget()
    frame.grid(column=1, row=1)

#Cosas para sacar los frames 
frame3=tk.Frame()
frame3.columnconfigure(0, weight=1)
frame3.grid(column=0, row=0)
frame2=tk.Frame()
frame2.columnconfigure(0, weight=1)
frame2.grid(column=0, row=0)

#Ventana principal
frame=tk.Frame(window)
frame.columnconfigure(0, weight=1)
frame.grid(column=0, row=0)

tk.Label(frame ,text="Bienvenido!").grid(column=0, row=0, columnspan=3)
tk.Button(frame, text="Multar", width=10, command=multar).grid(column=0, row=1)
tk.Button(frame, text="Ver", width=10, command=reporte).grid(column=2, row=1)

window.columnconfigure(0, weight=4)
window.columnconfigure(1, weight=1)

window.attributes("-toolwindow", True)
window.mainloop()