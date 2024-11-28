"""""import tkinter as tk 
from tkinter import messagebox 
from tkcalendar import DateEntry 
def funcion_externa(): # Crear la ventana principal 
    root = tk.Tk() 
    root.title("Seleccionar Fecha") 
    def mostrar_fecha(): # Obtener la fecha seleccionada 
        fecha_seleccionada = calendario.get_date()
        print(fecha_seleccionada)
        messagebox.showinfo("Fecha Seleccionada", f"La fecha seleccionada es: {fecha_seleccionada}") # Crear un widget de selección de fecha 
    calendario = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
     
    calendario.pack(pady=10) # Crear un botón para mostrar la fecha seleccionada 
    boton_mostrar = tk.Button(root, text="Mostrar Fecha", command=mostrar_fecha) 
    boton_mostrar.pack(pady=10) # Ejecutar el bucle principal de la interfaz 
    root.mainloop() # Llamar a la función externa para iniciar la aplicación funcion_externa()
funcion_externa()"""

import tkinter as tk
from tkcalendar import DateEntry

def obtener_fecha():
    fecha = entrada_fecha.get()
    etiqueta.config(text=f"Fecha seleccionada: {fecha}")

# Crear la ventana principal
root = tk.Tk()
root.title("Selección de Fecha")

# Crear el DateEntry para seleccionar la fecha
entrada_fecha = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd-mm-yyyy')
entrada_fecha.pack(pady=20)

# Botón para obtener la fecha seleccionada
boton = tk.Button(root, text="Obtener Fecha", command=obtener_fecha)
boton.pack(pady=20)

# Etiqueta para mostrar la fecha seleccionada
etiqueta = tk.Label(root, text="")
etiqueta.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
