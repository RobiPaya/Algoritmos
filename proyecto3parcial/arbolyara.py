def arbol_navidad():
    altura = 7  # Puedes ajustar la altura del árbol aquí
    for i in range(altura):
        espacios = ' ' * (altura - i - 1)
        estrellas = '*' * (2 * i + 1)
        print(espacios + estrellas)
    
    # Tronco del árbol
    tronco = ' ' * (altura - 1) + '|'
    print(tronco)
# Llamar a la función para mostrar el árbol de Navidad
arbol_navidad()
