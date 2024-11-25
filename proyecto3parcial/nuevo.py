from socios import socios
from tkinter import Menu
import tkinter as tk
from tkinter import PhotoImage
from time import sleep
ola=socios.registrar(nombre=["fatima","negra","diego"],sexo=["m","f","m"],fechadenacimiento=[10,18,70],entrenador=["Fatima","DIEGO","Elvis"],estado=["activo","activo","activo"])

#Contador secreto uwu
contadorsecreto=0

#Ventana
ventana=tk.Tk()
ventana.title("Fornite gym")
ventana.minsize(width=400,height=500)
barrademenu=Menu

#Frames
frameventanaprincipal=tk.Frame()
frameventanaprincipal.grid(column=0, row=0)
framesocios=tk.Frame()
frameconsultar=tk.Frame()
framesecreto=tk.Frame()

def verventanaprincipal():
    global contadorsecreto
    contadorsecreto=0
    framesecreto.grid_forget()
    frameconsultar.grid_forget()
    framesocios.grid_forget()
    frameconsultar.grid_forget()
    frameventanaprincipal.grid(column=0, row=1)

def consultar():
    frameconsultar.grid(column=0, row=0)
    framesocios.grid_forget()
    tk.Label(frameconsultar, text="ID : ").grid(column=0, row=0)
    Idconsultada=tk.Entry(frameconsultar).grid(column=1, row=0)
    tk.Button(frameconsultar, text="Volver", command=sociosboton).grid(column=0, row=1)

#Menú
barra_menu = Menu(ventana) 
menu_archivo = Menu(barra_menu, tearoff=1) 
barra_menu.add_checkbutton(label="Inicio", command=verventanaprincipal)
barra_menu.add_checkbutton(label="Socios")
barra_menu.add_checkbutton(label="Asistencias")
barra_menu.add_checkbutton(label="Reporte")
barra_menu.add_checkbutton(label="Salir", command=quit)
ventana.config(menu=barra_menu)

def sociosboton():
    frameconsultar.grid_forget()
    framesocios.grid(column=0, row=0)
    frameventanaprincipal.grid_forget()
    tk.Button(framesocios, text="Consultar", command=consultar).grid(column=0, row=0)
    tk.Button(framesocios, text="Registrar").grid(column=0, row=1)
    tk.Button(framesocios, text="Volver", command=verventanaprincipal).grid(column=0, row=2)

def secretouwu():
    global contadorsecreto
    contadorsecreto+=1
    if contadorsecreto==13:
        frameventanaprincipal.grid_forget()
        framesecreto.grid(column=0, row=0)
        tk.Button(framesecreto, text="No clic", command=porfatequierover).grid(column=0, row=0, padx=100, pady=100)

def porfatequierover():
    imagensecreta=tk.PhotoImage(file="socios.png")
    verimagensecreta=tk.Label(framesecreto, image=imagensecreta)
    verimagensecreta.grid(column=0, row=0)

#Pantalla principal
#¯\_(ツ)_/¯
logo = PhotoImage(file="Logo.png")
tk.Button(frameventanaprincipal, image=logo, command=secretouwu).grid(column=0, row=0, columnspan=2, padx=200)
#🐱‍👓
asistenciasimagen=PhotoImage(file="asistencias.png")
tk.Button(frameventanaprincipal, image=asistenciasimagen).grid(column=0, row=1)
#Botón e imagén de socios
sociosimagen=PhotoImage(file="socios.png")
tk.Button(frameventanaprincipal, image=sociosimagen, command=sociosboton).grid(column=1, row=1)
#Imagén y botón de ganancias
gananciasimagen=PhotoImage(file="ganancias.png")
tk.Button(frameventanaprincipal, image=gananciasimagen).grid(column=1, row=2)
#🤣
entrenadoresimagen=PhotoImage(file="entrenador.png")
tk.Button(frameventanaprincipal, image=entrenadoresimagen).grid(column=0, row=2)


ventana.mainloop()