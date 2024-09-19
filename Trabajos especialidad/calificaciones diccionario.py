diccionario={}
lista=[]
calificacion=0
alumnos=int(input("Cuantos alumnos son: "))
for x in range(alumnos):
    nombre=input("Dame tu nombre: ").title()
    while calificacion>=0:
        materia=input("Dame materia: ")
        calificacion=float(input("Dame tu calificaion: "))
        lista.append([materia,calificacion])
    diccionario[nombre]={lista}
    lista.clear()

for x in diccionario:
    print(x)
    notas=diccionario.get(x)
    for x in notas:
        print(x[0],x[1])
