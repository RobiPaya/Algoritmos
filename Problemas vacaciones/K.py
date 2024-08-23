lista=[]
x=0
lugar=0
niñasaltas=0
niñosaltos=0
niños=int(input("Número de niños que van al viaje : "))
if niños%2==0:
    niñes=int(niños/2)
    for estatuniñas in range(niñes):
        lugar+=1
        estaturaniñas=float(input(f"Estatura de la niña {lugar} : "))
        lista.append(estaturaniñas)
        estaturaniños=float(input(f"Estatura del niño {lugar} : "))
        lista.append(estaturaniños)
        minimo=min(lista)
        print(minimo)
        if minimo==estaturaniños:
            niñasaltas+=1
        if minimo==estaturaniñas:
            niñosaltos+=1
        lista.remove(estaturaniñas)
        lista.remove(estaturaniños)
else:
    print("Otra vez")
print(niñasaltas)
print(niñosaltos)