class Circulo:
    def __init__(self):
        self.__raio = 0.0
    def set_raio(self, r):
        if r<=0: raise ValueError('Valor inválido')
        self.__raio = r
    def get_raio(self):
        return self.__raio
    def calc_area(self):
        return 3.14 * self.__raio**2
    def calc_circunferencia(self):
        return 3.14 * 2 * self.__raio
    def __str__(self):
        return f"Raio: {self.__raio}"

a = Circulo()
print(a.get_raio())
a.set_raio(2)
print(a.get_raio())
print(a)
print(a.calc_area())
print(a.calc_circunferencia())