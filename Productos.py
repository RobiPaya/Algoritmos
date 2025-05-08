import sqlite3
from tabulate import *

connect = sqlite3.connect("Productos.db")
cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS usuarios'
'(id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,'
'nombre_usuario TEXT NOT NULL,'
'telefono_usuario TEXT NOT NULL,'
'correo_usuario TEXT NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS categorias'
'(id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,'
'nombre_categoria TEXT NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS productos'
'(id_producto INTEGER PRIMARY KEY AUTOINCREMENT,'
'id_categoria INTEGER NOT NULL,'
'nombre_producto TEXT NOT NULL,'
'precio_producto INTEGER NOT NULL,'
'existencias_producto INTEGER NOT NULL,'
'FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria))')

cursor.execute('CREATE TABLE IF NOT EXISTS pedidos'
'(id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,'
'id_usuario INTEGER,'
'id_producto INTEGER,'
'fecha_pedido DATE NOT NULL)')
'FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),'
'FOREIGN KEY (id_producto) REFERENCES productos(id_producto),'

cursor.execute('INSERT INTO usuarios(nombre_usuario, telefono_usuario, correo_usuario) VALUES'
'("Mau", "625-111-1111", "Mau@gmail.com"),'
'("Ricio", "625-222-2222", "Ricio@gmail.com"),'
'("Arturo", "625-333-3333", "Arturo@gmail.com"),'
'("Angulo", "625-444-4444", "Angulo@gmail.com")')

cursor.execute('INSERT INTO categorias(nombre_categoria) VALUES'
'("Electronica"),'
'("Ropa"),'
'("Comida"),'
'("Juguetes")')

cursor.execute('INSERT INTO productos(nombre_producto, precio_producto, existencias_producto, id_categoria) VALUES'
'("Maurico", 12, 21500, 3),'
'("Arturo-3000", 19000, 1000, 1),'
'("Palominos", 300, 13000, 4),'
'("Angulo", 400, 5000, 2)')

cursor.execute('INSERT INTO pedidos(id_usuario, id_producto, fecha_pedido) VALUES'
'(1, 1, "2025-03-20"),'
'(2, 2, "2025-06-12"),'
'(3, 3, "2052-01-30"),'
'(4, 4, "2076-08-27")')

#Tabla 1 INNER JOIN y print
cursor.execute('''
SELECT productos.id_producto, productos.nombre_producto, productos.precio_producto, productos.existencias_producto, categorias.nombre_categoria
FROM productos
INNER JOIN categorias
ON productos.id_producto = categorias.id_categoria
''')
print(f"{'ID Producto':<15}{'Nombre producto':<20}{'Precio':<15}{'Existencias':<15}{'Categoria':<20}")
print("-" * 80)
for x in (cursor.fetchall()):
    print(f"{x[0]:<15}{x[1]:<20}{x[2]:<15}{x[3]:<15}{x[4]:<20}")

#Tabla 2 INNER JOIN y print
cursor.execute('''
SELECT pedidos.id_usuario, usuarios.nombre_usuario, pedidos.id_pedido, pedidos.id_producto
FROM pedidos
INNER JOIN usuarios
ON pedidos.id_usuario = usuarios.id_usuario
''')
print(f"\n\n{'ID Usuario':<15}{'Nombre':<20}{'ID Pedido':<15}{'ID Producto':<15}")
print("-" * 80)
for x in (cursor.fetchall()):
    print(f"{x[0]:<15}{x[1]:<20}{x[2]:<15}{x[3]:<15}")

# Guardar datos
connect.commit()
# Cerrar conexión
connect.close()