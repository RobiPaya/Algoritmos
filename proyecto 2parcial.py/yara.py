import tkinter as tk
import json as js

window=tk.Tk()

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

tk.Button(text="Limpiar").grid(column=0, row=4)
tk.Button(text="Guardar").grid(column=0, row=4, columnspan=2)
tk.Button(text="Salir", command=window.destroy).grid(column=2, row=4, columnspan=1)

window.mainloop()

