import random
from estados import *
sasa=0
corrrectas=0
incorrrectas=0
listadecorrectas=[]
while True:
    posicion=random.randint(1,len(estados1))
    print(posicion)
    hola=input(f"Capital de {estados1[posicion]} : ").title()
    estados1.remove(estados1[posicion])
    for x in estados1:
        if hola in x:
            hola=x
    if hola==estados1[posicion]:
        corrrectas+=1
        print("Correcta")
    else:
        incorrrectas+=1
        print("Incorrecta")
        listadecorrectas.append(estados1[posicion])
    if hola=="Salir":
        break
    elif len(estados1)==0:
        print("Ya se acabaron")
        break
print(f"Correctas : {corrrectas}")
print(f"Incorrectas : {incorrrectas}")
print("Debes estudiar estas capitales : \n")
for x in listadecorrectas:
    print(x)