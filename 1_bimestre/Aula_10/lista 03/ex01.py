class Retangulo:
    def __init__(self, b, h):
        self.set_altura(h)
        self.set_base(b)
    def __str__(self):
        return f"Base: {self.__base}, altura: {self.__altura}"
    def set_base (self, b):
        if b <= 0: raise ValueError("Valor inválido")
        self.__base = b
    def set_altura (self, h):
        if h <= 0: raise ValueError("Valor inválido")
        self.__altura = h
    def get_altura (self):
        return self.__altura
    def get_base (self):
        return self.__base
    def calc_area(self):
        return self.__altura * self.__base
    def calc_diagonal(self):
        return (self.__altura**2 + self.__base**2)**0.5

x = Retangulo(2,3)
print(x)
print(x.calc_area())
print(x.calc_diagonal())
x.set_altura(5)
x.set_base(8)
print(x.calc_area())
print(x.calc_diagonal())
print(x)
print(x.get_altura())
print(x.get_base())