import pandas as pd
datos=pd.read_csv("parcial.csv")
print(f"Candtidad de alumnos : {datos.NOMBRE.count()}")
print(f"Promedio del grupo : {datos.Calificacion.mean()}")
print(f"Alumno con la calif mas alta : {datos}: {datos.Calificacion.max()}")
