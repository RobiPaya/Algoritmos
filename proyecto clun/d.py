import tkinter as tk
ventana=tk.Tk()
ventana.title(f"/50 Estados correctos")
entrada=tk.Entry(ventana)
entrada.pack(padx=50,pady=20)
answer_state=entrada.get()
boton=tk.Button(ventana,text="OK",command=ventana.destroy)
boton.pack(padx=20)