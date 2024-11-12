import tkinter as tk
from abonos import abonos
from tkinter import scrolledtext
window=tk.Tk()


def extraerdatos(event):
    datos=abonos.buscarclientes(codigo_entrada=codigo_entrada,abono_entrada=abono_entrada,text_area=text_area)
    if datos[1]=="":
        registro.config(text="")
        saldo.config(text="Saldo:")
        text_area.delete("1.0",tk.END)
        abono_entrada.config(state="disabled")
        pass
    else:
        mostrar=abonos.mostrarregistro(codigo_entrada=codigo_entrada)
        text_area.insert(tk.INSERT,mostrar)
        registro.config(text=datos[0])
        saldo.config(text=datos[1])


def registrarabonos(event):
    datos=abonos.registrarabono(codigo_entrada=codigo_entrada,abono_entrada=abono_entrada)
    saldo.config(text=f"Saldo: ${datos}")
def limpiar():
    codigo_entrada.delete(0,len(codigo_entrada.get()))
    abono_entrada.delete(0,len(abono_entrada.get()))
    text_area.delete("1.0",tk.END)
    saldo.config(text="Saldo:")
    registro.config(text="")
            
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
abono_entrada.bind("<Return>", registrarabonos)
abono_entrada.config(state="disabled")
abono_entrada.grid(column=1, row=3)

tk.Label(text="Reporte de abonos").grid(column=0, row=5, columnspan=2)
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=1)
text_area.grid(column=0, row=6)

tk.Label(text="").grid(column=0, row=4)

tk.Button(text="Limpiar",command=limpiar).grid(column=0, row=8)
tk.Button(text="Cerrar",command=window.destroy).grid(column=1, row=8)

window.mainloop()