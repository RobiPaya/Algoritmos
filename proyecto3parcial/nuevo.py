from socios import socios
from tkinter import Menu
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkcalendar import DateEntry
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

#Cosa pa ver la ventana principal otra vez
def verventanaprincipal():
    ventana.title("Inicio")
    frame_entrenadores.grid_forget()
    frame_asistencias.grid_forget()
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
            try:
                datos=socios.consultar(int(idconsultada.get()))
                frame_datos_socios=tk.Frame()
                frame_datos_socios.grid(column=0, row=0)
                tk.Label(frame_datos_socios, text=datos).grid(column=1, row=1)
                tk.Button(frame_datos_socios, text="Volver", command=destruir_framehola_y_mostrar_socios).grid(column=0, row=0)
                ventana.title("Socio consultado")
                frame_no_existe.grid_forget()
                frame_consultar.grid_forget()
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
    cambios_entrada=tk.StringVar()
    ventana.title("Socios registrar")
    def registrar_socios():
        nombre_geteado=nombre.get()
        sexo_getado=sexo.get()
        fechadenacimiento_geteado=fechadenacimiento.get()
        if not nombre_geteado or not sexo_getado or not fechadenacimiento_geteado:
            messagebox.showerror("Error", "Faltan datos")
        else:
            socios.registrar(nombre,sexo,fechadenacimiento)
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
    ventana.title("Entrenadores registar")
    frame_entrenadores.grid_forget()
    frame_registrar.grid(column=0, row=0)
    tk.Label(frame_registrar, text="Nombre : ").grid(column=0, row=0)
    nombre=tk.Entry(frame_registrar).grid(column=1, row=0)
    tk.Label(frame_registrar, text="Sexo : ").grid(column=0, row=1)
    sexo=tk.Entry(frame_registrar).grid(column=1, row=1)
    tk.Label(frame_registrar, text="Fecha de nacimiento : ").grid(column=0, row=2)
    fechadenacimiento=tk.Entry(frame_registrar).grid(column=1, row=2)
    tk.Button(frame_registrar, text="Registrar").grid(column=1, row=4)
    tk.Button(frame_registrar, text="Volver", command=entrenadores_boton).grid(column=0, row=4)
def entrenadores_consultar():
    ventana.title("Entrenadores consultar")
    frame_consultar.grid(column=0, row=0)
    frame_entrenadores.grid_forget()
    tk.Label(frame_consultar, text="ID : ").grid(column=0, row=0)
    idconsultada=tk.Entry(frame_consultar)
    idconsultada.grid(column=1, row=0)
    #idconsultada.bind("<Return>", pass)
    tk.Button(frame_consultar, text="Volver", command=entrenadores_boton).grid(column=0, row=1)

#Todo lo del botón de asistencias
def asistencias_boton():
    frame_ventana_principal.grid_forget()
    ventana.title("Asistencias")
    frame_asistencias.grid(column=0, row=0)
    tk.Label(frame_asistencias, text="ID : ").grid(column=0, row=0)
    idconsultada=tk.Entry(frame_asistencias).grid(column=1, row=0)
    tk.Button(frame_asistencias, text="Asistenciar").grid(column=1, row=1)
    tk.Button(frame_asistencias, text="Volver", command=verventanaprincipal).grid(column=0, row=1)

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
tk.Button(frame_ventana_principal, image=gananciasimagen).grid(column=1, row=2)
#🤣
entrenadoresimagen=PhotoImage(file="entrenador.png")
tk.Button(frame_ventana_principal, image=entrenadoresimagen, command=entrenadores_boton).grid(column=0, row=2)

ventana.mainloop()