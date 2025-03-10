import sqlite3

connect=sqlite3.connect("Ejercicio1.db")

cursor=connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(id_usuarios INTEGER PRIMARY KEY AUTOINCREMENT, nombre_usuario TEXT NOT NULL, telefono_usuario TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS productos(id_producto INTEGER PRIMARY KEY AUTOINCREMENT, nombre_producto TEXT NOT NULL, precio_producto FLOAT NOT NULL)")

#Registros de la tabla usuarios
cursor.execute('INSERT INTO usuarios(nombre_usuario, telefono_usuario) VALUES (?,?)',("Pepe", "123-456-7890"))
cursor.execute('INSERT INTO usuarios(nombre_usuario, telefono_usuario) VALUES (?,?)',("Sech", "123-456-7891"))

#Registros de la tabla productos
cursor.execute('INSERT INTO productos(nombre_producto, precio_producto) VALUES (?,?)',("Manzana", 12))
cursor.execute('INSERT INTO productos(nombre_producto, precio_producto) VALUES (?,?)',("Banana", 12.99))
cursor.execute('INSERT INTO productos(nombre_producto, precio_producto) VALUES (?,?)',("Durazno", 10.99))

#Guardar datos
connect.commit()
#Cerrar conexión
connect.close()