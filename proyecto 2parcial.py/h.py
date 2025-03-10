import tkinter as tk
import json as js
from tkinter import messagebox
from tkinter import ttk as ttk
from tkinter import *
import datetime as dt

window=tk.Tk()
window.resizable(0,0)
fechahoy=dt.datetime.now()
dia=str(fechahoy.day)
mes=str(fechahoy.month)
año=str(fechahoy.year)
horacutual=fechahoy.hour
minutos=fechahoy.minute
def reporte():
    def ver():
        cont=0
        cobrototal=0
        diasemanames=filtro.get()
        try:
            with open("reporte.json","r") as archivo:
                data=js.load(archivo)
                if diasemanames=="Día":
                    for x in data:
                        fecha=str(data[x]["Fecha"])
                        fecha=fecha.replace("/"," ")
                        fecha=fecha.split()
                        if fecha[0]==dia:
                            cont+=1
                            cobrototal+=data[x]["Cobro"]*1/2
                    respuesta.config(text=f"El total de multas en el dia fueron {cont}\nEl total de cobro fue de ${cobrototal:.2f}")
                elif diasemanames=="Semana":
                    cobrototal=0
                    cont=0
                    diaextra=dt.timedelta(days=0)
                    fechabien=dt.datetime(int(año),int(mes),int(dia))
                    if fechabien.strftime("%A")=="Monday":
                        diaextra=dt.timedelta(days=1)
                    elif fechabien.strftime("%A")=="Tuesday":
                        diaextra=dt.timedelta(days=2)
                    elif fechabien.strftime("%A")=="Wednesday":
                        diaextra=dt.timedelta(days=3)
                    elif fechabien.strftime("%A")=="Thursday":
                        diaextra=dt.timedelta(days=4)
                    elif fechabien.strftime("%A")=="Friday":
                        diaextra=dt.timedelta(days=5)
                    elif fechabien.strftime("%A")=="Saturday":
                        diaextra=dt.timedelta(days=6)
                    diainicio=fechabien-diaextra
                    diafinal=diainicio+dt.timedelta(days=6)
                    for x in data:
                        fecha=str(data[x]["Fecha"])
                        fecha=fecha.replace("/"," ")
                        fecha=fecha.split()
                        fechacomparar=dt.datetime(int(fecha[2]),int(fecha[1]),int(fecha[0]))
                        if fechacomparar>=diainicio and fechacomparar<=diafinal:
                            cont+=1
                            if int(fecha[0])<int(dia):
                                cobrototal+=data[x]["Cobro"]
                            elif int(fecha[0])==int(dia)-1:
                                if int(hora[0])>horacutual:
                                    cobrototal+=data[x]["Cobro"]
                                elif int(hora[0])==horacutual:
                                    if int(hora[1])>=minutos:
                                        cobrototal+=data[x]["Cobro"]
                                    else:
                                        cobrototal+=data[x]["Cobro"]*1/2
                            else:
                                cobrototal+=data[x]["Cobro"]*1/2
                    respuesta.config(text=f"El total de multas en el dia fueron {cont}\nEl total de cobro fue de ${cobrototal:.2f}")
                elif diasemanames=="Mes":
                    cobrototal=0
                    cont=0
                    for x in data:
                        fecha=str(data[x]["Fecha"])
                        hora=str(data[x]["Hora"])
                        hora=hora.replace(":"," ")
                        hora=hora.split()
                        fecha=fecha.replace("/"," ")
                        fecha=fecha.split()
                        if fecha[1]==mes:
                            cont+=1
                            if int(fecha[0])<int(dia):
                                cobrototal+=data[x]["Cobro"]
                            elif int(fecha[0])==int(dia)-1:
                                if int(hora[0])>horacutual:
                                    cobrototal+=data[x]["Cobro"]
                                elif int(hora[0])==horacutual:
                                    if int(hora[1])>=minutos:
                                        cobrototal+=data[x]["Cobro"]
                                    else:
                                        cobrototal+=data[x]["Cobro"]*1/2
                            else:
                                cobrototal+=data[x]["Cobro"]*1/2
                    respuesta.config(text=f"El total de multas en el dia fueron {cont}\nEl total de cobro fue de ${cobrototal:.2f}")
        except:
            messagebox.showinfo(title="No hay",message="NO HAY ARCHIVO DE MULTAS")
    frame.grid_forget()
    frame3.grid(column=0, row=0)
    filtro=ttk.Combobox(frame3, state="readonly", values=["Día","Semana","Mes"])
    filtro.grid(column=0, row=0)
    tk.Button(frame3, text="ver",command=ver).grid(column=0,row=2)
    eleccion=filtro.get()
    print(eleccion)
    tk.Button(frame3, text="Volver", command=verdenuevo).grid(column=0, row=3)
    respuesta=tk.Label(frame3,text="")
    respuesta.grid(column=0,row=1)


