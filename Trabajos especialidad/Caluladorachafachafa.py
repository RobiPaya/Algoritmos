import tkinter as tk
def func1():
    sumador = (str(texto["text"]))
    sumador += "1"
    texto.config(text=str(sumador))
def func2():
    sumador = (str(texto["text"]))
    sumador += "2"
    texto.config(text=str(sumador))
def func3():
    sumador = (str(texto["text"]))
    sumador += "3"
    texto.config(text=str(sumador))
def func4():
    sumador = (str(texto["text"]))
    sumador += "4"
    texto.config(text=str(sumador))
def func5():
    sumador = (str(texto["text"]))
    sumador += "5"
    texto.config(text=str(sumador))
def func6():
    sumador = (str(texto["text"]))
    sumador += "6"
    texto.config(text=str(sumador))
def func7():
    sumador = (str(texto["text"]))
    sumador += "7"
    texto.config(text=str(sumador))
def func8():
    sumador = (str(texto["text"]))
    sumador += "8"
    texto.config(text=str(sumador))
def func9():
    sumador = (str(texto["text"]))
    sumador += "9"
    texto.config(text=str(sumador))
def func0():
    sumador = (str(texto["text"]))
    sumador += "0"
    texto.config(text=str(sumador))
def func10():
    sumador = (str(texto["text"]))
    sumador += "+"
    texto.config(text=str(sumador))

def multiple():
    return[func10(),]
lista=[]
window=tk.Tk()
window.title("CalculaDora")
texto=tk.Label(text="")
texto.grid(column=0,row=0, columnspan=5)
num1=tk.Button(text="1",command=func1, width=1, height=1)
num1.grid(column=1,row=1)
num2=tk.Button(text="2", command=func2, width=1, height=1)
num2.grid(column=2, row=1)
num3=tk.Button(text="3", command=func3, width=1, height=1)
num3.grid(column=3, row=1)
num4=tk.Button(text="4", command=func4, width=1, height=1)
num4.grid(column=1, row=2)
num5=tk.Button(text="5", command=func5, width=1, height=1)
num5.grid(column=2, row=2)
num6=tk.Button(text="6", command=func6, width=1, height=1)
num6.grid(column=3, row=2)
num7=tk.Button(text="7", command=func7, width=1, height=1)
num7.grid(column=1, row=3)
num8=tk.Button(text="8", command=func8, width=1, height=1)
num8.grid(column=2, row=3)
num9=tk.Button(text="9", command=func9, width=1, height=1)
num9.grid(column=3, row=3)
num0=tk.Button(text="0", command=func0, width=1, height=1)
num0.grid(column=2, row=4)
suma=tk.Button(text="+", command=multiple, width=1, height=1)
suma.grid(column=4, row=1)
resta=tk.Button(text="-", command=multiple, width=1, height=1)
resta.grid(column=4, row=2)
multiplicacion=tk.Button(text="*", command=multiple, width=1, height=1)
multiplicacion.grid(column=4, row=3)
division=tk.Button(text="/", command=multiple, width=1, height=1)
division.grid(column=4, row=4)
porcentaje=tk.Button(text="%", command=multiple, width=1, height=1)
porcentaje.grid(column=3, row=5)
borrar=tk.Button(text="<-", command=multiple, width=1, height=1)
borrar.grid(column=2, row=5)
clear=tk.Button(text="C", command=multiple, width=1, height=1)
clear.grid(column=1, row=5)
punto=tk.Button(text=".", command=multiple, width=1, height=1)
punto.grid(column=3, row=4)
igual=tk.Button(text="=", command=multiple, width=1, height=1)
igual.grid(column=4, row=5)
window.mainloop()