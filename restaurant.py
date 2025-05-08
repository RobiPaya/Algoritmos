import sqlite3
from tabulate import *

connect = sqlite3.connect("Restaurant.db")
cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes'
'(id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,'
'nombre_cliente TEXT NOT NULL,'
'telefono_cliente TEXT NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS productos'
'(id_producto INTEGER PRIMARY KEY AUTOINCREMENT,'
'nombre_producto TEXT NOT NULL,'
'precio_producto FLOAT NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS pedidos'
'(id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,'
'fecha_pedido DATE NOT NULL,'
'id_cliente INTEGER NOT NULL,'
'total_pedido FLOAT NOT NULL,'
'FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente))')

cursor.execute('CREATE TABLE IF NOT EXISTS detalles_pedidos'
'(id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,'
'id_pedido INTEGER NOT NULL,'
'id_producto INTEGER NOT NULL,'
'cantidad_detalle INTEGER NOT NULL,'
'subtotal_detalle INTEGER NOT NULL,'
'FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),'
'FOREIGN KEY (id_producto) REFERENCES productos(id_producto))')

cursor.execute('INSERT INTO clientes(nombre_cliente, telefono_cliente) VALUES'
'("Mauricio", "625-111-1111"),'
'("Arturo", "625-222-2222"),'
'("Angulo", "625-333-3333"),'
'("Palomino", "625-444-4444"),'
'("Pepe", "625-555-5555")')

cursor.execute('INSERT INTO productos(nombre_producto, precio_producto) VALUES'
'("Pollo", 149.99),'
'("Polla", 149.99),'
'("Gallina", 299.99),'
'("Gallo", 299.99),'
'("Huevo", 49.99)')

cursor.execute('INSERT INTO pedidos(fecha_pedido, id_cliente, total_pedido) VALUES'
'("2025-03-25", 1, 300),'
'("2025-08-12", 1, 300),'
'("2026-06-26", 3, 6),'
'("2012-12-12", 2, 12),'
'("2011-03-11", 5, 11),'
'("2010-10-10", 4, 10)')

cursor.execute('INSERT INTO detalles_pedidos(id_pedido, id_producto, cantidad_detalle, subtotal_detalle) VALUES'
'(1, 1, 1, 1),'
'(2, 2, 2, 2),'
'(3, 3, 3, 3),'
'(4, 4, 4, 4),'
'(5, 5, 5, 5)')


cursor.execute("SELECT * FROM clientes")
for x in (cursor.fetchall()):
    print(x[1])

cursor.execute("SELECT * FROM productos ORDER BY precio_producto DESC")
for x in (cursor.fetchall()):
    print(x[2])

cursor.execute("SELECT * FROM pedidos")
for x in (cursor.fetchall()):
    print(x)

cursor.execute("SELECT * FROM detalles_pedidos WHERE id_pedido = 3")
for x in (cursor.fetchall()):
    print(x)

cursor.execute('''
SELECT clientes.nombre_cliente, COUNT(pedidos.id_pedido) as total_pedidos
FROM pedidos
INNER JOIN clientes
ON clientes.id_cliente = pedidos.id_cliente
GROUP BY clientes.id_cliente
ORDER BY total_pedidos DESC
''')
for x in cursor.fetchall():
    print(f"{x[0]} ha hecho {x[1]} pedidos")

cursor.execute('SELECT * FROM pedidos WHERE fecha_pedido BETWEEN ("2010-01-01") AND ("2025-01-01")')
for x in cursor.fetchall():
    print(x)

cursor.execute("SELECT nombre_cliente FROM clientes WHERE nombre_cliente LIKE 'M%'")
for x in (cursor.fetchall()):
    print(x[0])

cursor.execute("SELECT nombre_producto FROM productos WHERE precio_producto > 50")
for x in (cursor.fetchall()):
    print(x[0])

cursor.execute("UPDATE productos SET precio_producto = ? WHERE nombre_producto = ?", ("90", "Pollo"))

cursor.execute("DELETE FROM clientes WHERE id_cliente = '5'")

cursor.execute('SELECT * FROM pedidos ORDER BY fecha_pedido DESC')
for x in (cursor.fetchall()):
    print(x)

cursor.execute('SELECT * FROM productos ORDER BY precio_producto DESC')
for x in (cursor.fetchall()):
    print(x)

cursor.execute("SELECT SUM(total_pedido) FROM pedidos")
for x in (cursor.fetchall()):
    print(x)

cursor.execute("SELECT count(id_producto) FROM productos")
for x in (cursor.fetchall()):
    print(x)

cursor.execute('''
SELECT clientes.nombre_cliente, pedidos.fecha_pedido
FROM pedidos
INNER JOIN clientes
ON clientes.id_cliente = pedidos.id_cliente
''')
for x in (cursor.fetchall()):
    print(x)

