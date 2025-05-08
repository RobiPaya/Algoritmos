from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Función para registrar curso
def registrar():
    e = nombre.get()
    d = edad.get()
    p = especialidad.get()
    
    if not e or not d or not p:
        messagebox.showerror("Error", "Faltan datos")
    else:
        tree.insert("", "end", values=(e, d, p))  # Agregar datos a la tabla
        messagebox.showinfo("Registro exitoso", "El curso ha sido registrado correctamente")  # Mensaje de éxito
        nombre.delete(0, END)  # Limpiar campos
        edad.delete(0, END)
        especialidad.delete(0, END)

# Creación de la ventana
ventana = Tk()
ventana.title("Sistema de gestión de cursos")
ventana.minsize(width=800, height=600)

# Contenedor de pestañas
notebook = ttk.Notebook(ventana)
notebook.grid(row=0, column=0, sticky="nsew")

# Pestañas
frame1 = Frame(notebook)
frame1.grid(row=0, column=0, sticky="nsew")
frame2 = Frame(notebook)
frame2.grid(row=0, column=0, sticky="nsew")

notebook.add(frame1, text="Registro")
notebook.add(frame2, text="Listado de cursos")

# Etiquetas y entradas en la pestaña de registro
Label(frame1, text="Nombre curso : ").grid(column=0, row=1)
Label(frame1, text="Duración en horas : ").grid(column=0, row=2)
Label(frame1, text="Instructor : ").grid(column=0, row=3)

nombre = Entry(frame1)
nombre.grid(column=1, row=1)
edad = Entry(frame1)
edad.grid(column=1, row=2)
especialidad = Entry(frame1)
especialidad.grid(column=1, row=3)

# Botón de registro
Button(frame1, text="Registrar curso", command=registrar).grid(column=0, row=4, columnspan=20)

# Tabla en la pestaña de listado
tree = ttk.Treeview(frame2, columns=("Nombre", "Duración", "Instructor"), show="headings")
tree.heading("Nombre", text="Nombre de curso")
tree.heading("Duración", text="Duración en horas")
tree.heading("Instructor", text="Instructor")

tree.grid(row=0, column=0, sticky="nsew")

# Scrollbar para la tabla
scrollbar = ttk.Scrollbar(frame2, orient="vertical", command=tree.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
tree.configure(yscrollcommand=scrollbar.set)

ventana.mainloop()