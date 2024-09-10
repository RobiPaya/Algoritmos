import turtle

# Configuración de la pantalla
pantalla = turtle.Screen()
pantalla.title("Pájaro volando hacia un árbol")
pantalla.bgcolor("skyblue")

# Configuración del pájaro
pajaro = turtle.Turtle()
pajaro.shape("triangle")
pajaro.color("red")
pajaro.penup()
pajaro.speed(2)

# Configuración del árbol
arbol = turtle.Turtle()
arbol.shape("square")
arbol.color("green")
arbol.penup()
arbol.goto(200, -100)

# Movimiento del pájaro
def volar(pajaro, destino):
    while pajaro.distance(destino) > 10:
        x = pajaro.xcor() + (destino.xcor() - pajaro.xcor()) * 0.1
        y = pajaro.ycor() + (destino.ycor() - pajaro.ycor()) * 0.1
        pajaro.goto(x, y)

# Ubicación inicial del pájaro
pajaro.goto(-200, 0)

# Ubicación del árbol
destino = turtle.Turtle()
destino.hideturtle()
destino.penup()
destino.goto(200, -100)

# Iniciar el vuelo
volar(pajaro, destino)

# Mantener la ventana abierta hasta que se cierre
pantalla.mainloop()