#Clientes por alfabetismo
#Mostrar pedido en especiifc
#Pordcuto mas caro
#Total de ventas por fechas
#Ver los pedidos con iun total mayor a 159
#Buscar los productos n un pedido en especifico
#Actualizar el nimero de telefono
#Total generado por un cleinte
#Obtener el total de cada cliente
#Mostrar productos de entre 50 y 100$
#Ver todos los pedidos del mes de marzo

print("\nConsultas del Mau\n")
print("1. aLFAbetico")
cursor.execute("SELECT * FROM clientes ORDER BY nombre_cliente ASC")
print(tabulate(cursor.fetchall(), headers=["ID Cliente", "Nombre Cliente", "Telefono Cliente"], tablefmt="simple"),"\n")

print("2. Mostar PEDIDOS de un cliente en especifico")
cursor.execute("""SELECT clientes.nombre_cliente, pedidos.id_pedido, pedidos.fecha_pedido, pedidos.total_pedido
FROM pedidos
INNER JOIN clientes
ON clientes.id_cliente = pedidos.id_cliente
WHERE nombre_cliente = 'Mauricio'""")
print(tabulate(cursor.fetchall(), headers=["Nombre Cliente", "ID Pedido", "Fecha Pedido", "Total Pedido"], tablefmt="pretty"), "\n")

print("3. Más caro")
cursor.execute('SELECT * FROM productos WHERE precio_producto = (SELECT MAX (precio_producto) FROM productos)')
print(tabulate(cursor.fetchall(), headers=["ID Producto", "Nombre Producto", "Precio Producto"], tablefmt="pretty"),"\n")

print("4. Total de ventas por fechas")
cursor.execute("""SELECT fecha_pedido, SUM(total_pedido) AS total_ventas
FROM pedidos
GROUP BY fecha_pedido
ORDER BY fecha_pedido ASC""")
print(tabulate(cursor.fetchall(), headers=["Fecha", "Total de ventas"], tablefmt="rst"), "\n")

print("5. Mayor a 150$")
cursor.execute("SELECT * FROM pedidos WHERE total_pedido > 150")
print(tabulate(cursor.fetchall(), headers=["ID Pedido", "Fecha Pedido", "ID Cliente", "Total Pedido"], tablefmt="pretty"), "\n")

print("6. Buscar los PRODUCTOS en un pedido en especifico")
cursor.execute("""SELECT detalles_pedidos.id_pedido, productos.id_producto, productos.nombre_producto
FROM productos
INNER JOIN detalles_pedidos
ON productos.id_producto = detalles_pedidos.id_producto
WHERE id_pedido = 1""")
print(tabulate(cursor.fetchall(), headers=["ID Pedido", "ID Producto", "Nombre Producto"], tablefmt="pretty"), "\n")

print("7. Updatear el telefono de un cliente")
cursor.execute('SELECT * FROM clientes WHERE id_cliente = 1')
print("Viejo")
print(tabulate(cursor.fetchall(), headers=["ID Cliente", "Nombre Cliente", "Telefono Cliente"], tablefmt="eggs"), "\n")
cursor.execute("UPDATE clientes SET telefono_cliente = '625-214-6423' WHERE id_cliente = 1")
cursor.execute('SELECT * FROM clientes WHERE id_cliente = 1')
print("Nuevo")
print(tabulate(cursor.fetchall(), headers=["ID Cliente", "Nombre Cliente", "Telefono Cliente"], tablefmt="eggs"), "\n")

print("8. Obtener el total generado de cada cliente")
cursor.execute("""
SELECT clientes.id_cliente, clientes.nombre_cliente, SUM(pedidos.total_pedido) AS total_generado
FROM clientes
INNER JOIN pedidos
ON clientes.id_cliente = pedidos.id_cliente
GROUP BY clientes.id_cliente
""")
print(tabulate(cursor.fetchall(), headers=["ID Cliente", "Nombre Cliente", "Total Generado"], tablefmt="pretty"), "\n")


print("9. Productos entre 50$ y 100$")
cursor.execute('SELECT * FROM productos WHERE precio_producto < 100 AND precio_producto > 50')
print(tabulate(cursor.fetchall(), headers=["ID Producto", "Nombre Producto", "Precio Producto"], tablefmt="pretty"), "\n")

print("10. Pedidos realizados en marzo")
cursor.execute("""
SELECT * FROM pedidos
WHERE strftime('%m', fecha_pedido) = '03'
""")
print(tabulate(cursor.fetchall(), headers=["ID Pedido", "Fecha Pedido", "ID Cliente", "Total Pedido"], tablefmt="pretty"), "\n")


# Guardar datos
connect.commit()
# Cerrar conexión
connect.close()