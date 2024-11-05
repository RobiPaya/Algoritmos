import json as js
import tkinter as tk
from clientes import clientes
from abonos import abonos
window=tk.Tk()


def extraerdatos(event):
    datos=abonos.buscarclientes(codigo_entrada=codigo_entrada)
    registro.config(text=datos[0])
    saldo.config(text=datos[1])


            
tk.Label(text="Código").grid(column=0, row=0)
codigo_entrada=tk.Entry()
codigo_entrada.bind("<Return>", extraerdatos)
codigo_entrada.grid(column=0, row=1)
registro=tk.Label(text="")
registro.grid(column=0, row=2) #Label debajo del codigo de entrada cpdigo

saldo=tk.Label(text="Saldo:")
saldo.grid(column=1, row=0)


tk.Label(text="Abono").grid(column=1,row=2)
abono_entrada=tk.Entry(text="$")
abono_entrada.grid(column=1, row=3)

tk.Label(text="Reporte de abonos").grid(column=0, row=5, columnspan=2)


tk.Label(text="").grid(column=0, row=4)

tk.Button(text="Limpiar").grid(column=0, row=6)
tk.Button(text="Cerrar").grid(column=1, row=6)

window.mainloop()