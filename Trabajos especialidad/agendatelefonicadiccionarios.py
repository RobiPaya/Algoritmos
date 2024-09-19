from os import system
lista={}
while True:
    system("cls")
    print('''\tAgenda''')
    print('''A-Agregar\nM-Mostrar\nBO-Borrar\nBU-Buscar\nS-Salir''')
    opcion=input("DAME LA OPCION QUE QUIERES: ").upper()
    if opcion=="S":
        break
    elif opcion=="A":
        nombre=input("Nombre: ").title()
        if nombre in lista:
            print("Yata")
            print(f"Su numero : {numero}")
        else:
            numero=input("Numero de telefono: ").replace(" ","-")
            lista[nombre]=numero
    elif opcion=="M":
        for x in lista:
            print(f"Nombre : {x} Número : {lista.get(x)}")
    elif opcion=="BO":
        borrador=input("Cuál vas a matar : ").title()
        if borrador in lista:
            lista.pop(borrador)
            print("borrado")
        else:
            print("No encontrado")
    elif opcion=="BU":
        buscar=input("Quien BUSCAR: ").title()
        for x in lista:
            if buscar in x:
                print(f"Nombre : {x} Número : {lista.get(x)}")
            else:
                print("No se encuentra esa persona")
    else:
        print("ESA OPCION NO EXISTE")
    input("Enter para continuar...")