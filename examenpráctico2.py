import sqlite3
from tabulate import *

#1.
connect = sqlite3.connect("empresa.db")
cursor = connect.cursor()

#2.
cursor.execute('CREATE TABLE IF NOT EXISTS clientes'
'(id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,' \
'nombre TEXT NOT NULL,'
'correo TEXT NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS ordenes'
'(id_orden INTEGER PRIMARY KEY AUTOINCREMENT,'
'id_cliente INTEGER NOT NULL,'
'producto TEXT NOT NULL,'
'total INTEGER NOT NULL,'
'FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente))')

#3.
cursor.execute('INSERT INTO clientes (nombre, correo) VALUES' \
'("Mauricio", "Mauricio@gmail.com"),'
'("Arturo", "Arturo@gmail.com"),'
'("Angulo", "Angulo@gmail.com"),'
'("Palomino", "Palomino@gmail.com"),'
'("Mauricito", "Mauricito@gmail.com")')

cursor.execute('INSERT INTO ordenes (id_cliente, producto, total) VALUES' 
'(1, "Manzana", 23),'
'(1, "Platano", 27),'
'(2, "Pera", 3),'
'(2, "Uva", 2),'
'(3, "Coco", 50),'
'(3, "Calabaza", 50),'
'(4, "Chocolate", 123),'
'(4, "Fruta", 127),'
'(5, "Verdura", 500),'
'(5, "Producto", 500)')

#4.
cursor.execute("""SELECT clientes.nombre, ordenes.producto, SUM(ordenes.total) as total FROM ordenes 
INNER JOIN clientes
ON clientes.id_cliente = ordenes.id_cliente
GROUP BY ordenes.id_cliente""")
print(tabulate(cursor.fetchall(), headers=["Nombre del cliente", "Producto", "Total de la orden"], tablefmt="pretty"))

#5.
cursor.execute('SELECT total FROM ordenes WHERE total > 50')
print(tabulate(cursor.fetchall(), headers=["Mayores a 50"], tablefmt="pretty"))

#6.
cursor.execute("UPDATE ordenes SET total = ? WHERE total = ?", (7, 2))

#7
cursor.execute('DELETE FROM ordenes WHERE id_orden = 5')

#8.
connect.commit()
connect.close()