import sqlite3

connect = sqlite3.connect("Biblioteca.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS libros
(id_libros INTEGER PRIMARY KEY AUTOINCREMENT,
titulo_libro TEXT NOT NULL,
año_publicacion DATE NOT NULL)""")

cursor.execute("CREATE TABLE IF NOT EXISTS autores(id_autor INTEGER PRIMARY KEY AUTOINCREMENT,"
"nombre_autor TEXT NOT NULL,"
"nacionalidad_autor TEXT NOT NULL)")

cursor.execute("CREATE TABLE IF NOT EXISTS categorias(id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,"
"nombre_categoria TEXT NOT NULL)")

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(id_usuario INTEGER PRIMARY KEY AUTOINCREMENT," "correo_usuario TEXT NOT NULL," "telefono_usuario TEXT NOT NULL)")

#Insertaciones de la tabla libros
cursor.execute('INSERT INTO libros(titulo_libro, año_publicacion) VALUES '
'("Cien años de soledad","1967-06-05"),'
'("Don Quijote de la Mancha","1605-01-16"),'
'("Orgullo y prejuicio","1813-01-21"),'
'("La sombra del viento","2001-06-17"),'
'("El extranjero","1942-05-19")')

#Inserts in la table autores
cursor.execute("INSERT INTO autores(nombre_autor, nacionalidad_autor) VALUES (?,?)", ("Gabriel García Márquez","Colombiana"))
cursor.execute("INSERT INTO autores(nombre_autor, nacionalidad_autor) VALUES (?,?)", ("Miguel de Cervantes","Española"))
cursor.execute("INSERT INTO autores(nombre_autor, nacionalidad_autor) VALUES (?,?)", ("Jane Austen","Británica"))
cursor.execute("INSERT INTO autores(nombre_autor, nacionalidad_autor) VALUES (?,?)", ("Carlos Ruiz Zafón","Española"))
cursor.execute("INSERT INTO autores(nombre_autor, nacionalidad_autor) VALUES (?,?)", ("Albert Camus","Francesa"))

#INSERT INTO usuarios
cursor.execute("INSERT INTO usuarios(correo_usuario, telefono_usuario) VALUES(?, ?)", ("Usuario1@gmail","821-324-1245"))
cursor.execute("INSERT INTO usuarios(correo_usuario, telefono_usuario) VALUES (?, ?)", ("Usuario0@gmail", "821-324-1245"))
cursor.execute("INSERT INTO usuarios(correo_usuario, telefono_usuario) VALUES (?, ?)", ("Usuario2@gmail", "539-124-7342"))
cursor.execute("INSERT INTO usuarios(correo_usuario, telefono_usuario) VALUES (?, ?)", ("Usuario3@gmail", "463-634-3245"))
cursor.execute("INSERT INTO usuarios(correo_usuario, telefono_usuario) VALUES (?, ?)", ("Usuario4@gmail", "567-325-1256"))

#Metida en la tabla categorias
cursor.execute("INSERT INTO categorias(nombre_categoria) VALUES (?)", ("Realismo mágico, Literatura latinoamericana",))
cursor.execute("INSERT INTO categorias(nombre_categoria) VALUES (?)", ("Clásico, Novela de caballería, Parodia",))
cursor.execute("INSERT INTO categorias(nombre_categoria) VALUES (?)", ("Romance, Literatura clásica, Crítica social",))
cursor.execute("INSERT INTO categorias(nombre_categoria) VALUES (?)", ("Misterio, Drama histórico, Literatura contemporánea",))
cursor.execute("INSERT INTO categorias(nombre_categoria) VALUES (?)", ("Existencialismo, Filosofía, Literatura moderna",))


#Updatear los datos
"""cursor.execute("UPDATE libros SET titulo_libro = ? WHERE id_libro=?", ("100 años de soledad",1))
cursor.execute("UPDATE autores SET nombre_autor = ? WHERE id_autor = ?"("Miguelito de Cervantes",2))
cursor.execute("UPDATE categorias SET nombre_categoria = ? WHERE id_categoria = ?"("Literatura",3))
cursor.execute("UPDATE usuarios SET correo_usuario = ? WHERE id_usuario = ?"("gmail@gmail.com",4))"""

#Eliminación de datos
cursor.execute("DELETE FROM libros WHERE titulo_libro = 'Orgullo y prejuicio' ")
cursor.execute("DELETE FROM autores WHERE nombre_autor = 'Jane Austen' ")
cursor.execute("DELETE FROM categorias WHERE nombre_categoria= 'Literatura' ")
cursor.execute("DELETE FROM usuarios WHERE correo_usuario = 'Usuario5@gmail.com' ")

#Verición de tablas
cursor.execute("SELECT * FROM libros")
tabla=cursor.fetchall()
print("Tabla libros")
for x in tabla:
    print(x)

cursor.execute("SELECT * FROM autores")
tabla=cursor.fetchall()
print("\nTabla autores")
for x in tabla:
    print(x)

cursor.execute("SELECT * FROM categorias")
tabla=cursor.fetchall()
print("\nTabla categorias")
for x in tabla:
    print(x)

cursor.execute("SELECT * FROM usuarios")
tabla=cursor.fetchall()
print("\nTabla usuarios")
for x in tabla:
    print(x)

print("\nTablas ordenadas")

#Ordenar datos
cursor.execute('SELECT * FROM libros ORDER BY año_publicacion ASC')
ordenado=cursor.fetchall()
print("\n")
for x in ordenado:
    print(x)

cursor.execute('SELECT * FROM autores ORDER BY nacionalidad_autor ASC')
ordenado=cursor.fetchall()
print("\nTabla de autores ordenada en orden ascendente por su nacionalidad\n")
for x in ordenado:
    print(x)

cursor.execute('SELECT * FROM categorias ORDER BY nombre_categoria ASC')
ordenado=cursor.fetchall()
print("\nTabla de categorias ordenada en orden ascendente por su nombre\n")
for x in ordenado:
    print(x)

cursor.execute('SELECT * FROM usuarios ORDER BY correo_usuario ASC')
ordenado=cursor.fetchall()
print("\nTabla de usuarios ordenada en orden ascendente por su correo\n")
for x in ordenado:
    print(x)

#Contar registros
cursor.execute('SELECT COUNT (*) FROM usuarios')
print(f"\nNúmero de registros en la tabla usuarios : {cursor.fetchone()[0]}")

cursor.execute('SELECT COUNT (*) FROM autores')
print(f"\nNúmero de registros en la tabla autores : {cursor.fetchone()[0]}")

cursor.execute('SELECT COUNT (*) FROM categorias')
print(f"\nNúmero de registros en la tabla usuarios : {cursor.fetchone()[0]}")

cursor.execute('SELECT COUNT (*) FROM libros')
print(f"\nNúmero de registros en la tabla usuarios : {cursor.fetchone()[0]}")

#Buscar patrones
cursor.execute('SELECT * FROM usuarios WHERE correo_usuario LIKE "%gmail%"')
like=cursor.fetchall()
print(f"\nNúmero de coincidencias de 'gmail' de correo_usuario en la tabla usuarios: {len(like)}")

cursor.execute("SELECT COUNT(*) FROM libros WHERE año_publicacion > '1950-01-01'")
resultado = cursor.fetchone()
print(f"\nNúmero de coincidencias de año de publicación en la tabla libros: {resultado[0]}")


# Guardar datos
connect.commit()
# Cerrar conexión
connect.close()