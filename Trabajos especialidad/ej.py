from tkinter import *

#Creación de la ventana principal
root = Tk()
#Título de la ventana
root.title("www.programacionfacil.org")

opcion = IntVar()

#Radiobutton
Radiobutton(root,
           text="Rojo", 
           variable=opcion, 
           value=1).pack()

Radiobutton(root,
           text="Azul",
           variable=opcion, 
           value=2).pack()

Radiobutton(root,
           text="Verde",
           variable=opcion, 
           value=3).pack()

Radiobutton(root,
           text="Amarillo",
           variable=opcion, 
           value=4).pack()

#Bucle de ejecución
root.mainloop()