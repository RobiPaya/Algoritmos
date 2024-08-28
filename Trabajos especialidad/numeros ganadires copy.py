lista=[]
bole=int(input("Cuantos boletos:"))
for x in range(bole):
    numeros=input("Dame los numeros:")
    lista.append(numeros)
lista=sorted(lista,key=lambda columna:columna[0])
for x in lista:
    print(x)