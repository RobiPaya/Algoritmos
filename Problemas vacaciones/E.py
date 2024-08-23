lugar=0
costos=0
productos=int(input("Productos : "))
for hola in range(productos):
    lugar+=1
    costo=float(input(f"Costo del producto {lugar} :"))
    costos+=costo
print(costos)