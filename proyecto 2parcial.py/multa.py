import tkinter as tk
from tkinter import *
window=tk.Tk()

def opcion(seleccion):
    print(seleccion) #Esto es solo para saber que opción selecciona en el OptionMenu de las multas

def multar():
    window.destroy()
    windowmultar=tk.Tk()
    
    #Aqui empieza el OptionMenu
    variable = StringVar()
    variable.set("Value")
    choices = ['Multa', 'Multa 2', 'Multa 3']
    menu = OptionMenu(windowmultar, variable, * choices, command=opcion)
    menu.grid(column=0, row=0, columnspan=2)
    
    #Textos y entradas
    fechatexto=tk.Label(text="Fecha : ")
    fechatexto.grid(column=0, row=1)
    fechaentrada=tk.Entry(justify="right")
    fechaentrada.grid(column=1, row=1)    
    
    nombretexto=tk.Label(text="Nombre : ")
    nombretexto.grid(column=0, row=2)
    nombreentrada=tk.Entry(justify="right")
    nombreentrada.grid(column=1, row=2)
    
    horatexto=tk.Label(text="Hora : ")
    horatexto.grid(column=0, row=3)
    horaentrada=tk.Entry(justify="right")
    horaentrada.grid(column=1, row=3)
    
    matriculatexto=tk.Label(text="Matrícula")
    matriculatexto.grid(column=0, row=4)
    matriculaentrada=tk.Entry(justify="right")
    matriculaentrada.grid(column=1, row=4)
    
    enviarboton=tk.Button(text="Enviar", width=25)
    enviarboton.grid(column=0, row=5, columnspan=2)
    
    windowmultar.mainloop()

#Ventana principal
bienvenidotexto=tk.Label(text="Bienvenido!")
bienvenidotexto.grid(column=0, row=0, columnspan=3)
multarboton=tk.Button(text="Multar", width=10, command=multar)
multarboton.grid(column=0, row=1)
reporteboton=tk.Button(text="Ver", width=10)
reporteboton.grid(column=2, row=1)

window.mainloop()