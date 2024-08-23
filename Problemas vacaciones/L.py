entrada='''6
1.5
15
0.5
15
3
20
1.2
10
0.7
10
1.8
7
'''
volumenes=0
pesos=0
bolsas=0
entrada=entrada.replace(entrada[0],"")
entrada=entrada.split()
for x in range(0,len(entrada),2):
    peso=float(entrada[x])
    volumen=int(entrada[x+1])
    volumenes+=volumen
    pesos+=peso
    if pesos>=5 or volumenes>=40:
        volumenes=0
        pesos=0
        volumenes+=volumen
        pesos+=peso
        bolsas+=1
    if x==len(entrada)-2:
        if volumenes==0 or pesos==0:
            pass
        else:
            bolsas+=1
print(bolsas)