def multar():
    def enviar():
        ok=messagebox.askokcancel(title="Seguro?", message="Quieres enviar los datos?")
        if ok:
            fecha=fechaentrada.get()
            fecha1=fecha.replace("/"," ")
            fecha1=fecha1.split()
            nombre=nombreentrada.get()
            hora=horaentrada.get()
            matricula=matriculaentrada.get()
            multa=tipomultas.get()
            sexo=tiposexo.get()
            if multa=="No portar un faro delantero o posterior" or "Falta de llantas de refacción o herramientas para su cambio":
                    cobro=651.42
            elif multa=="No usar el casco de protección para motociclistas y acompañantes":
                cobro=1302.84
            elif multa=="Ingerir bebidas alcohólicas mientras se conduce":
                cobro=977.13
            elif multa=="Manejar mientras la licencia o permiso está suspendido":
                cobro=10,965.57
            fechapras=dt.datetime(int(fecha1[2]),int(fecha1[1]),int(fecha1[0]))
            dialimiteendatetime=fechapras+dt.timedelta(days=1)
            dialimite=f"{dialimiteendatetime.day}/{dialimiteendatetime.month}/{dialimiteendatetime.day}"
            datos=({matricula:{"Nombre":nombre,"Sexo":sexo,"Fecha":fecha,"Fechalimite":dialimite,"Hora":hora,"Tipo":multa,"Cobro":cobro}})
            try:
                with open("reporte.json","r") as archivo:
                    data=js.load(archivo)
                    data.update(datos)
                with open("reporte.json","w") as archivo:
                    js.dump(data,archivo,indent=4)
            except:
                with open("reporte.json","w") as archivo: 
                    js.dump(datos,archivo,indent=4)
            ttk.Button(frame2, command=multar())
    frame.grid_forget()
    frame2.grid(column=0, row=0)
    
    #Textos y entradas
    tk.Label(frame2,text="Fecha : ").grid(column=0, row=1) #Texto de fecha
    fechaentrada=tk.Entry(frame2,justify="right")
    fechaentrada.grid(column=1, row=1)
    fechaentrada.insert(0,f"{dia}/{mes}/{año}")
    
    tk.Label(frame2, text="Nombre : ").grid(column=0, row=2) #Texto de nombre
    nombreentrada=tk.Entry(frame2, justify="right")
    nombreentrada.grid(column=1, row=2)
    
    tk.Label(frame2, text="Hora : ").grid(column=0, row=3) #Texto de hora
    horaentrada=tk.Entry(frame2, justify="right")
    horaentrada.grid(column=1, row=3)
    
    tk.Label(frame2, text="Matrícula : ").grid(column=0, row=4) #Texto de matrícula
    matriculaentrada=tk.Entry(frame2, justify="right")
    matriculaentrada.grid(column=1, row=4)
    
    tk.Label(frame2, text="Sexo : ").grid(column=0, row=6) #Texto de sexo
    tiposexo=ttk.Combobox(frame2, width=17, state="readonly", values=["Hombre","Mujer","Otre"])
    tiposexo.grid(column=1, row=6)
    
    #Aqui empieza el OptionMenu
    tk.Label(frame2, text="Tipo de multa : ").grid(column=0, row=0)
    tipomultas=ttk.Combobox(frame2, width=17,state="readonly",values=['No portar un faro delantero o posterior', 'Falta de llantas de refacción o herramientas para su cambio', 'No usar el casco de protección para motociclistas y acompañantes','Ingerir bebidas alcohólicas mientras se conduce','Manejar mientras la licencia o permiso está suspendido'])
    tipomultas.grid(column=1, row=0)

    #Botones
    tk.Button(frame2, text="Enviar", width=25, command=enviar).grid(column=0, row=100, columnspan=2) #Botón para enviar
    tk.Button(frame2, text="Volver", width=25, command=verdenuevo).grid(column=0, row=101, columnspan=2) #Botón para volver
    

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