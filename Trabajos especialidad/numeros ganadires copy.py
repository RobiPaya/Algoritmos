lista=[]
bole=int(input("Cuantos boletos:"))
for x in range(bole):
    numeros=input("Dame los numeros:")
    lista.append(numeros)
lista.sort()
for x in lista:
    print(x)