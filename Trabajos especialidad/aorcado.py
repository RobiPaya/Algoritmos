from palabras import *
from os import system
import random
adivina=""
oportunidades=0
palabra=random.choice(palabras)
tamañopalabra=len(palabra)
for x in range(tamañopalabra):
    adivina+="-"
adivina1=adivina
while True:
    system("cls")
    print(pala)
    print(caca[oportunidades])
    print(f"\n{adivina}")
    adivina=list(adivina)
    letra=input("Dame una letra: ").lower()
    for y in range(len(palabra)):
        if palabra[y]==letra:
            adivina[y]=letra
    if letra not in palabra or not letra:
        oportunidades+=1
    adivina1=""
    adivina1=adivina1.join(adivina)
    adivina=adivina1
    if oportunidades==6 or adivina==palabra:
        break
imagen=random.randint(0,4)
if adivina==palabra:
    system("cls")
    print(pala)
    print(gane[imagen])
    print(f"GANASTE\n{palabra}")
else:
    system("cls")
    print(pala)
    print(perdi[imagen])
    print(f"PERDISTE\nLa palabra era {palabra}")