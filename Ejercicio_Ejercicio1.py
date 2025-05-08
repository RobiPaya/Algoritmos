import sqlite3

connect = sqlite3.connect("Ejercicio_estudiantes_cursos_foarignesnkey.db")
cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS estudiantes'
'(id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,'
'nombre_estudiante TEXT NOT NULL,'
'edad_estudiante INTEGER NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS cursos'
'(id_curso INTEGER PRIMARY KEY NOT NULL,'
'id_estudiante INTEGER NOT NULL,'
'nombre_curso TEXT NOT NULL,'
'FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante))')

cursor.execute('INSERT INTO estudiantes(nombre_estudiante, edad_estudiante) VALUES'
'("Mauricio", 1),'
'("Profesor", 56),'
'("Trapinch", 3),'
'("Sudowoodo", 42),'
'("Arturo", 865)')

cursor.execute('INSERT INTO cursos(id_estudiante, nombre_curso) VALUES'
'(1,"Matemáticas"),'
'(2, "Español"),'
'(3, "Fisica"),'
'(4, "Deportividad acertiva"),'
'(5, "Mauricidad complitiva")')

consulta = '''
SELECT estudiantes.nombre_estudiante, cursos.nombre_curso, estudiantes.edad_estudiante
FROM estudiantes
INNER JOIN cursos
ON estudiantes.id_estudiante = cursos.id_estudiante
'''

#Consulatar
cursor.execute(consulta)
resultados = cursor.fetchall()

# Mostrar los resultados
for x in resultados:
    print(f"Estudiante: {x[0]}, Edad: {x[2]}, Curso: {x[1]}")

# Guardar datos
connect.commit()
# Cerrar conexión
connect.close()