from os import system
lista=[]
while True:
    system("cls")
    print("\tTIENDA DON CHUY")
    print('''
          A - Agregar
          B - Buscar
          E - Eliminar
          S - Salir''')
    opcion=input("Que opcion quieres: ")
    if opcion=="A":
        nombre=input("Nombre del producto: ")
        precio=input("Precio del producto: ")
        lista.append([nombre,precio])
        print("Agregando...")
    elif opcion=="E":
        borra=input("Que quieres borrar: ")
        for x in lista:
            if borra in x[0]:
                lista.remove(x)
                print("Borrando....")
        else:
            print("No se agrego")
    elif opcion=="B":
        busca=input("Que quieres buscar: ")
        for x in lista:
            if busca in x[0]:
                print(f"{x[0]:<15} - {x[1]}")
        else:
            print("No se enconto")
    elif opcion=="S":
        break
    else:
        print("Esa opcion no existe")
    input("Enter para continuar....")
