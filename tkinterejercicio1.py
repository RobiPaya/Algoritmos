from tkinter import *
from tkinter import messagebox

#Funciones
def registrar():
    e = nombre.get()
    d = edad.get()
    p = especialidad.get()
    if not e or not d or not p:
        messagebox.showerror("Error", "Faltan datos")
    else:
        Label(ventana, text=f"{e, d, p}").grid(column=0, row=4, columnspan=20)

#Creación de la ventana
ventana = Tk()
ventana.title("Registro de estudiantes")
ventana.minsize(width=500, height=400)

#Etiquetas mostradas en pantalla
etiquetanombre = Label(ventana, text="Nombre estudiante : ")
etiquetanombre.grid(column=0, row=0)

etiquetaedad = Label(ventana, text="Edad : ")
etiquetaedad.grid(column=0, row=1)

etiquetaespecialidad = Label(ventana, text="Especialidad : ")
etiquetaespecialidad.grid(column=0, row=2)

#Entrys
nombre = Entry()
nombre.grid(column=1, row=0)
edad = Entry()
edad.grid(column=1, row=1)
especialidad = Entry()
especialidad.grid(column=1, row=2)

#Botón
Button(ventana, text="Registrar estudiante", command=registrar).grid(column=0,row=3, columnspan=20)

ventana.mainloop()