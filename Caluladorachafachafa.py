import tkinter as tk
lista=[]
listaoperaciones=[]
def func10():
    sumador=float(texto.get())
    texto.delete(0,len(texto.get()))
    lista.append(sumador)
    listaoperaciones.append("+")
def func11():
    sumador=float(texto.get())
    texto.delete(0,len(texto.get()))
    lista.append(sumador)
    listaoperaciones.append("-")
def func12():
    sumador=float(texto.get())
    texto.delete(0,len(texto.get()))
    lista.append(sumador)
    listaoperaciones.append("x")
def func13():
    sumador=float(texto.get())
    texto.delete(0,len(texto.get()))
    lista.append(sumador)
    listaoperaciones.append("/")
def func14():
    sumador=float(texto.get())
    texto.delete(0,len(texto.get()))
    lista.append(sumador)
    listaoperaciones.append("%")
def funcigual():
    numer1=lista[0]
    numer2=float(texto.get())
    operacion=listaoperaciones[0]
    if operacion=="+":
        resultado=numer1+numer2
    elif operacion=="-":
        resultado=numer1-numer2
    elif operacion=="x":
        resultado=numer1*numer2
    elif operacion=="/":
        resultado=numer1/numer2
    elif operacion=="%":
        resultado=num1*num2/100
    texto.delete(0,len(texto.get()))
    texto.insert(0,resultado)
    lista.clear()
    listaoperaciones.clear()

window=tk.Tk()
texto=tk.Entry(justify="right")
texto.grid(column=0,row=0, columnspan=5)
num1=tk.Button(text="1",command=texto.insert(len(texto.get()),"1"), width=3, height=3)
num1.grid(column=1,row=1)
num2=tk.Button(text="2", command=texto.insert(len(texto.get()),"2"), width=3, height=3)
num2.grid(column=2, row=1)
num3=tk.Button(text="3", command=texto.insert(len(texto.get()),"3"), width=3, height=3)
num3.grid(column=3, row=1)
num4=tk.Button(text="4", command=texto.insert(len(texto.get()),"4"), width=3, height=3)
num4.grid(column=1, row=2)
num5=tk.Button(text="5", command=texto.insert(len(texto.get()),"5"), width=3, height=3)
num5.grid(column=2, row=2)
num6=tk.Button(text="6", command=texto.insert(len(texto.get()),"6"), width=3, height=3)
num6.grid(column=3, row=2)
num7=tk.Button(text="7", command=texto.insert(len(texto.get()),"7"), width=3, height=3)
num7.grid(column=1, row=3)
num8=tk.Button(text="8", command=texto.insert(len(texto.get()),"8"), width=3, height=3)
num8.grid(column=2, row=3)
num9=tk.Button(text="9", command=texto.insert(len(texto.get()),"9"), width=3, height=3)
num9.grid(column=3, row=3)
num0=tk.Button(text="0", command=texto.insert(len(texto.get()),"0"), width=3, height=3)
num0.grid(column=2, row=4)
suma=tk.Button(text="+", command=func10, width=3, height=3)
suma.grid(column=4, row=1)
resta=tk.Button(text="-", command=func11, width=3, height=3)
resta.grid(column=4, row=2)
multiplicacion=tk.Button(text="*", command=func12, width=3, height=3)
multiplicacion.grid(column=4, row=3)
division=tk.Button(text="/", command=func13, width=3, height=3)
division.grid(column=4, row=4)
porcentaje=tk.Button(text="%", command=func14, width=3, height=3)
porcentaje.grid(column=3, row=5)
borrar=tk.Button(text="<-", command=texto.delete(len(texto.get())-1,len(texto.get())), width=3, height=3)
borrar.grid(column=2, row=5)
clear=tk.Button(text="C", command=texto.delete(0,len(texto.get())), width=3, height=3)
clear.grid(column=1, row=5)
punto=tk.Button(text=".", command=texto.insert(len(texto.get()),"."), width=3, height=3)
punto.grid(column=3, row=4)
igual=tk.Button(text="=", command=funcigual, width=3, height=3)
igual.grid(column=4, row=5)
window.mainloop()