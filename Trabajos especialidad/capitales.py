from estados import *
import random
respuestas=[]
posiciones=[]
for x in range(10):
    posicion=random.randint(0,31)
    posiciones.append(posicion)
    for x in posiciones:
        if x==posicion:
            posicion=random.randint(0,31)
    respuesta=input(f"Dame la capital de {estados1[posicion]}: ").title()
    if respuesta==estadosconcaptal[posicion]:
        respuestas.append(respuesta+" Correcta")
    else:
        respuestas.append(respuesta+" incorrecta")

print(respuestas)