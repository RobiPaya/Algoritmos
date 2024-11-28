"""def socios_registar():
    ventana.title("Socios registrar")
    def registrar_socios():
        similitudes=False
        nombre_geteado=nombre.get()
        sexo_getado=sexo.get()
        fechadenacimiento_geteado=fechadenacimiento.get_date().strftime('%d-%m-%Y')
        print(fechadenacimiento_geteado)
        archivo=pd.read_csv("socios.csv")
        for idx, row in archivo.iterrows():
            for col_index, col_name in enumerate(archivo.columns):
                if (nombre_geteado in str(row.iloc[col_index]) and sexo_getado in str(row.iloc[col_index]) and fechadenacimiento_geteado in str(row.iloc[col_index])):
                    similitudes=True
                    break
            if similitudes:
                break
        if similitudes:
            messagebox.showerror("Igual", "Ya está registrado")
        elif not nombre_geteado or not sexo_getado or not fechadenacimiento_geteado:
            messagebox.showerror("Error", "Faltan datos")
        else:
            socios.registrar(nombre_geteado,sexo_getado,fechadenacimiento_geteado)"""
import tkinter as tk
from tkinter import messagebox
import pandas as pd

def buscar_columna():
    # Obtener el nombre de la columna del Entry
    nombre_columna = entry_columna.get()

    try:
        df = pd.read_csv('socios.csv')  # Leer el archivo CSV
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo CSV")
        return
    
    # Buscar la posición de la columna
    if nombre_columna in df.columns:
        posicion = df.columns.get_loc(nombre_columna) + 1  # +1 para que sea basado en 1
        messagebox.showinfo("Resultado de la Búsqueda", f"La columna '{nombre_columna}' está en la posición: {posicion}")
    else:
        messagebox.showinfo("Resultado de la Búsqueda", f"No se encontró la columna '{nombre_columna}'")

# Configurar la interfaz tkinter
root = tk.Tk()
root.title("Buscar Columna en CSV")

# Campo de entrada para el nombre de la columna
entry_columna = tk.Entry(root)
entry_columna.pack(pady=10)
entry_columna.insert(0, 'Nombre de la Columna')  # Texto de ejemplo

# Botón para iniciar la búsqueda
btn_buscar = tk.Button(root, text="Buscar", command=buscar_columna)
btn_buscar.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
