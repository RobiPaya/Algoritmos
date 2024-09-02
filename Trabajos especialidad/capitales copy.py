import random
from estados import *
sasa=0
corrrectas=0
incorrrectas=0
listadeya=[]
for x in range(10+sasa):
    posicion=random.randint(1,10)
    listadeya.append(posicion)
    hola=input(f"Capital de {estados1[posicion]}")
    if hola==estados1[posicion]:
        corrrectas+=1
    else:
        incorrrectas+=1
print(f"Correctas : {corrrectas}")
print(f"Incorrectas : {incorrrectas}")