import tkinter as tk
def calcular():
    millas=int(entrada.get())
    resu=millas*1.609
    respuesta.config(text=(f"Equivale a {resu:.2f} kms"))
ventana=tk.Tk()
ventana.title("Convertidor")
ventana.minsize(width=500,height=400)
entrada=tk.Entry()
entrada.grid(column=1,row=1,pady=54,padx=190)
nota=tk.Label(text=("Millas")).grid(column=2,row=1)
respuesta=tk.Label(text=("Equivale a 0 kms"))
respuesta.place(x=190,y=74)
boton=tk.Button(ventana,text=("Calcular"),command=calcular)
boton.place(x=210,y=94)
ventana.mainloop()