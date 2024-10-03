import tkinter as tk
def funcA():
    print("1")
def funcB():
    print("2")
def funcC():
    print("3")
def sumastr():
    texto1.config(text="H")
def command():
    return[funcA(),funcB(),funcC()]
window=tk.Tk()
window.title("Dora")
texto=tk.Label(text="-")
texto.pack()
texto1=tk.Label(text="hola")
texto1.pack()
num1=tk.Button(text="1", command=command)
num1.pack()
window.mainloop()