import tkinter as tk
import json as js
def func():
    estaturareal=float(entradamart.get())
    pesokg=float(entradalune.get())
    personareal=entrada.get()
    imc=pesokg/(estaturareal**2)
    
    if imc<=18.5:
        salud="Por Debajo"
    elif imc>18.5 and imc<25:
        salud="Saludable"
    elif imc>=25 and imc<30:
        salud="Sobrepeso"
    elif imc>=30:
        salud="obesidad"
    datos=({personareal:{"Peso":pesokg,"Estatura":estaturareal,"IMC":imc,"Estado":salud}})
    with open("datospesososo.json","a") as archivo:
        js.dump(datos,archivo,indent=4)
    label.config(text=f"IMC:{imc:.2f}\nEstas {salud}")
window=tk.Tk()
window.title("masa")
window.minsize(250,100)
persona=tk.Label(text="Nombre:").place(x=20,y=30)
pesoenkg=tk.Label(text="Peso en kg:").place(x=20,y=50)
estatura=tk.Label(text="Estatura en m:").place(x=20,y=70)
entrada=tk.Entry(justify="right")
entradalune=tk.Entry(justify="right")
entradamart=tk.Entry(justify="right")
entrada.place(x=100,y=30)
entradalune.place(x=100,y=50)
entradamart.place(x=100,y=70)
boton=tk.Button(text="CALCULAR",command=func)
boton.place(x=125,y=90)
boton2=tk.Button(text="REPORTE")
label=tk.Label(text="")
label.place(x=125,y=130)
window.mainloop()