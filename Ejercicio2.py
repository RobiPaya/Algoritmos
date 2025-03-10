import sqlite3

connect = sqlite3.connect("Ejercicio1.db")
cursor = connect.cursor()

# Crear tablas
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(id_usuarios INTEGER PRIMARY KEY AUTOINCREMENT, nombre_usuario TEXT NOT NULL, telefono_usuario TEXT NOT NULL)""")
cursor.execute("CREATE TABLE IF NOT EXISTS productos(id_producto INTEGER PRIMARY KEY AUTOINCREMENT, nombre_producto TEXT NOT NULL, precio_producto FLOAT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS pedidos(id_pedido INTEGER PRIMARY KEY AUTOINCREMENT, fecha_pedido DATE NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS almacen(id_producto INTEGER NOT NULL, existencias_producto INTEGER NOT NULL, FOREIGN KEY (id_producto) REFERENCES productos(id_producto))")

# Registros de la tabla usuarios
cursor.execute('INSERT INTO usuarios(nombre_usuario, telefono_usuario) VALUES (?, ?)', ("Pepe", "123-456-7890"))
cursor.execute('INSERT INTO usuarios(nombre_usuario, telefono_usuario) VALUES (?, ?)', ("Sech", "123-456-7891"))

# Registros de la tabla productos
cursor.execute('INSERT INTO productos(nombre_producto, precio_producto) VALUES (?, ?)', ("Manzana", 12))
cursor.execute('INSERT INTO productos(nombre_producto, precio_producto) VALUES (?, ?)', ("Banana", 12.99))
cursor.execute('INSERT INTO productos(nombre_producto, precio_producto) VALUES (?, ?)', ("Durazno", 10.99))

# Registros de la tabla pedidos
cursor.execute('INSERT INTO pedidos(fecha_pedido) VALUES (?)', ('2025-03-10',))
cursor.execute('INSERT INTO pedidos(fecha_pedido) VALUES (?)', ('2025-03-10',))

# Registros de la tabla almacen
cursor.execute('INSERT INTO almacen(id_producto, existencias_producto) VALUES (?, ?)', (1, 2))
cursor.execute('INSERT INTO almacen(id_producto, existencias_producto) VALUES (?, ?)', (2, 3))

# Guardar datos
connect.commit()
# Cerrar conexión
connect.close()
