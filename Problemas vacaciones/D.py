entrada="""4
L
N
P
S
3
"""
cont=0
longitud=(len(entrada))
n=entrada[0]
z=entrada[longitud-2]
entrada=entrada.replace(n,"")
entrada=entrada.replace(z,"")
n=int(n)
z=int(z)
if z<0 or z>n:
    print("error")
else:
    entrada=entrada.split()
    escenario=entrada[z-1]
    for x in entrada:
        if x==escenario:
            pass
        else:
            entrada[cont]=x.replace(x,"x")
        cont+=1
    print(entrada)