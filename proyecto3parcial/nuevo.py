from socios import socios
from tkinter import Menu
import tkinter as tk
from tkinter import PhotoImage
ola=socios.registrar(nombre=["fatima","negra","diego"],sexo=["m","f","m"],edad=[10,18,70],entrenador=["Fatima","DIEGO","Elvis"],estado=["activo","activo","activo"])
ventana=tk.Tk()
ventana.title("Fornite gym")
ventana.minsize(width=400,height=500)
barrademenu=Menu

barra_menu = Menu(ventana) 
menu_archivo = Menu(barra_menu, tearoff=1) 
barra_menu.add_checkbutton(label="Socios")
barra_menu.add_checkbutton(label="Asistencias")
barra_menu.add_checkbutton(label="Reporte")
barra_menu.add_checkbutton(label="Salir", command=quit)
ventana.config(menu=barra_menu)

imagen = PhotoImage(file="Logo.png")


ventana.mainloop()