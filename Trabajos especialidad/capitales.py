from estados import *
import random
respuestas=[]
posiciones=[]
for x in range(10):
    posicion=random.randint(1,len(estados1))
    posiciones.append(posicion)
    for x in posiciones:
        if x==posicion:
            posicion=random.randint(1,len(estados1))
    respuesta=input(f"Dame la capital de {estados1[posicion]}: ")
    if respuesta==estadosconcaptal[posicion]:
        respuestas.append(respuesta+" Correcta")
    else:
        respuestas.append(respuesta+" incorrecta")

print(respuestas)




