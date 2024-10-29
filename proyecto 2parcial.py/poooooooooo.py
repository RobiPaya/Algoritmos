import math
import tkinter as tk
class figura:
    def __init__(self,lado1,lado2):
        self.lado1=lado1
        self.lado2=lado2
    
    def area(self):
        return self.lado1 * self.lado2
    
    def resulta(self):
        return f"El area del {self.__class__.__name__} es {self.area()}"
class rectangulo(figura):
    pass
class trianglulo(rectangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def area(self):
        return super().area()/2
class hexagono(figura)  :
    def __init__(self, lado):
        self.lado=lado
    def area(self):
        return ((3*(3**0.5))*self.lado**2)/2
class circulo(figura):
    def __init__(self, radio):
        self.radio=radio
    def area(self):
        return 3.1416*(self.radio**2)
class cuadrado(figura):
    def __init__(self, lado):
        self.lado=lado
    def area(self):
        return self.lado**2
#instanciar la clase figura

#Definiciones para el tkinter
def cuadrado_boton():
    framecirculo.grid_forget() 
    frametriangula.grid_forget()
    tk.Label(framecuadrado, text="Lado : ").grid(column=0, row=1)
    lado=tk.Entry(framecuadrado).grid(column=1, row=1)
    tk.Button(framecuadrado, text="CALCULAR").grid(column=1, row=2)
    framecuadrado.grid(column=0, row=1)
    return lado

def triangulo_boton():
    framecirculo.grid_forget()
    framecuadrado.grid_forget()
    tk.Label(frametriangula, text="Base : ").grid(column=0, row=1)
    base=tk.Entry(frametriangula).grid(column=1, row=1)
    tk.Label(frametriangula, text="Altura : ").grid(column=0, row=2)
    altura=tk.Entry(frametriangula).grid(column=1, row=2)
    tk.Button(frametriangula, text="CALCULAR").grid(column=1, row=3)
    frametriangula.grid(column=0, row=1)
    return base, altura

window=tk.Tk()

frame=tk.Frame(window)
frame.columnconfigure(0, weight=1)
frame.grid(column=0, row=0)

tk.Button(frame, text="Cuadrado", command=cuadrado_boton).grid(column=0, row=0)
tk.Button(frame, text="Triandulo", command=triangulo_boton).grid(column=1, row=0)
tk.Button(frame, text="Ciruclo").grid(column=2, row=0)
tk.Button(frame, text="Hexagono").grid(column=3, row=0)

framecuadrado=tk.Frame(window)
framecuadrado.columnconfigure(0, weight=1)
framecuadrado.grid(column=0, row=1)

frametriangula=tk.Frame(window)
frametriangula.columnconfigure(0, weight=1)
frametriangula.grid(column=0, row=1)

framecirculo=tk.Frame(window)
framecirculo.columnconfigure(0, weight=1)
framecirculo.grid(column=0, row=1)

window.mainloop()