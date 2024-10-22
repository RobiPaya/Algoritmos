import tkinter as tk
from tkinter import ttk as tkk
from tkinter import *
import json as js
import datetime as dt
window=tk.Tk()
fechahoy=dt.datetime.now()
dia=fechahoy.day
mes=fechahoy.month
año=fechahoy.year
def opcion(seleccion):
    print(seleccion) #Esto es solo para saber que opción selecciona en el OptionMenu de las multas

def multar():
    def guardar():
        fecha=fechaentrada.get()
        nombre=nombreentrada.get()
        hora=horaentrada.get()
        matricula=matriculaentrada.get()
        multa=tipomultas.get()
        if multa=="No portar un faro delantero o posterior" or "Falta de llantas de refacción o herramientas para su cambio":
            cobro=651.42
        elif multa=="No usar el casco de protección para motociclistas y acompañantes":
            cobro=1302.84
        elif multa=="Ingerir bebidas alcohólicas mientras se conduce":
            cobro=977.13
        elif multa=="Manejar mientras la licencia o permiso está suspendido":
            cobro=10,965.57
        dialimite=dia+1
        if dialimite==31 and mes==4 or mes==6 or mes==9 or mes==11:
            dialimite=f"{1}/{mes+1}/{año}"
        elif dialimite==32:
            dialimite=f"{1}/{mes+1}/{año}"
            if mes==13:
                dialimite=f"{1}/{1}/{año}"
        elif dialimite==30 and mes==2 and año%4==0:
            dialimite=f"{1}/{mes+1}/{año}"
        elif dialimite==29 and mes==2:
            dialimite=f"{1}/{mes+1}/{año}"
        else:
            dialimite=f"{dia+1}/{mes}/{año}"
        datos=({matricula:{"Nombre":nombre,"Fecha":fecha,"Fechalimite":dialimite,"Hora":hora,"Tipo":multa,"Cobro":cobro}})
        
        try:
            with open("reporte.json","r") as archivo:
                data=js.load(archivo)
                data.update(datos)
            with open("reporte.json","w") as archivo:
                js.dump(data,archivo,indent=4)
        except:
            with open("reporte.json","w") as archivo:
                js.dump(datos,archivo,indent=4)
    window.destroy()
    windowmultar=tk.Tk()
    
    #Aqui empieza el OptionMenu
    tipomultas=tkk.Combobox(state="readonly",values=['No portar un faro delantero o posterior', 'Falta de llantas de refacción o herramientas para su cambio', 'No usar el casco de protección para motociclistas y acompañantes','Ingerir bebidas alcohólicas mientras se conduce','Manejar mientras la licencia o permiso está suspendido'])
    tipomultas.grid(column=0, row=0, columnspan=2)
    '''variable = StringVar()
    variable.set("Tipo de multas")
    choices = ['No portar un faro delantero o posterior', 'Falta de llantas de refacción o herramientas para su cambio', 'No usar el casco de protección para motociclistas y acompañantes','Ingerir bebidas alcohólicas mientras se conduce','Manejar mientras la licencia o permiso está suspendido']
    menu = OptionMenu(windowmultar, variable, * choices, command=opcion)
    menu.grid(column=0, row=0, columnspan=2)'''
    #Textos y entradas
    fechatexto=tk.Label(text="Fecha : ")
    fechatexto.grid(column=0, row=1)
    fechaentrada=tk.Entry(justify="right")
    fechaentrada.grid(column=1, row=1)    
    fechaentrada.insert(0,f"{dia}/{mes}/{año}")
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
    
    enviarboton=tk.Button(text="Enviar", width=25,command=guardar)
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