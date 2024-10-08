import tkinter as tk
from tkinter import messagebox
import random as r
import json as json
#
lista=[]
listaabecedario=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
listanumeros=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
listasimbolos=['!', '#', '$', '%', '&', '(', ')', '*', '+']
def archivo():
    web=entradawebsite.get()
    user=entradaemail.get()
    passw=entradapassword.get()
    #py.copy(passw)
    if not web or not user or not passw:
        messagebox.showinfo(title="NADA", message="FALTAN DATOS")
    else:
        ok = messagebox.askokcancel(title="Titulo", message="Quieres guardar esta información?")
        if ok :
            try:
                with open("datos.json", "a") as archivo:
                    archivo.write(f"{web} | {user} | {passw}\n")
                    entradapassword.delete(0, len(entradapassword.get()))
                    entradaemail.delete(0, len(entradaemail.get()))
                    entradawebsite.delete(0, len(entradawebsite.get()))
            except:
                messagebox.showinfo(title="ERROR", message="NO SE PUDO ABRIR EL ARCHIVO")
def buscar():
    web=entradawebsite.get()
    if not web:
        messagebox.showinfo(title="NADA", message="FALTAN DATOS")
    else:
        with open("datos.json", "r") as data_file:
            archivo = json.load(data_file) # La información del archivo se guarda en "datos"
            print(type(archivo)) # datos es un diccionario que contiene la información del archivo
            print(archivo) # Aqui se muestra en consola el contenido del archivo
def passwords():
    rango=r.randint(8,12)
    entradapassword.delete(0,len(entradapassword.get()))
    for x in range(rango):
        opcion=r.randint(1,3)
        if opcion==1:
            lista.append(r.choice(listaabecedario))
        elif opcion==2:
            lista.append(r.choice(listanumeros))
        elif opcion==3:
            lista.append(r.choice(listasimbolos))
    passwordsss=""
    passwordsss=passwordsss.join(lista)
    entradapassword.insert(0,passwordsss)
    lista.clear()
window=tk.Tk()
window.minsize(width=10, height=10)
imagen = tk.PhotoImage(file="imagess.png")
verimagen = tk.Label(image=imagen).grid(row=1, column=2)
website=tk.Label(text="Website").grid(row=2,column=1)
entradawebsite=tk.Entry(width=28)
entradawebsite.grid(row=2, column=2, columnspan=2)
generarbuscar=tk.Button(text="Buscar", width=6,command=buscar)
generarbuscar.grid(row=2, column=3)
email=tk.Label(text="email").grid(row=3,column=1)
entradaemail=tk.Entry(width=28)
entradaemail.grid(row=3, column=2, columnspan=2)
password=tk.Label(text="password").grid(row=4,column=1)
entradapassword=tk.Entry(width=19)
entradapassword.grid(row=4, column=2, columnspan=1)
generarpassword=tk.Button(text="Generar", width=6,command=passwords)
generarpassword.grid(row=4, column=3)
guardar=tk.Button(text="Guardar", width=23,command=archivo)
guardar.grid(row=5, column=2, columnspan=2)
window.mainloop()