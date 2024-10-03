import tkinter as tk
def picale():
    print("HOLA")
window=tk.Tk()
window.title("MY FIRST CACA")
window.minsize(width=500,height=400)
titulo=tk.Label(text=("titulo"),font=("Arial",24,"bold"))
titulo.pack(padx=20,pady=70)

boton=tk.Button(window,text=("Diego"),command=picale)
boton.pack()
window.mainloop()