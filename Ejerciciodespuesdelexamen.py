import sqlite3
from tabulate import *

connect = sqlite3.connect("empresa.db")
cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes'
'(id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,'
'nombre TEXT,'
'telefono TEXT,'
'correo TEXT)')

cursor.execute('CREATE TABLE IF NOT EXISTS pedidos'
'(id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,'
'id_cliente INTEGER,'
'producto TEXT,'
'cantidad INTEGER,'
'fecha_pedido DATE,'
'FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente))')

#1
cursor.execute('INSERT INTO clientes (nombre, telefono, correo) VALUES' \
'("Mauricio", NULL ,"Mauricio@gmail.com"),'
'("Arturo", "625-222-2222", "Arturo@gmail.com"),'
'("Angulo", "625-333-333", "Angulo@gmail.com")')

#2
cursor.execute('INSERT INTO pedidos (id_cliente, producto, cantidad, fecha_pedido) VALUES' 
'(1, "Manzana", 23, "2025-06-21"),'
'(1, "Platano", 27, "2025-03-15"),'
'(1, "Pera", 3, "2025-02-15"),'
'(null, "Uva", 2, "2025-09-28"),'
'(2, "Coco", 50, "2024-01-01"),'
'(2, "Calabaza", 50, "2024-09-30"),'
'(2, "Chocolate", 123, "2025-12-25"),'
'(3, "Fruta", 127, "2025-12-31"),'
'(3, "Verdura", 500, "2025-08-14"),'
'(3, "Producto", 500, "2025-05-27")')

#3
cursor.execute('SELECT nombre FROM clientes')
print(tabulate(cursor.fetchall(), headers=["Nombre"], tablefmt="pretty"))

#4
cursor.execute('SELECT * FROM clientes WHERE id_cliente = 1')
print(tabulate(cursor.fetchall(), headers=["ID del cliente consultado", "Nombre", "telefono","correo"], tablefmt="pretty"))

#5
cursor.execute("UPDATE clientes SET telefono = ? WHERE id_cliente = ?", ("625-234-5678", 2))

#6
cursor.execute('DELETE FROM clientes WHERE id_cliente = 3')

#7
cursor.execute('SELECT producto FROM pedidos ORDER BY producto ASC')
print(tabulate(cursor.fetchall(), headers=["Nombre"], tablefmt="pretty"))

#8
cursor.execute('SELECT COUNT(nombre) FROM clientes WHERE telefono IS NOT NULL')
print(tabulate(cursor.fetchall(), headers=["Cantidad de clientes con teléfono"], tablefmt="pretty"))

#9
cursor.execute('SELECT clientes.nombre, pedidos.producto, pedidos.cantidad, pedidos.fecha_pedido FROM pedidos '
'INNER JOIN clientes '
'ON clientes.id_cliente = pedidos.id_cliente')
print(tabulate(cursor.fetchall(), headers=["Nombre del cliente", "Producto", "Cantidad", "Fecha pedido"], tablefmt="pretty"))

#10
cursor.execute('SELECT * FROM clientes')
print(tabulate(cursor.fetchall(), headers=["ID cliente","Nombre", "Telefono", "Correo"], tablefmt="pretty"))

#cursor.execute("""SELECT clientes.nombre, ordenes.producto, SUM(ordenes.total) as total FROM ordenes 
#INNER JOIN clientes
#ON clientes.id_cliente = ordenes.id_cliente
#GROUP BY ordenes.id_cliente""")
#print(tabulate(cursor.fetchall(), headers=["Nombre del cliente", "Producto", "Total de la orden"], tablefmt="pretty"))

#cursor.execute('SELECT total FROM ordenes WHERE total > 50')
#print(tabulate(cursor.fetchall(), headers=["Mayores a 50"], tablefmt="pretty"))

connect.commit()
connect.close()
