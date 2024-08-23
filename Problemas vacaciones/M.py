entrada='''7
5 0 2 1 1 1 5
'''.split()
ocupado=0
cantidad=int(entrada[0])
entrada.remove(entrada[0])
k1=entrada[0]
longi=int(max(entrada))
if cantidad>10000 or cantidad<3:
    print("error")
else:
    total=longi*cantidad
    for x in range(0,len(entrada)):
        y=int(entrada[x])
        if y<0:
            print("error")
            break
        if x==len(entrada)-1:
            if k1!=entrada[x]:
                print("error")
                break
        ocupado+=y
    print(total-ocupado)