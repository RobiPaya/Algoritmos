diccionario={}
lista=[]
calificacion=0
alumnos=int(input("Cuantos alumnos son: "))
for x in range(alumnos):
    lista.clear()
    nombre=input("Dame tu nombre: ").title()
    while calificacion>=0:
        calificacion=float(input("Dame tu calificaion: "))
        if calificacion>=0:
            lista.append(calificacion)
    calificacion=0
    diccionario.update({nombre:lista})
for x in diccionario:
    print(x)
    notas=diccionario.get(x)
    for x in notas:
        print(x)
