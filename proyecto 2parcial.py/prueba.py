import csv
sumacalif=0
reprobados=0
cont=0
with open("parcial.csv","r") as archivo:
     calificaciones = csv.reader(archivo)
     print(calificaciones)
     calif = []
     for alumno in calificaciones:
          if alumno[5] != "Calificacion":     #[5] es el numero de columna donde esta la calificacion del alumno
               calif.append(float(alumno[5]))
               if float(alumno[5])==max(calif):
                    malto=alumno[0]
               if float(alumno[5])==min(calif):
                    mameno=alumno[0]
for x in calif:                                                              
     sumacalif+=x
     cont+=1
     if x<60:
          reprobados+=1
print(sumacalif/cont,reprobados,len(calif)-reprobados,malto,max(calif),mameno,min(calif))