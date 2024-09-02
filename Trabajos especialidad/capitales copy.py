import random
from estados import *
sasa=0
corrrectas=0
incorrrectas=0
hola2=0
listadeya=[]
for x in range(10+sasa):
    posicion=random.randint(1,10)
    listadeya.append(posicion)
    hola=input(f"Capital de {estados1[posicion]} : ").title()
    for x in estadosconcaptal:
        if x in hola:
            hola2=x
    if hola2==estados1[posicion]:
        corrrectas+=1
        print("Correcta")
    else:
        incorrrectas+=1
print(f"Correctas : {corrrectas}")
print(f"Incorrectas : {incorrrectas}")