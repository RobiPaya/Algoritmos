import csv

with open("parcial.csv","r") as archivo:
     calificaciones = csv.reader(archivo)
     calif = []
     for alumno in calificaciones:
          if alumno[5] != "Calificación":     #[5] es el numero de columna donde esta la calificacion del alumno
               calif.append(float(alumno[5]))
print(calif)