class Viagem:
    def __init__(self):
        self.__tempo = 0
        self.__distancia = 0
    def set_tempo(self, t):
        if t <= 0: raise ValueError('Valor inválido')
        self.__tempo = t
    def get_tempo(self):
        return self.__tempo
    def set_distancia(self, d):
        if d <= 0: raise ValueError('Valor inválido')
        self.__distancia = d
    def get_distancia(self):
        return self.__distancia
    def calc_velocidade(self):
        return f"{self.__distancia/self.__tempo}km/h"
    
x = Viagem()
print(x.get_tempo())
x.set_distancia(float(input()))
x.set_tempo(float(input()))
print(x.calc_velocidade())
    