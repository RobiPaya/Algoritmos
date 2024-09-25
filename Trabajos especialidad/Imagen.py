import tkinter as tk

root = tk.Tk()
root.title("Imagen en Tk")
o = tk.PhotoImage(file="Trabajos especialidad/No abrirb.png")
root.geometry("500x500")
label = tk.Label(image=o)
label.pack()
root.mainloop()