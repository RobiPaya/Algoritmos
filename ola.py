#almacenar asignaturas de un curso (mate,fisica,historia,ertc) en una lista y la muestre en la pantalla
from os import system
system('cls')
lista=[]
cal=[]
rep=[]
bien=[]
no=int(input('Número de materias ??: '))

for x in range(no):
    materia=input('Nombre de la asignatura : ').upper()
    
    calif=int(input('calificacion? :'))
    lista.append(materia)
    cal.append(calif)
    ola=(f'EN {lista[x]} SACASTE {cal[x]}')
    bien.append(ola)
    if cal[x]<=5:
        rep.append(ola)

print(f'''     CALIFICACIONES:
     {bien}''')
print(f'''
      TIENES QUE RECUSRAR :
      {rep}
''')

im nothing like y'all 😎😎😭😭🐠💧🌊🌊🐠🐠
