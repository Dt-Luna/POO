class Circulo:
    def __init__(self):
        self.raio = 0
    def calcular_area(self):
        return self.raio ** 2 * 3.14
    
x = Circulo()
x.raio = 10
print(x.calcular_area(x))
