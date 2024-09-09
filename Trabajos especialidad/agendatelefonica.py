from os import system

lista=[]
while True:
    system("cls")
    print('''\tAgenda''')
    print('''A-Agregar\nM-Mostrar\nBO-Borrar\nBU-Buscar\nS-Salir''')
    opcion=input("DAME LA OPCION QUE QUIERES: ").upper()
    if opcion=="S":
        break
    elif opcion=="A":
        nombre=input("Nombre: ").title()
        numero=input("Numero de telefono: ").replace(" ","-")
        lista.append([nombre,numero])
    elif opcion=="M":
        for x in lista:
            print(f"{x[0]:<10} - {x[1]:>5}")
    elif opcion=="BO":
        borrador=input("Cuál vas a matar : ").title()
        for x in lista:
            if x[0]==borrador:
                lista.remove(x)
                print("borrado")
        else:
            print("No encontrado")
    elif opcion=="BU":
        buscar=input("Quien BUSCAR: ").title()
        for x in lista:
            if buscar in x[0]:
                print(f"{x[0]:<10} - {x[1]:>5}")
            else:
                print("No se encuentra esa persona")
    else:
        print("ESA OPCION NO EXISTE")
    input("Enter para continuar...")