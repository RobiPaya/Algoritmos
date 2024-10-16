import tkinter as tk
window=tk.Tk()

def sacartablas():
    try:
        numero=int(numeroentrada.get())
        for x in range(11):
            resultado=numero*x
            resultadotexto=tk.Label(text=(f"{numero} * {x} = {resultado}"))
            resultadotexto.grid(column=0, row=2+x, columnspan=2)
    except:
        pass

tablasboton=tk.Button(text="Sacar tablas ya!!!", command=sacartablas)
tablasboton.grid(column=0, columnspan=2, row=1)

numerotexto=tk.Label(text="Número : ")
numerotexto.grid(column=0,row=0)
numeroentrada=tk.Entry(justify="right")
numeroentrada.grid(column=1,row=0)

window.mainloop()