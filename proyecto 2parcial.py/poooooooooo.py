class figura:
    def __init__(self,lado1,lado2):
        self.lado1=lado1
        self.lado2=lado2
    
    def area(self):
        return self.lado1 * self.lado2
    
    def resulta(self):
        return f"El area del {self.__class__.__name__} es {self.area()}"

#instanciar la clase figura
cuadro =figura(10,20)
print(cuadro.resulta())