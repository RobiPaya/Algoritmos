import tkinter as tk
from tkinter import messagebox
def func():
    dias=int(entradalune.get())+int(entradamart.get())+int(entradamier.get())+int(entradajueve.get())+int(entradavierne.get())
    if dias>100:
        messagebox.showinfo(title="BONO INSANO",message="♥♥♥♥Felicidades tienes un Bono de Productividad♥♥♥♥")
    elif dias<100:
        messagebox.showinfo(title="BONO NO-INSANO",message=f"Te faltaron {100-dias} para alcanzar tu bono")
    elif dias==100:
        messagebox.showinfo(title="NO",message="CONSEGUISTE LOS 100 EXACTOS")
window=tk.Tk()
window.title("bono")
window.minsize(400,400)
lunes=tk.Label(text="Lunes").place(x=40,y=50)
martes=tk.Label(text="Martes").place(x=40,y=70)
miercoles=tk.Label(text="Miercoles").place(x=40,y=90)
jueves=tk.Label(text="Jueves").place(x=40,y=110)
viernes=tk.Label(text="Viernes").place(x=40,y=130)
entradalune=tk.Entry(justify="right")
entradamart=tk.Entry(justify="right")
entradamier=tk.Entry(justify="right")
entradajueve=tk.Entry(justify="right")
entradavierne=tk.Entry(justify="right")
entradalune.place(x=100,y=50)
entradamart.place(x=100,y=70)
entradamier.place(x=100,y=90)
entradajueve.place(x=100,y=110)
entradavierne.place(x=100,y=130)
boton=tk.Button(text="Ejecutar",command=func)
boton.place(x=140,y=150)
window.mainloop()