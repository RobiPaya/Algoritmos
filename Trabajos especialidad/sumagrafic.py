import tkinter as tk
def suma():
    numero1=int(entrada1.get())
    numero2=int(entrada2.get())
    resu=numero1+numero2
    resultado.config(text=(f"Resultado {resu}"))
ventana=tk.Tk()
ventana.title("SUMA")
ventana.minsize(width=500,height=400)   
titulo=tk.Label(text=("SUMA"),font=("Arial",24,"bold")).pack()
entrada1=tk.Entry()
entrada2=tk.Entry()
entrada1.place(x=190,y=54)
entrada2.place(x=190,y=84)
boton=tk.Button(ventana,text=("SUMA"),command=suma)
boton.place(x=355,y=120)
resultado=tk.Label(text=(f"Resultado 0"))
resultado.place(x=200,y=120)
ventana.mainloop()