import sqlite3

connect = sqlite3.connect("Hospital.db")
cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS pacientes'
'(id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,'
'nombre_paciente TEXT NOT NULL,'
'edad_paciente INTEGER NOT NULL,'
'genero_paciente TEXT NOT NULL,'
'telefono_paciente TEXT)')

cursor.execute('CREATE TABLE IF NOT EXISTS especialidades'
'(id_especialidad INTEGER PRIMARY KEY AUTOINCREMENT,'
'nombre_especialidad TEXT NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS doctores'
'(id_doctor INTEGER PRIMARY KEY AUTOINCREMENT,'
'id_especialidad INTEGER NOT NULL,'
'nombre_doctor TEXT NOT NULL,'
'telefono_doctor TEXT NOT NULL,'
'FOREIGN KEY (id_especialidad) REFERENCES especialidades(id_especialidad))')

cursor.execute('CREATE TABLE IF NOT EXISTS citas'
'(id_citas INTEGER PRIMARY KEY AUTOINCREMENT,'
'id_paciente INTEGER NOT NULL,'
'id_doctor INTEGER NOT NULL,'
'fecha_cita DATE NOT NULL,'
'hora_cita TIME NOT NULL,'
'FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),'
'FOREIGN KEY (id_doctor) REFERENCES doctores(id_doctor))')

#Insertaciones
cursor.execute('INSERT INTO pacientes'
'(nombre_paciente, edad_paciente, genero_paciente, telefono_paciente) VALUES'
'("Mauricio Arturo Angulo Palomino", 1, "Masculino", "625-123-7915"),'
'("Enter Delete Tab", 132, "Prefiero no decirlo", NULL)')

cursor.execute('INSERT INTO especialidades'
'(nombre_especialidad) VALUES'
'("Dr. Chapatín"),'
'("Plastilina")')

cursor.execute('INSERT INTO doctores'
'(id_especialidad, nombre_doctor, telefono_doctor) VALUES'
'(1, "Mauricio", "332-345-7521"),'
'(2, "Mauricio 2", "Mauri_celular@gmail.com")')

cursor.execute('INSERT INTO citas'
'(id_paciente, id_doctor, fecha_cita, hora_cita) VALUES'
'(1, 1, "2025-03-13", "18:00"),'
'(2, 1, "2025-06-15", "15:00")')

#Mostración
cursor.execute('SELECT * FROM citas')
datos=cursor.fetchall()
print("\nVista de la tabla citas\n")
for x in datos:
    print(x)

cursor.execute('SELECT * FROM pacientes')
datos=cursor.fetchall()
print("\nVisualización de la tabla pacientes\n")
for x in datos:
    print(x)

cursor.execute('SELECT * FROM especialidades')
datos=cursor.fetchall()
print("\nDemo stración de la tabla especialidades\n")
for x in datos:
    print(x)

cursor.execute('SELECT * FROM doctores')
datos=cursor.fetchall()
print("\nPrint de la tabla doctores\n")
for x in datos:
    print(x)

# Guardar datos
connect.commit()
# Cerrar conexión
connect.close()