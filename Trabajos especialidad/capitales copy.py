import random
from estados import *
sasa=0
corrrectas=0
incorrrectas=0
hola2=0
listadeya=[]
for x in range(10+sasa):
    posicion=random.randint(1,10)
    if posicion in listadeya:
        sasa+=1
        print("ohl")
        continue
    listadeya.append(posicion)
    hola=input(f"Capital de {estados1[posicion]} : ").title()
    for x in estados1:
        if hola in x:
            hola=x
    if hola==estados1[posicion]:
        corrrectas+=1
        print("Correcta")
    else:
        incorrrectas+=1
        print("Incorrecta")
print(f"Correctas : {corrrectas}")
print(f"Incorrectas : {incorrrectas}")