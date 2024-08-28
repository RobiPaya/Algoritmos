import random
lista=[]
listya=[]
a=0
lamba=int(input("cua´tants materisa' : "))
for x in range(lamba):
    calificacaiopn=random.randint(0,10)
    asignaturas=input("ASIGNATURA?:").capitalize()
    lista.append(asignaturas)
    listya.append(calificacaiopn)
for x in lista:
    print(f"{x} - {listya[a]}")
    a+=1
