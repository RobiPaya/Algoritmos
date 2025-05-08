import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import matplotlib.pyplot as pito

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Pedido de Pizza")
ventana.geometry("500x400")

# Crear un canvas y una scrollbar para poder desplazar el contenido
canvas = tk.Canvas(ventana)
scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Crear un frame dentro del canvas que contendrá todos los widgets
scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Actualizar la región de scroll cada vez que cambie el tamaño del frame
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

# Fuente para los labels
font_label = ("Arial", 12, "bold")

# Fila 0: Etiqueta "Tamaño:" y Menubutton de opciones
ttk.Label(scrollable_frame, text="Tamaño:", font=font_label).grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Variable para la selección del menú
pizza_option = tk.StringVar(value="Sin opción")

# Menubutton usando ttk (opciones de Pizza)
menu_opciones = ttk.Menubutton(scrollable_frame, text="Opciones de Pizza")
menu_opciones.grid(row=0, column=1, padx=10, pady=5, sticky="e")

menu = tk.Menu(menu_opciones, tearoff=0)
menu.add_command(label="Masa Delgada", command=lambda: pizza_option.set("Masa Delgada"))
menu.add_command(label="Masa Gruesa", command=lambda: pizza_option.set("Masa Gruesa"))
menu.add_command(label="Oferta del Día", command=lambda: pizza_option.set("Oferta del Día"))
menu.add_command(label="Acompañamientos", command=lambda: pizza_option.set("Acompañamientos"))
menu_opciones["menu"] = menu

# Variable para los Radiobuttons (Tamaño)
tamaño_var = tk.StringVar(value="")  # Ningún radio button seleccionado al iniciar

# Fila 1-3: Radiobuttons para el tamaño
ttk.Radiobutton(scrollable_frame, text="Chica", variable=tamaño_var, value="Chica")\
    .grid(row=1, column=0, padx=10, sticky="w")
ttk.Radiobutton(scrollable_frame, text="Mediana", variable=tamaño_var, value="Mediana")\
    .grid(row=2, column=0, padx=10, sticky="w")
ttk.Radiobutton(scrollable_frame, text="Grande", variable=tamaño_var, value="Grande")\
    .grid(row=3, column=0, padx=10, sticky="w")

# Fila 4: Etiqueta para ingredientes
ttk.Label(scrollable_frame, text="Ingredientes:", font=font_label)\
    .grid(row=4, column=0, padx=10, pady=5, sticky="w")

# Variables para los Checkbuttons
pepperoni_var = tk.IntVar()
salami_var = tk.IntVar()
pimientos_var = tk.IntVar()
carne_var = tk.IntVar()
jamon_piña_var = tk.IntVar()

# Filas 5-9: Checkbuttons para los ingredientes
ttk.Checkbutton(scrollable_frame, text="Pepperoni", variable=pepperoni_var)\
    .grid(row=5, column=0, sticky="w", padx=10)
ttk.Checkbutton(scrollable_frame, text="Salami", variable=salami_var)\
    .grid(row=6, column=0, sticky="w", padx=10)
ttk.Checkbutton(scrollable_frame, text="Pimientos", variable=pimientos_var)\
    .grid(row=7, column=0, sticky="w", padx=10)
ttk.Checkbutton(scrollable_frame, text="Carne Asada", variable=carne_var)\
    .grid(row=8, column=0, sticky="w", padx=10)
ttk.Checkbutton(scrollable_frame, text="Jamón/Piña", variable=jamon_piña_var)\
    .grid(row=9, column=0, sticky="w", padx=10)

# Fila 10: Etiqueta para la fecha del pedido
ttk.Label(scrollable_frame, text="Fecha del Pedido:", font=font_label)\
    .grid(row=10, column=0, padx=10, pady=5, sticky="w")

#Seleccionar la fecha
date_entry = DateEntry(scrollable_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=11, column=0, padx=10, pady=5, sticky="w")

# Fila 12: Botón para mostrar el pedido
def mostrar_pedido():
    # Construir los datos del pedido
    tamaño = tamaño_var.get()
    ingredientes_list = []
    if pepperoni_var.get():
        ingredientes_list.append("Pepperoni")
    if salami_var.get():
        ingredientes_list.append("Salami")
    if pimientos_var.get():
        ingredientes_list.append("Pimientos")
    if carne_var.get():
        ingredientes_list.append("Carne Asada")
    if jamon_piña_var.get():
        ingredientes_list.append("Jamón/Piña")
    
    # Obtener la fecha seleccionada
    fecha_pedido = date_entry.get_date()
    
    pedido = (
        f"Pedido:\n\n"
        f"Fecha: {fecha_pedido}\n\n"
        f"Tamaño: {tamaño if tamaño else 'No seleccionado'}\n\n"
        f"Ingredientes:\n{', \n'.join(ingredientes_list) if ingredientes_list else 'Ninguno'}\n\n"
        f"Extra o algo 852as225252825: {pizza_option.get()}"
    )
    pedido_label.config(text=pedido)

ttk.Button(scrollable_frame, text="Mostrar Pedido", command=mostrar_pedido)\
    .grid(row=12, column=1, padx=10, pady=5)

# Fila 13: Etiqueta para mostrar el pedido resultante
pedido_label = ttk.Label(scrollable_frame, text="", font=font_label, justify="left")
pedido_label.grid(row=13, column=0, columnspan=2, padx=10, pady=5, sticky="w")

ventana.mainloop()

#crear 2 listas con los nombres de 5 estudiantes y sus calificaciones en 2 materias (matéamtica y cienca) utiliza matplotlib 
#para hacer un gráfico de barras comparando las calificaciones de am89as materias y haz un grafico de lineas mostrando la 
#evolución de cada estudiamte