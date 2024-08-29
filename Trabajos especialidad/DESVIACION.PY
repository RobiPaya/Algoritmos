import math
total=0
cont=0
desviacion=0
NUMEROS=input("Numeros: ").replace(","," ").split()
for x in NUMEROS:
    y=int(x)
    total+=y
    cont+=1
media=total/cont
for x in NUMEROS:
    y=int(x)
    desviacion+=(y-media)**2
tipica=math.sqrt(desviacion/cont)
print(f"La media es de {media} y la desviacion tipica es de {tipica:.2f}")