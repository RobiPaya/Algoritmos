#una escuela necesita registrar la informacion de sus estudiantes y los cursos que cada uno toma debes construir una base de datos en sqlite para organizar 

#crea una base de datos llamada (academia.db)
# crear dos tablas:estudiantes:debes tener al menos los campos id nombre, edad y carrera.
#incertar 5 regegistros en cada tabla con datos academicos validos 

#realizar las sig. 8 consusltas en sqlite     
#1 mostrar todos los regitros de la tabla estudiantes
#2 mostrar todos los registros de la tabla cursos
#3 mostrar los estudiantes cuya edad sea mayor o igual 21
#4 contar cuantos cursos hay en total 
#5 calcular el promedio de calificaciones de todos los cursos
#6 actualizar la calificacion  de un curso espec ifico(debes elegir cual)
#7  mostrar los estudiantes ordenados alfabeticamente por nombre
#8 realizar una consulta con inner join que muestre:nombre del estudiante,nombre del curso y calificacion 


import sqlite3
from tabulate import *

#crea una base de datos llamada (academia.db)
connect = sqlite3.connect("academia.db")
cursor = connect.cursor 

cursor.execute("""CREATE TABLE IF NOT EXISTS academia
                (id_estudiantes INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre estudiantes TEXT NOT NULL,
                edad DATE NOT NULL,
                carrera TEXT NOT NULL)""")

# crear dos tablas:estudiantes:debes tener al menos los campos id nombre, edad y carrera.
cursor.execute('CREATE TABLE IF NOT EXISTS estudiantes'
                '(id_estudiantes INTEGER PRIMARY KEY AUTOINCREMENT,'
                'id_nombre INTEGER NOT NULL,'
                'edad TEXT NOT NULL,'
                'carreras INTEGER NOT NULL,'
                'FOREIGN KEY (id_nombre) REFERENCES carreras(id_nombre))')

#incertar 5 regegistros en cada tabla con datos academicos validos 
cursor.execute('INSERT INTO estudiantes (nombre, edad carrera) VALUES' 
                '("dulce",21,"arquitectura"),'
                '("susana",22,"pintura"),'
                '("ayli",21,"odontologia"),'
                '("fer",23,"doctore"),'
                '("luis",24,"maestre"),')

cursor.execute('INSERT INTO (id_estudiante, nombre, edad, curso)'
'(1, "dulce", 21, a1),'
'(2,"susana",22, b3),'
'(3,"ayli",21, b8),'
'(4,"fer",23, d3),'
'(5,"luis",24, a5)')

# crear dos tablas:
cursor.execute('CREATE TABLE IF NOT EXISTS curso'
                '(id_curso INTEGER PRIMARY KEY AUTOINCREMENT,'
                'id_nombre INTEGER NOT NULL,'
                'estudiante TEXT NOT NULL,'
                'carreras INTEGER NOT NULL,'
                'FOREIGN KEY (id_estudiante) REFERENCES curso (id_estudiante))')

cursor.execute('INSERT INTO cursos (id_carrera, carrera, curso) VALUES' 
                '("arquitectura",a1),'
                '("pintura",b3),'
                '("odontologia",b8),'
                '("doctor",d3),'
                '("maestre",a5),')

cursor.execute('INSERT INTO (id_estudiante, nombre, edad, curso)'
'(1, "dulce", 21, a1),'
'(2,"susana",22, b3),'
'(3,"ayli",21, b8),'
'(4,"fer",23, d3),'
'(5,"luis",24, a5)')


cursor.execute("""SELECT nombre_estudiante, """)






cursor.commit()
cursor.close()

