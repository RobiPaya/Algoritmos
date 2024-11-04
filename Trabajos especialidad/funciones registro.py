def limpiar():
    nombre_entrada.delete(0,len(nombre_entrada.get()))
    direccion_entrada.delete(0,len(direccion_entrada.get()))
    telefono_entrada.delete(0,len(telefono_entrada.get()))
    saldo_entrada.delete(0,len(saldo_entrada.get()))
def guardar():
    lista=[]
    nombre=nombre_entrada.get()
    direccion=direccion_entrada.get()
    telefono=telefono_entrada.get()
    saldo=saldo_entrada.get()
    try:
        with open("clientes.json","r") as archivo:
            for x in archivo:
                lista.append(x)
            lista=sorted(lista,key=lambda columna:columna[0], reverse=True)
            ultimocliente=int(lista[0])
            nuevocliente=ultimocliente+1
    except:
        nuevocliente=1
    datos={nuevocliente:{"nombre":nombre,"direccion":direccion,"telefono":telefono,"saldo":saldo}}
    try:
        with open("clientes.json","r") as archivo:
            data=js.load(archivo)
            data.update(datos)
    except:
        with open("reporte.json","w") as archivo:
                js.dump(data,archivo,indent=4)
            


