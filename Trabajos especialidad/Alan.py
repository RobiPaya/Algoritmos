listasasa=[]
a="cac"
while a!="caca":
    caca="""Ccaca
    C - Agragar calificaciones
    B - Buscar calificaciones
    K - Borro cacali
    S - Salir de las calificaones""".upper()
    if caca=="S":
        a+="a"
    elif caca=="C":
        materia=input("Matewria : ")
        if materia in listasasa:
            print("Yata")
            continue
        klifia=input(f"Calfifcacíon de {materia} : ")
        listasasa.append([materia,klifia])
    elif caca=="B":
        buscardo=input("Cual vsa a buscar : ")
        for x in listasasa:
            if buscardo in x[0]:
                print(x[0],x[1])
            else:
                print("No hay de esa materia")
    elif caca=="K":
        borrador=input("Cual vas a borara : ")
        for x in listasasa:
            