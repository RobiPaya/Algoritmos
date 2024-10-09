import tkinter as tk
lista=[]
listaoperaciones=[]
def func1():
    sumador="1"
    texto.insert(0,sumador)
def func2():
    sumador="2"
    texto.insert(0,sumador)
def func3():
    sumador="3"
    texto.insert(0,sumador)
def func4():
    sumador="4"
    texto.insert(0,sumador)
def func5():
    sumador="5"
    texto.insert(0,sumador)
def func6():
    sumador="6"
    texto.insert(0,sumador)
def func7():
    sumador="7"
    texto.insert(0,sumador)
def func8():
    sumador="8"
    texto.insert(0,sumador)
def func9():
    sumador="9"
    texto.insert(0,sumador)
def func0():
    sumador="0"
    texto.insert(0,sumador)
def funcpunto():
    sumador="."
    texto.insert(0,sumador)
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
def funcborra():
    texto.delete(0,1)
def funclear():
    texto.delete(0,len(texto.get()))
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
imagen=tk.PhotoImage(file="vrijit.png")
background=tk.Label(image=imagen)
background.place(x=0, y=0)
window.title("CalculaDora")
texto=tk.Entry()
texto.grid(column=0,row=0, columnspan=5)
num1=tk.Button(text="1",command=func1)
num1.grid(column=1,row=1)
num2=tk.Button(text="2", command=func2)
num2.grid(column=2, row=1)
num3=tk.Button(text="3", command=func3)
num3.grid(column=3, row=1)
num4=tk.Button(text="4", command=func4)
num4.grid(column=1, row=2)
num5=tk.Button(text="5", command=func5)
num5.grid(column=2, row=2)
num6=tk.Button(text="6", command=func6)
num6.grid(column=3, row=2)
num7=tk.Button(text="7", command=func7)
num7.grid(column=1, row=3)
num8=tk.Button(text="8", command=func8)
num8.grid(column=2, row=3)
num9=tk.Button(text="9", command=func9)
num9.grid(column=3, row=3)
num0=tk.Button(text="0", command=func0)
num0.grid(column=2, row=4)
suma=tk.Button(text="+", command=func10)
suma.grid(column=4, row=1)
resta=tk.Button(text="-", command=func11)
resta.grid(column=4, row=2)
multiplicacion=tk.Button(text="*", command=func12)
multiplicacion.grid(column=4, row=3)
division=tk.Button(text="/", command=func13)
division.grid(column=4, row=5)
porcentaje=tk.Button(text="%", command=func14)
porcentaje.grid(column=3, row=5)
borrar=tk.Button(text="<-", command=funcborra)
borrar.grid(column=2, row=5)
clear=tk.Button(text="C", command=funclear)
clear.grid(column=1, row=5)
punto=tk.Button(text=".", command=funcpunto)
punto.grid(column=3, row=4)
igual=tk.Button(text="=",command=funcigual)
igual.grid(column=3,row=5)


window.mainloop()