import tkinter as tk
window=tk.Tk()
hola=""
def agregar():
    texto.config(text=hola+"1")
def cambiar2():
    texto.config(text=hola+"2")
texto=tk.Label(text="w")
texto.pack()
num1=tk.Button(text="1",command=agregar)
num1.pack()
num2=tk.Button(text="2",command=cambiar2)
num2.pack()







window.mainloop()