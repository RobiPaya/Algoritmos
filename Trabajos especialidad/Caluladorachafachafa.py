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
texto.pack()
num1=tk.Button(text="1",command=func1)
num1.pack()
num2=tk.Button(text="2", command=func2)
num2.pack()
num3=tk.Button(text="3", command=func3)
num3.pack()
num4=tk.Button(text="4", command=func4)
num4.pack()
num5=tk.Button(text="5", command=func5)
num5.pack()
num6=tk.Button(text="6", command=func6)
num6.pack()
num7=tk.Button(text="7", command=func7)
num7.pack()
num8=tk.Button(text="8", command=func8)
num8.pack()
num9=tk.Button(text="9", command=func9)
num9.pack()
num0=tk.Button(text="0", command=func0)
num0.pack()
num10=tk.Button(text="+", command=multiple)
num10.pack()




window.mainloop()