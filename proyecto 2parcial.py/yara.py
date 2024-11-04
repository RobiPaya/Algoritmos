import tkinter as tk
import json as js

window=tk.Tk()

def limpiar():
    nombre_entrada.delete(0,len(nombre_entrada.get()))
    direccion_entrada.delete(0,len(direccion_entrada.get()))
    telefono_entrada.delete(0,len(telefono_entrada.get()))
    saldo_entrada.delete(0,len(saldo_entrada.get()))
def guardar():
    lista=[]
    nombre=nombre_entrada.get()
    direccion=direccion_entrada.get()
    telefono=telefono_entrada.get()
    saldo=saldo_entrada.get()
    try:
        with open("clientes.json","r") as archivo:
            for x in archivo:
                lista.append(x)
            lista=sorted(lista,key=lambda columna:columna[0], reverse=True)
            ultimocliente=int(lista[0])
            nuevocliente=ultimocliente+1
    except:
        nuevocliente=1
    datos={nuevocliente:{"nombre":nombre,"direccion":direccion,"telefono":telefono,"saldo":saldo}}
    try:
        with open("cleintes.json","r") as archivo:
            data=js.load(archivo)
            data.update(datos)
        with open("cleintes.json","w") as archivo:
            js.dump(data,archivo,indent=4)
    except:
        with open("cleintes.json","w") as archivo: 
            js.dump(datos,archivo,indent=4)

window.title("Alta cleintes")

tk.Label(text="Nombre").grid(column=0, row=0)
nombre_entrada=tk.Entry()
nombre_entrada.grid(column=1, row=0)

tk.Label(text="Dirección").grid(column=0, row=1)
direccion_entrada=tk.Entry()
direccion_entrada.grid(column=1,row=1)

tk.Label(text="Telefono").grid(column=0, row=2)
telefono_entrada=tk.Entry()
telefono_entrada.grid(column=1, row=2)

tk.Label(text="Saldo").grid(column=0, row=3)
saldo_entrada=tk.Entry()
saldo_entrada.grid(column=1, row=3)

tk.Label().grid(column=2,row=3)

tk.Button(text="Limpiar", command=limpiar).grid(column=0, row=4)
tk.Button(text="Guardar", command=guardar).grid(column=0, row=4, columnspan=2)
tk.Button(text="Salir", command=window.destroy).grid(column=2, row=4, columnspan=1)

window.mainloop()

