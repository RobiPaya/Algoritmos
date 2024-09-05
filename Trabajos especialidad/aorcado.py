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
if adivina==palabra:
    system("cls")
    print(f"GANASTE\n{palabra}")
    print(caca[oportunidades])
else:
    system("cls")
    print(caca[6])
    print(f"PERDISTE\nLa palabra era {palabra}")