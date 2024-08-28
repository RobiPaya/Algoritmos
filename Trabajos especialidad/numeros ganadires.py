import random
gandaira=random.randint(1,10)
listadegaandarores=[]
for x in range(gandaira):
    numero=random.randint(1,10000)
    listadegaandarores.append(numero)
    lies=sorted(listadegaandarores,key=lambda columna:columna[0])
    print(lies)