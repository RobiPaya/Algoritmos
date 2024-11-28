from socios import socios
from tkinter import Menu
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkcalendar import DateEntry
from fortnite import sociose
from entrenadores import entrenadores
import pandas as pd
import random

#Contador secreto uwu
contadorsecreto=0
otrocontadornosecreto=0

#Ventana
ventana=tk.Tk()
ventana.title("Inicio")
ventana.minsize(width=400,height=500)
barrademenu=Menu

#Frames
frame_ventana_principal=tk.Frame()
frame_ventana_principal.grid(column=0, row=0)
frame_socios=tk.Frame()
frame_consultar=tk.Frame()
frame_registrar=tk.Frame()
frame_entrenadores=tk.Frame()
frame_asistencias=tk.Frame()
frame_ganancias=tk.Frame()

#Cosa pa ver la ventana principal otra vez
def verventanaprincipal():
    ventana.title("Inicio")
    frame_entrenadores.grid_forget()
    frame_asistencias.grid_forget()
    frame_ganancias.grid_forget()
    frame_socios.grid_forget()
    frame_consultar.grid_forget()
    frame_registrar.grid_forget()
    frame_ventana_principal.grid(column=0, row=1)

#Menú
barra_menu = Menu(ventana) 
menu_archivo = Menu(barra_menu, tearoff=1) 
barra_menu.add_checkbutton(label="Inicio", command=verventanaprincipal)
barra_menu.add_checkbutton(label="Socios")
barra_menu.add_checkbutton(label="Asistencias")
barra_menu.add_checkbutton(label="Reporte")
barra_menu.add_checkbutton(label="Salir", command=quit)
ventana.config(menu=barra_menu)

#Todo lo de socios
def socios_boton():
    ventana.title("Socios")
    frame_registrar.grid_forget()
    frame_consultar.grid_forget()
    frame_socios.grid(column=0, row=0)
    frame_ventana_principal.grid_forget()
    tk.Button(frame_socios, text="Consultar", command=socios_consultar).grid(column=0, row=0)
    tk.Button(frame_socios, text="Registrar", command=socios_registar).grid(column=0, row=1)
    tk.Button(frame_socios, text="Volver", command=verventanaprincipal).grid(column=0, row=2)
def socios_consultar():
    frame_no_existe=tk.Frame()
    otrocontadornosecreto=0
    def destruir_framex_y_mostrar_socios():
        return [socios_boton(), frame_no_existe.destroy()]
    def extraerdatos(event):
        def probar_consulta():
            def destruir_framehola_y_mostrar_socios(): #Doble funcion solo para destruir
                return [socios_consultar(), frame_datos_socios.destroy()]
            global otrocontadornosecreto
            def editar_socios():
                    def editar2():
                        socios.editar(int(idconsultada.get()),int(idconsultada.get()),nombre_editado.get())
                    nombre_editado=tk.Entry(frame_datos_socios)
                    nombre_editado.grid(column=1, row=0)
                    nombre_editado.insert(0, datos["nombre"])
                    tk.Button(frame_datos_socios,text="Listo", command=editar2).grid(column=1, row=5)
            try:
                frame_no_existe.grid_forget()
                frame_consultar.grid_forget()
                ventana.title("Socio consultado")
                datos=socios.consultar(int(idconsultada.get()))
                frame_datos_socios=tk.Frame()
                frame_datos_socios.grid(column=0, row=0)
                tk.Label(frame_datos_socios, text="Nombre : ").grid(column=0, row=0)
                tk.Label(frame_datos_socios, text="Sexo : ").grid(column=0, row=1)
                tk.Label(frame_datos_socios, text="Fecha de nacimiento : ").grid(column=0, row=2)
                tk.Label(frame_datos_socios, text="Entrenador : ").grid(column=0, row=3)
                tk.Label(frame_datos_socios, text="Estado : ").grid(column=0, row=4)
                tk.Label(frame_datos_socios, text=datos["nombre"]).grid(column=1, row=0)
                tk.Label(frame_datos_socios, text=datos["sexo"]).grid(column=1, row=1)
                tk.Label(frame_datos_socios, text=datos["fecha_de_nacimiento"]).grid(column=1, row=2)
                tk.Label(frame_datos_socios, text=datos["entrenador"]).grid(column=1, row=3)
                tk.Label(frame_datos_socios, text=datos["estado"]).grid(column=1, row=4)
                tk.Button(frame_datos_socios, text="Editar", command=editar_socios).grid(column=1,row=5)
                tk.Button(frame_datos_socios, text="Volver", command=destruir_framehola_y_mostrar_socios).grid(column=0, row=5)
            except:
                frame_no_existe.grid(column=0,row=1)
                tk.Label(frame_no_existe, text="No existe").grid(column=1, row=otrocontadornosecreto+1)
                otrocontadornosecreto+=1
        probar_consulta() #Esto es solo pa que se corra
    ventana.title("Socios consultar")
    frame_socios.grid_forget()
    frame_consultar.grid(column=0, row=0)
    tk.Label(frame_consultar, text="ID : ").grid(column=0, row=0)
    idconsultada=tk.Entry(frame_consultar)
    idconsultada.grid(column=1, row=0)
    idconsultada.bind("<Return>", extraerdatos)
    tk.Button(frame_consultar, text="Volver", command=destruir_framex_y_mostrar_socios).grid(column=0, row=otrocontadornosecreto+2)
