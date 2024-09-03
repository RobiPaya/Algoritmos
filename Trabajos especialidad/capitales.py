from estados import *
import random
erroress=[]
aciertos=0
errores=0
while True:
    posicion=random.randint(0,31)
    respuesta=input(f"Dame la capital de {estados1[posicion]}: ").title()
    if respuesta==estadosconcaptal[posicion]:
        estados1.remove(estados1[posicion])
        estadosconcaptal.remove(estadosconcaptal[posicion])
        aciertos+=1
    elif respuesta=="S":
        print(f"""Total de aciertos: {aciertos}\nTotal de errores:
              {errores}""")
        print("Tus errores fueron en")
        for x in errores:
            print(x)
        print("SALIDO")
        break
    else:
        erroress.append(estados1[posicion])
        errores+=1
