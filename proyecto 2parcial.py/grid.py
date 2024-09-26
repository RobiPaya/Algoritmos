import tkinter as tk
lista=[]
listaabecedario=[“a”, “b”, “c”, “d”, “e”, “f”, “g”, “h”, “i”, “j”, “k”, “l”, “m”, “n”, “o”, “p”, “q”, “r”, “s”, “t”, “u”, “v”, “w”, “x”, “y”, “z”, “A”, “B”, “C”, “D”, “E”, “F”, “G”, “H”, “I”, “J”, “K”, “L”, “M”, “N”, “O”, “P”, “Q”, “R”, “S”, “T”, “U”, “V”, “W”, “X”, “Y”, “Z”]
listanumeros=[“0”, “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”]
listasimbolos=[“!”, “@”, “#”, “$”, “%”, “^”, “&”, “*”, “(”, “)”, “-”, “_”, “=”, “+”, “[”, “]”, “{”, “}”, “;”, “:”, “'”, “"”, “,”, “.”, “/”, “<”, “>”, “?”, “\”, “|”, “~”, “`”]
def password():


window=tk.Tk()
window.minsize(width=10, height=10)

imagen = tk.PhotoImage(file="imagess.png")
verimagen = tk.Label(image=imagen).grid(row=1, column=2)

website=tk.Label(text="Website").grid(row=2,column=1)
entradawebsite=tk.Entry(width=28).grid(row=2, column=2, columnspan=2)

email=tk.Label(text="email").grid(row=3,column=1)
entradaemail=tk.Entry(width=28).grid(row=3, column=2, columnspan=2)

password=tk.Label(text="password").grid(row=4,column=1)
entradapassword=tk.Entry(width=19).grid(row=4, column=2, columnspan=1)
generarpassword=tk.Button(text="Generar", width=6).grid(row=4, column=3)

guardar=tk.Button(text="Guardar", width=23).grid(row=5, column=2, columnspan=2)

window.mainloop()