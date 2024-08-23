entrada='''10 4 6
0 0 5 8 1 0
0 0 0 0 0 9
2 0 0 0 0 2
0 2 0 1 2 0
'''.split()
vacio=0
derrame=0
h=int(entrada[0])
l=int(entrada[1])
w=int(entrada[2])
entrada.remove(entrada[0])
entrada.remove(entrada[0])
entrada.remove(entrada[0])
water=h*l*w
for x in entrada:
    i=int(x)
    if i==0:
        vacio+=1
    else:
        derrame+=i
print(water-derrame)
print(derrame)
print(vacio)