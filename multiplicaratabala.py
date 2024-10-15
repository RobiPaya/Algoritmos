import tkinter as tk
def func():
    numero=entrda.get()
    label.config(text=f'''1x{numero}={int(numero)*1}        6x{numero}={int(numero)*6}
2x{numero}={int(numero)*2}      7x{numero}={int(numero)*7}
3x{numero}={int(numero)*3}      8x{numero}={int(numero)*8}
4x{numero}={int(numero)*4}      9x{numero}={int(numero)*9}
5x{numero}={int(numero)*5}      10x{numero}={int(numero)*10}''')
    entrda.delete(0,len(entrda.get()))
window=tk.Tk()
window.title("Tablas de multiplicar")
window.minsize(400,400)
entrda=tk.Entry(justify="right")
entrda.place(x=100,y=50,width=200)
boton=tk.Button(text="Ejecutar",command=func)
boton.place(x=175,y=100)
label=tk.Label(text="")
label.place(x=150,y=130)
window.mainloop()