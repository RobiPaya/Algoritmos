import json as js
import tkinter as tk

window=tk.Tk()


def extraerdatos(event):
    codigo_entradita=codigo_entrada.get()
    with open("cleintes.json","r") as archivo:
        data=js.load(archivo)
    for x in data:
        if x==codigo_entradita:
            print(codigo_entradita)

            
tk.Label(text="Código").grid(column=0, row=0)
codigo_entrada=tk.Entry()
codigo_entrada.bind("<Return>", extraerdatos)
codigo_entrada.grid(column=0, row=1)
tk.Label(text="").grid(column=0, row=2) #Label debajo del codigo de entrada cpdigo

tk.Label(text="Saldo:").grid(column=1, row=0)


tk.Label(text="Abono").grid(column=1,row=2)
abono_entrada=tk.Entry(text="$")
abono_entrada.grid(column=1, row=3)

tk.Label(text="Reporte de abonos").grid(column=0, row=5, columnspan=2)


tk.Label(text="").grid(column=0, row=4)

tk.Button(text="Limpiar").grid(column=0, row=6)
tk.Button(text="Cerrar").grid(column=1, row=6)

window.mainloop()