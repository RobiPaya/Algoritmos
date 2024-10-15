import tkinter as tk
from tkinter import messagebox
window=tk.Tk()

def productividad():
    lunes=int(lunesentrada.get())
    martes=int(martesentrada.get())
    miercoles=int(miercolesentrada.get())
    jueves=int(juevesentrada.get())
    viernes=int(viernesentrada.get())
    try:
        sumatoria=lunes+martes+miercoles+jueves+viernes
        if sumatoria>100:
            messagebox.showinfo(title="Felicidades", message="Tienes un bono de productividad")
        else:
            faltantes=100-sumatoria
            messagebox.showinfo(title="Chambea más", message=(f"Te faltaron {faltantes} pal bono"))
    except:
        messagebox.showerror(title="No", message="Faltan datos")

lunestexto=tk.Label(text="Lunes")
lunestexto.grid(column=0,row=1)
lunesentrada=tk.Entry(justify="right")
lunesentrada.grid(column=1,row=1)

martestexto=tk.Label(text="Martes")
martestexto.grid(column=0,row=2)
martesentrada=tk.Entry(justify="right")
martesentrada.grid(column=1,row=2)

miercolestexto=tk.Label(text="Miércoles")
miercolestexto.grid(column=0,row=3)
miercolesentrada=tk.Entry(justify="right")
miercolesentrada.grid(column=1,row=3)

juevestexto=tk.Label(text="Jueves")
juevestexto.grid(column=0,row=4)
juevesentrada=tk.Entry(justify="right")
juevesentrada.grid(column=1,row=4)

viernestexto=tk.Label(text="Viernes")
viernestexto.grid(column=0,row=5)
viernesentrada=tk.Entry(justify="right")
viernesentrada.grid(column=1,row=5)

productividadboton=tk.Button(text="Productividad?", command=productividad)
productividadboton.grid(column=0,columnspan=2,row=0)

window.mainloop()