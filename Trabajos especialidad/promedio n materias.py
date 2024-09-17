def promedio(calificaciones):
    suma=0
    for x in calificaciones:
        suma+=x
    promedios=suma/len(calificaciones)
    return promedios
calificaciones=[]
materias=[]
while True:
    materia=input("QUe maTeira: ").capitalize()
    if not materia:
        promed=promedio(calificaciones)
        for x in range(len(calificaciones)):
            print(f"{materias[x]} - {calificaciones[x]}")
        print(f"Promedio {promed}")
    calificacion=int(input("Calif: "))
    materias.append(materia)
    calificaciones.append(calificacion)
    promed=promedio(calificaciones)
