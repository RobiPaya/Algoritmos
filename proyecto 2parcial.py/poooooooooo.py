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
    frame.grid_forget()
    
    
window=tk.Tk()

frame=tk.Frame(window)
frame.columnconfigure(0, weight=1)
frame.grid(column=0, row=0)

tk.Button(frame, text="Cuadrado", command=cuadrado_boton).grid(column=0, row=0)
tk.Button(frame, text="Triandulo").grid(column=1, row=0)
tk.Button(frame, text="Ciruclo").grid(column=2, row=0)
tk.Button(frame, text="Hexagono").grid(column=3, row=0)

window.mainloop()