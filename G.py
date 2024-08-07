listas=[]
lprecio=int(input("Precio de algodón de limón : "))
lfila=int(input("Personas en la fila de algodón de limón : "))
listas.append(lfila)
fprecio=int(input("Precio de algodón de fresa : "))
ffila=int(input("Personas en la fila de algodón de fresa : "))
listas.append(ffila)
while ffila==lfila:
    listas.remove(ffila)
    ffila=int(input("Personas en la fila de algodón de fresa : "))
    listas.append(ffila)
mprecio=int(input("Precio de algodón de menta : "))
mfila=int(input("Personas en la fila de algodón de menta : "))
listas.append(mfila)
while mfila==lfila or mfila==ffila:
    listas.remove(mfila)
    mfila=int(input("Personas en la fila de algodón de menta : "))
    listas.append(mfila)
minimo=(min(listas))
if minimo==lfila:
    if lprecio<=10:
        print("SI")
    else:
        print("NO")
if minimo==ffila:
    print("NO")
if minimo==mfila:
    if mprecio<=10:
        print("SI")
    else:
        print("NO")