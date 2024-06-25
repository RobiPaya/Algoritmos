lista=["GOKUS","VEGETAS","KRILINS","FREEZERS","BULMAS"]
GOKUS=50
VEGETAS=40
KRILINS=1
FREEZERS=20
BULMAS=200
while True:
    opcion=input("").upper().split()
    for x in lista:
        if opcion[1] in x:
            opcion[1]=x
    print(opcion)

    if opcion=="":
        break


