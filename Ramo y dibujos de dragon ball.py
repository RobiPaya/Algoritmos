def ramo_y_sus_dibujos():
    print("\tDibujos de dragon ball\n")
    print('''    goku --- 50
    vegeta --- 40
    krilin --- 1
    frezeer --- 20
    bulma --- 200\n''')
    total_dinero=0
    while True:
        personaje=str(input("Que compras:")).upper().strip(" ")
        if personaje=="SALIR":
            break
        personaje = personaje.rstrip('S')
        cantidad=int(input("Cantidad:"))
        
        if personaje=="GOKU":
            total_dinero+=50*cantidad
        if personaje=="VEGETA":
            total_dinero+=40*cantidad
        if personaje=="KRILIN":
            total_dinero+=1*cantidad
        if personaje=="FREZZER":
            total_dinero+=20*cantidad
        if personaje=="BULMA":
            total_dinero+=200*cantidad
        if not personaje:
            print("Error")
    
    print("\n")
    print(f"El total de ganancias fue de: ${total_dinero}")
    print(f"La multa del SAT es de: ${total_dinero*3}")
    print(f"La deuda final es de: ${total_dinero*3-total_dinero}")

ramo_y_sus_dibujos()