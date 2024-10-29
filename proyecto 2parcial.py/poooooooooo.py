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

#instanciar la clase figura
cuadro =trianglulo(10,20)
print(cuadro.resulta())