def socios_registar():
    ventana.title("Socios registrar")
    def registrar_socios():
        nombre_geteado=nombre.get()
        sexo_getado=sexo.get()
        fechadenacimiento_geteado=fechadenacimiento.get_date().strftime('%d-%m-%Y')
        entrenador=""
        estado="Activo"
        if not nombre_geteado or not sexo_getado or not fechadenacimiento_geteado:
            messagebox.showerror("Error", "Faltan datos")
        else:
            sociose.registrar(nombre_geteado,sexo_getado,fechadenacimiento_geteado,entrenador,estado)

    frame_consultar.grid_forget()
    frame_socios.grid_forget()
    frame_registrar.grid(column=0, row=0)
    tk.Label(frame_registrar, text="Nombre : ").grid(column=0, row=0)
    nombre=tk.Entry(frame_registrar)
    nombre.grid(column=1, row=0)
    tk.Label(frame_registrar, text="Sexo : ").grid(column=0, row=1)
    sexo=tk.Entry(frame_registrar)
    sexo.grid(column=1, row=1)
    tk.Label(frame_registrar, text="Fecha de nacimiento : ").grid(column=0, row=2)
    fechadenacimiento=DateEntry(frame_registrar, width=17, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd-mm-yyyy')
    fechadenacimiento.grid(column=1, row=2)
    tk.Button(frame_registrar, text="Registrar", command=registrar_socios).grid(column=1, row=4)
    tk.Button(frame_registrar, text="Volver", command=socios_boton).grid(column=0, row=4)

#Esto es secreto, no ver
def secretouwu():
    global contadorsecreto
    contadorsecreto+=1
    numerorando=random.randint(1,100)
    if contadorsecreto==numerorando:
        ventana.destroy()
        ventanasecreta=tk.Tk()
        ventanasecreta.title("UwU")
        imagensecreta=tk.PhotoImage(file="No abrirb.png")
        tk.Label(image=imagensecreta).grid(column=0, row=0)
        ventanasecreta.mainloop()

#Todo lo del botón de entrenadores
def entrenadores_boton():
    ventana.title("Entrenadores")
    frame_ventana_principal.grid_forget()
    frame_consultar.grid_forget()
    frame_registrar.grid_forget()
    frame_entrenadores.grid(column=0, row=0)
    tk.Button(frame_entrenadores, text="Consultar", command=entrenadores_consultar).grid(column=0, row=0)
    tk.Button(frame_entrenadores, text="Registrar", command=entrenadores_registar).grid(column=0, row=1)
    tk.Button(frame_entrenadores, text="Volver", command=verventanaprincipal).grid(column=0, row=2) 
def entrenadores_registar():
    ventana.title("Entrenadores registrar")
    frame_entrenadores.grid_forget()
    def registrar_entrenadores():
        nombre_geteado=nombre.get()
        sexo_getado=sexo.get()
        fechadenacimiento_geteado=fechadenacimiento.get_date().strftime('%d-%m-%Y')
        estado="Activo"
        if not nombre_geteado or not sexo_getado or not fechadenacimiento_geteado:
            messagebox.showerror("Error", "Faltan datos")
        else:
            entrenadores.registrar(nombre_geteado,sexo_getado,fechadenacimiento_geteado,estado)
    frame_consultar.grid_forget()
    frame_socios.grid_forget()
    frame_registrar.grid(column=0, row=0)
    tk.Label(frame_registrar, text="Nombre : ").grid(column=0, row=0)
    nombre=tk.Entry(frame_registrar)
    nombre.grid(column=1, row=0)
    tk.Label(frame_registrar, text="Sexo : ").grid(column=0, row=1)
    sexo=tk.Entry(frame_registrar)
    sexo.grid(column=1, row=1)
    tk.Label(frame_registrar, text="Fecha de nacimiento : ").grid(column=0, row=2)
    fechadenacimiento=DateEntry(frame_registrar, width=17, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd-mm-yyyy')
    fechadenacimiento.grid(column=1, row=2)
    tk.Button(frame_registrar, text="Registrar", command=registrar_entrenadores).grid(column=1, row=4)
    tk.Button(frame_registrar, text="Volver", command=entrenadores_boton).grid(column=0, row=4)
def entrenadores_consultar():
    frame_entrenadores.grid_forget()
    frame_no_existe=tk.Frame()
    otrocontadornosecreto=0
    def destruir_framex_y_mostrar_entrenadores():
        return [entrenadores_boton(), frame_no_existe.destroy()]
    def extraerdatos(event):
        def probar_consulta():
            def destruir_framehola_y_mostrar_entrenadores(): #Doble funcion solo para destruir
                return [entrenadores_consultar(), frame_datos_entrenadores.destroy()]
            global otrocontadornosecreto
            def editar_entrenadores():
                a=tk.Entry(frame_datos_entrenadores).grid(column=1, row=0)
            try:
                frame_no_existe.grid_forget()
                frame_consultar.grid_forget()
                ventana.title("Entrenador consultado")
                datos=entrenadores.consultar(int(idconsultada.get()))
                frame_datos_entrenadores=tk.Frame()
                frame_datos_entrenadores.grid(column=0, row=0)
                tk.Label(frame_datos_entrenadores, text="Nombre : ").grid(column=0, row=0)
                tk.Label(frame_datos_entrenadores, text="Sexo : ").grid(column=0, row=1)
                tk.Label(frame_datos_entrenadores, text="Fecha de nacimiento : ").grid(column=0, row=2)
                tk.Label(frame_datos_entrenadores, text="Estado : ").grid(column=0, row=3)
                tk.Label(frame_datos_entrenadores, text=datos["nombre"]).grid(column=1, row=0)
                tk.Label(frame_datos_entrenadores, text=datos["sexo"]).grid(column=1, row=1)
                tk.Label(frame_datos_entrenadores, text=datos["fecha_de_nacimiento"]).grid(column=1, row=2)
                tk.Label(frame_datos_entrenadores, text=datos["estado"]).grid(column=1, row=3)
                tk.Button(frame_datos_entrenadores, text="Editar", command=editar_entrenadores).grid(column=1,row=4)
                tk.Button(frame_datos_entrenadores, text="Volver", command=destruir_framehola_y_mostrar_entrenadores).grid(column=0, row=4)
            except:
                frame_no_existe.grid(column=0,row=1)
                tk.Label(frame_no_existe, text="No existe").grid(column=1, row=otrocontadornosecreto+1)
                otrocontadornosecreto+=1
        probar_consulta() #Esto es solo pa que se corra
    ventana.title("Socios consultar")
    frame_socios.grid_forget()
    frame_consultar.grid(column=0, row=0)
    tk.Label(frame_consultar, text="ID : ").grid(column=0, row=0)
    idconsultada=tk.Entry(frame_consultar)
    idconsultada.grid(column=1, row=0)
    idconsultada.bind("<Return>", extraerdatos)
    tk.Button(frame_consultar, text="Volver", command=destruir_framex_y_mostrar_entrenadores).grid(column=0, row=otrocontadornosecreto+2)

#Todo lo del botón de asistencias
def asistencias_boton():
    frame_ventana_principal.grid_forget()
    ventana.title("Asistencias")
    frame_asistencias.grid(column=0, row=0)
    tk.Label(frame_asistencias, text="ID : ").grid(column=0, row=0)
    idconsultada=tk.Entry(frame_asistencias).grid(column=1, row=0)
    tk.Button(frame_asistencias, text="Asistenciar").grid(column=1, row=1)
    tk.Button(frame_asistencias, text="Volver", command=verventanaprincipal).grid(column=0, row=1)

def ganancias_boton():
    ventana.title("Pagos")
    frame_ventana_principal.grid_forget()
    frame_ganancias.grid(column=0, row=0)
    tk.Button(frame_ganancias, text="Reporte").grid(column=0,row=0)
    tk.Button(frame_ganancias, text="Corte").grid(column=0, row=1)

#Pantalla principal
#¯\_(ツ)_/¯
logo = PhotoImage(file="Logo.png")
tk.Button(frame_ventana_principal, image=logo, command=secretouwu).grid(column=0, row=0, columnspan=2, padx=200)
#🐱‍👓
asistenciasimagen=PhotoImage(file="asistencias.png")
tk.Button(frame_ventana_principal, image=asistenciasimagen, command=asistencias_boton).grid(column=0, row=1)
#Botón e imagén de socios
sociosimagen=PhotoImage(file="socios.png")
tk.Button(frame_ventana_principal, image=sociosimagen, command=socios_boton).grid(column=1, row=1)
#Imagén y botón de ganancias
gananciasimagen=PhotoImage(file="ganancias.png")
tk.Button(frame_ventana_principal, image=gananciasimagen, command=ganancias_boton).grid(column=1, row=2)
#🤣
entrenadoresimagen=PhotoImage(file="entrenador.png")
tk.Button(frame_ventana_principal, image=entrenadoresimagen, command=entrenadores_boton).grid(column=0, row=2)

ventana.mainloop()