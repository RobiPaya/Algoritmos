import sqlite3
from tabulate import *

connect = sqlite3.connect("Gamers y puntuaciones.db")
cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS jugadores'
'(id_jugador INTEGER PRIMARY KEY AUTOINCREMENT,'
'nombre_jugador TEXT)')

cursor.execute('CREATE TABLE IF NOT EXISTS resultados' 
'(id_resultado INTEGER PRIMARY KEY AUTOINCREMENT,'
'id_jugador INTEGER,' 
'puntuacion INTEGER,'
'FOREIGN KEY (id_jugador) REFERENCES jugadores(id_jugador))')

cursor.execute('INSERT INTO jugadores(nombre_jugador) VALUES'
'(null),'
'("Arturo"),'
'(null),'
'("Palomino"),'
'(null),'
'("Stephen King")')

cursor.execute('INSERT INTO resultados(id_jugador, puntuacion) VALUES' 
'(null, Null),'
'(2, 100000),'
'(3, 10),'
'(4, 150000),'
'(5,142),'
'(null, 37743444455)')

cursor.execute("""SELECT jugadores.nombre_jugador, resultados.puntuacion 
FROM jugadores 
LEFT JOIN resultados ON jugadores.id_jugador = resultados.id_jugador
""")
print(tabulate(cursor.fetchall(), headers=["Nombre Jugador", "Puntuación Jugador"], tablefmt="pretty"))

cursor.execute('SELECT jugadores.nombre_jugador, resultados.puntuacion FROM resultados '
'LEFT JOIN jugadores on jugadores.id_jugador = resultados.id_resultado')
print(tabulate(cursor.fetchall(), headers=["Nombre Jugador", "Puntuación Jugador"], tablefmt="pretty"))

#SELECT jugadores.nombre_jugador, resultados.puntuacion 
#FROM resultados 
#LEFT JOIN jugadores ON jugadores.id_jugador = resultados.id_jugador;

# Guardar datos
connect.commit()
# Cerrar conexión
connect.close()