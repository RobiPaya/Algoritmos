from palabras import *
import random
adivina=""
oportunidades=0
palabra=random.choice(palabras)
tamañopalabra=len(palabra)
for x in range(tamañopalabra):
    adivina+="-"
adivina1=adivina
while True:
    print(adivina)
    adivina=list(adivina)
    letra=input("Dame una letra: ").lower()
    for y in range(len(palabra)):
        if palabra[y]==letra:
            adivina[y]=letra
    if letra not in palabra:
        print("esa letra es incorrecta")
        oportunidades+=1
    else:
        if oportunidades==0:
            pass
        else:
            oportunidades-=1
    adivina1=""
    adivina1=adivina1.join(adivina)
    adivina=adivina1
    if oportunidades==6 or adivina==palabra:
        break
if adivina==palabra:
    print("GANASTE")
else:
    print("PERDISTE")