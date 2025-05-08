import matplotlib.pyplot as plt  # Importamos la librería para hacer gráficos

# Definir los nombres de los estudiantes y sus calificaciones
estudiantes = ["Ana", "Carlos", "María", "José", "Elena"]
matematicas = [85, 70, 90, 60, 75]  # Calificaciones de matemáticas
ciencia = [80, 75, 95, 65, 70]  # Calificaciones de ciencia

# Crear el gráfico
plt.figure(figsize=(8, 5))  # Definir el tamaño del gráfico

# Dibujar las líneas de calificaciones
plt.plot(estudiantes, matematicas, marker="o")  # Línea azul con círculos
plt.plot(estudiantes, ciencia, marker="s")  # Línea verde con cuadrados

# Añadir títulos y etiquetas
plt.xlabel("Estudiantes")  # Etiqueta del eje X
plt.ylabel("Calificaciones")  # Etiqueta del eje Y
plt.title("Comparación de calificaciones en Matemáticas y Ciencia")  # Título del gráfico
# Mostrar el gráfico
plt.show()