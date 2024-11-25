import csv
suma=0
reprobados=0
with open("parcial.csv") as archivo:
     calificaciones = csv.reader(archivo)
     calif = []
     for alumno in calificaciones:
          if alumno[5] != "Calificacion":#[5] es el numero de columna donde esta la calificacion del alumno
            if float(alumno[5])<60.0:
                reprobados+=1
            suma+=float(alumno[5])
            calif.append(float(alumno[5]))
            if float(alumno[5])==min(calif):
                alumnomin=alumno[0]
                califmin=alumno[5]
print(suma/len(calif))
print(f"reprobados : {reprobados}")
print(f"aprobados : {len(calif)-reprobados}")
print(f"Calificación más alta : {alumno[0]} {alumno[5]}")
print(f"Calificación más baja : {alumnomin} {califmin}")