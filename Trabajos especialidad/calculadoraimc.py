import tkinter as tk
import json
from tkinter import messagebox
window=tk.Tk()

def guardar():
    try:
        nombre=nombreentrada.get()
        peso=float(pesoentrada.get())
        estatura=float(estaturaentrada.get())
        imc=peso/(estatura**2)
        if imc<16:
            obeso="delgadez severa"
            messagebox.showerror(title="Cuidado", message="Tienes delgadez severa y un bajo peso corporal")
        elif imc>=16 and imc<17:
            obeso="delgadez moderada"
            messagebox.showerror(title="Cuidado", message="Tienes delgadez moderada y un bajo peso corporal")
        elif imc>17 and imc<18.5:
            obeso="delgadez leve"
            messagebox.showerror(title="Cuidado", message="Tienes delgadez leve y un bajo peso corporal")    
        elif imc>=18.5 and imc<=24.9:
            obeso="Normal"
            messagebox.showinfo(title="Normal", message="Tienes peso normal")    
        elif imc>=25 and imc<=29.9:
            obeso="PRE-OBESO"
            messagebox.showwarning(title="Cuidado", message="Eres PRE-OBESO")
        elif imc>=30 and imc<=34.9:
            obeso="OBESO tipo I"
            messagebox.showwarning(title="Cuidado", message="Tienes OBESIDAD TIPO I")
        elif imc>=35 and imc<=39.9:
            obeso="OBESO tipo II"
            messagebox.showwarning(title="Cuidado", message="Tienes OBESIDAD TIPO II")
        elif imc>40:
            obeso="OBESO tipo III"
            messagebox.showwarning(title="Cuidado", message="Eres OBESO III")
        nuevosdatos=({"persona":{"Nombre":nombre,"Peso":peso, "estatura":estatura,"imc":imc, "peso corporal":obeso}})
        with open("Datitos.json","a") as archivo:
            json.dump(nuevosdatos,archivo,indent=4)
    except:
        messagebox.showwarning(title="Faltan", message="Datos")

def ver():
    with open("Datitos.json","r") as archivo:
        data=json.load(archivo)
    texto=tk.Label(text=data["persona"])
    texto.grid(column=0,row=4)
    
nombretexto=tk.Label(text="Nombre : ")
nombretexto.grid(column=0, row=0)
nombreentrada=tk.Entry()
nombreentrada.grid(column=1, row=0)

pesotexto=tk.Label(text="Peso : ")
pesotexto.grid(column=0, row=1)
pesoentrada=tk.Entry()
pesoentrada.grid(column=1, row=1)

estaturatexto=tk.Label(text="Estatura : ")
estaturatexto.grid(column=0, row=2)
estaturaentrada=tk.Entry()
estaturaentrada.grid(column=1, row=2)

guardarboton=tk.Button(text="Generar", command=ver)
guardarboton.grid(column=0, row=3)
generarboton=tk.Button(text="Guardar", width=10, command=guardar)
generarboton.grid(column=1, row=3, columnspan=2)

window.mainloop()