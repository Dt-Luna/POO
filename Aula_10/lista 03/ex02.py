class Frete:
    def __init__(self, d, p):
        self.set_distancia(d)
        self.set_peso(p)
    def set_distancia(self, d):
        if d <= 0: raise ValueError("Valor Inválido")
        self.__distancia = d
    def set_peso(self, p):
        if p <= 0: raise ValueError("Valor Inválido")
        self.__peso = p
    def get_peso(self):
        return self.__peso 
    def get_distancia(self):
        return self.__distancia 
    def calc_frete(self):
        return f"R${(self.__peso/self.__distancia) * 0.01:.2f}"
    def __str__(self):
        return f"Distância: {self.__distancia}km, peso: {self.__peso}kg"

x = Frete(2, 300)
print(x)
print(x.calc_frete())