from os import system
system ('cls')
print('¡¡¡tienes q pesar mas de 50, menos de 120 e ingresar un numero mayor de 0 en Cianuro.!!!\n')
kg=int(input('Cuánto pesas? :'))
cianuro=int(input('cuanto  cianuro ? :'))
if kg>50 or kg<120:
    input('continuar...')
    if cianuro>0:
        if cianuro>=kg*3:
            hola=cianuro-kg*3
            print(f'quitale {hola} y es seguro esoo')
            print('mucho cianuro, te mueres 😭')
        else:
            print('cometela')
else:
    print('No puedes, el peso debe ser mayor a 50 y menor a 120.El cianuro tiene que ser mayor a 0')
