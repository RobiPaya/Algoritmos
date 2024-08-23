seg=int(input("Cuántos segundos cantas las sirenas? : "))
hola=0
lista=[]
for x in range(seg):
    hola+=1
    for x in range(hola):
        lista.append("a")
    lista.append("h")
for x in lista:
    print(x, end="") 