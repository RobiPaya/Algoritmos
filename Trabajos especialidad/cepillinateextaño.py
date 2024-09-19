cadena=input("Dame cosas : ")
diccionario={}
for x in (cadena):
    if x in diccionario:
        diccionario[x]+=1
    else:
        diccionario[x]=1
for x in diccionario:
    print(f"{x} : {diccionario.get(x)}")