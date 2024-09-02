import random
from estados import *
sasa=0
corrrectas=0
listadeya=[]
for x in range(10+sasa):
    posicion=random.randint(1,10)
    listadeya.append(posicion)
    if posicion in listadeya:
        sasa+=1
        continue
    print("osao")