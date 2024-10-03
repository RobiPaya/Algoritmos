import tkinter as tk
def calcular():
    if nose.get()==1:
        respuesta=int(entrada.get())
        resu=respuesta*1.609
        resultado.config(text=(f"{respuesta} millas son {resu:.2f} kms"))
    elif nose.get()==2:
        respuesta=int(entrada.get())
        resu=respuesta/1.609
        resultado.config(text=(f"{respuesta} kms son {resu:.2f} millas"))
ventana=tk.Tk()
ventana.title("Convertidor")
ventana.minsize(width=500,height=400)
entrada=tk.Entry()
entrada.place(x=190,y=54)
nose=tk.IntVar()
nota=tk.Label(text=("Valor")).place(x=150,y=54)
radiobutton1 = tk.Radiobutton(ventana,text="Millas a km", variable=nose, value=1)
radiobutton2 = tk.Radiobutton(ventana,text="km a Millas", variable=nose, value=2)
radiobutton1.place(x=190,y=74)
radiobutton2.place(x=190,y=94)
boton=tk.Button(text="Calcular",command=calcular)
boton.place(x=300,y=84)
resultado=tk.Label(text=(""))
resultado.place(x=190,y=120)
ventana.mainloop()