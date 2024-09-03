from estados import *
import random
erroress=[]
respuesta=""
aciertos=0
errores=0
while True:
    if len(estados1)==0 or respuesta=="S":
        break
    posicion=random.randint(0,len(estados1)-1)
    respuesta=input(f"Dame la capital de {estados1[posicion]}: ").title()
    if respuesta==estadosconcaptal[posicion]:
        estados1.remove(estados1[posicion])
        estadosconcaptal.remove(estadosconcaptal[posicion])
        aciertos+=1
    else:
        erroress.append([estados1[posicion],estadosconcaptal[posicion]])
        errores+=1
        estados1.remove(estados1[posicion])
        estadosconcaptal.remove(estadosconcaptal[posicion])
print(f"""Total de aciertos: {aciertos}\nTotal de errores:
        {errores}""")
print("Tus errores fueron en")
for x in erroress:
    print(f"{x[0]} la respuesta es {x[1]}")
print("SALIDO")
