from palabras import *
import random
adivina=""
palabra=random.choice(palabras)
tamañopalabra=len(palabra)
for x in range(tamañopalabra):
    adivina+="-"
print(adivina)
for x in range(6):
    letra=input("Dame una letra: ").lower()
    for x in range(len(palabra)):
        if palabra[x]==letra:
            adivina.replace(adivina[x],palabra[x])
    if not letra in palabra:
        print("esa letra es incorrecta")
        pass
if adivina==palabra:
    print("GANASTE")
else:
    print("PERDISTE")