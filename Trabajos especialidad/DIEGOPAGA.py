import random
from os import system
lista=[]
paoga=random.randint(1,1000000000000)
camiapo=random.randint(1,paoga)
for x in range(4):
    lista.append(input("Nomrbe? : ").upper())
    system("cls")
print(f"PAGA: {random.choice(lista)} ${paoga}\nY LE DAN EL CAMBIO A DIEGO ☺ ${camiapo}")