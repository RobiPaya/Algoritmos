import sqlite3

connect = sqlite3.connect("Ejercicio1.db")
cursor = connect.cursor()

# Crear tablas
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(id_usuarios INTEGER PRIMARY KEY AUTOINCREMENT, nombre_usuario TEXT NOT NULL, telefono_usuario TEXT NOT NULL)""")
cursor.execute("CREATE TABLE IF NOT EXISTS productos(id_producto INTEGER PRIMARY KEY AUTOINCREMENT, nombre_producto TEXT NOT NULL, precio_producto FLOAT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS pedidos(id_pedido INTEGER PRIMARY KEY AUTOINCREMENT, fecha_pedido DATE NOT NULL)")
cursor.execute("""CREATE TABLE IF NOT EXISTS almacen(id_producto INTEGER NOT NULL,
            existencias_producto INTEGER NOT NULL,
            FOREIGN KEY (id_producto) REFERENCES productos(id_producto))""")

# Registros de la tabla usuarios
cursor.execute('INSERT INTO usuarios(nombre_usuario, telefono_usuario) VALUES (?, ?)', ("Pepe", "123-456-7890"))
cursor.execute('INSERT INTO usuarios(nombre_usuario, telefono_usuario) VALUES (?, ?)', ("Sech", "123-456-7891"))
cursor.execute('INSERT INTO usuarios(nombre_usuario, telefono_usuario) VALUES (?, ?)', ("Tilin", "625-159-5258"))
cursor.execute('INSERT INTO usuarios(nombre_usuario, telefono_usuario) VALUES (?, ?)', ("Pomni", "123-666-7891"))

# Registros de la tabla productos
cursor.execute('INSERT INTO productos(nombre_producto, precio_producto) VALUES (?, ?)', ("Manzana", 12))
cursor.execute('INSERT INTO productos(nombre_producto, precio_producto) VALUES (?, ?)', ("Banana", 12.99))
cursor.execute('INSERT INTO productos(nombre_producto, precio_producto) VALUES (?, ?)', ("Durazno", 10.99))
cursor.execute('INSERT INTO productos(nombre_producto, precio_producto) VALUES (?, ?)', ("Frutilla", 1.99))
cursor.execute('INSERT INTO productos(nombre_producto, precio_producto) VALUES (?, ?)', ("Cocoa", 24.99))

# Registros de la tabla pedidos
cursor.execute('INSERT INTO pedidos(fecha_pedido) VALUES (?)', ('2025-03-10',))
cursor.execute('INSERT INTO pedidos(fecha_pedido) VALUES (?)', ('2025-03-10',))
cursor.execute('INSERT INTO pedidos(fecha_pedido) VALUES (?)', ('2025-03-10',))
cursor.execute('INSERT INTO pedidos(fecha_pedido) VALUES (?)', ('2025-03-10',))

# Registros de la tabla almacen
cursor.execute('INSERT INTO almacen(id_producto, existencias_producto) VALUES (?, ?)', (1, 2))
cursor.execute('INSERT INTO almacen(id_producto, existencias_producto) VALUES (?, ?)', (2, 3))
cursor.execute('INSERT INTO almacen(id_producto, existencias_producto) VALUES (?, ?)', (3, 346))
cursor.execute('INSERT INTO almacen(id_producto, existencias_producto) VALUES (?, ?)', (4, 231))

#Update de datos
cursor.execute("UPDATE productos SET precio_producto = ? WHERE id_producto=?",(100.99,2))
cursor.execute("UPDATE usuarios SET nombre_usuario = ? WHERE id_usuarios=?",("No jalo",2))
cursor.execute("UPDATE pedidos SET fecha_pedido = ? WHERE id_pedido=?",('2026-03-10',2))
cursor.execute("UPDATE almacen SET existencias_producto = ? WHERE id_producto=?",(12434334,2))

#Borrar registros
cursor.execute("""DELETE FROM productos WHERE nombre_producto="Manzana" """)

cursor.execute("""SELECT * FROM usuarios""")
datos_usuarios=cursor.fetchall()
print("Tabla Usuarios")
for x in datos_usuarios:
    print(x)

cursor.execute("""SELECT * FROM pedidos""")
datos_pedidos=cursor.fetchall()
print("\nTabla Pedidos")
for x in datos_pedidos:
    print(x)

cursor.execute("""SELECT * FROM productos""")
datos_productos=cursor.fetchall()
print("\nTabla Productos")
for x in datos_productos:
    print(x)

cursor.execute("""SELECT * FROM almacen""")
datos_almacen=cursor.fetchall()
print("\nTabla almacen")
for x in datos_almacen:
    print(x)

# Guardar datos
#connect.commit()
# Cerrar conexión
connect.close()