import tkinter as tk
def func():
    estaturareal=float(entradamart.get())
    pesokg=float(entradalune.get())
    imc=pesokg/(estaturareal**2)
    label.config(text=f"IMC:{imc:.2f}")
window=tk.Tk()
window.title("masa")
window.minsize(250,100)
pesoenkg=tk.Label(text="Peso en kg:").place(x=20,y=50)
estatura=tk.Label(text="Estatura en m:").place(x=20,y=70)
entradalune=tk.Entry(justify="right")
entradamart=tk.Entry(justify="right")
entradalune.place(x=100,y=50)
entradamart.place(x=100,y=70)
boton=tk.Button(text="CALCULAR",command=func)
boton.place(x=125,y=90)
label=tk.Label(text="")
label.place(x=125,y=130)




window.mainloop()