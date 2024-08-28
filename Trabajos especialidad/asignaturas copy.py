lista=[]
lamba=int(input("cua´tants materisa' : "))
for x in range(lamba):
    asignaturas=input("ASIGNATURA?:").capitalize()
    calificacion=int(input("CALIFICACION?:"))
    lista.append([asignaturas,calificacion])
for x in lista:
    print(f"En {x[0]} sacaste {x[1]} de calificacion")