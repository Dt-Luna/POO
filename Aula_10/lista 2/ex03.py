class Conta:
    def __init__(self):
        self.__titular = " "
        self.__saldo = 0.0
        self.__numero = " "
    def set_titular(self, t):
        if t == " ": raise ValueError()
        self.__titular = t
    def set_numero(self, n):
        if n == " ": raise ValueError()
        self.__titular = n
    def set_saldo(self, s):
        if s == " ": raise ValueError()
        self.saldo = s
    def get_titular(self):
        return self.__titular
    def get_numero(self):
        return self.__numero
    def get_saldo(self):
        return self.__saldo
    def depositar (self, v):
        if v < 0: raise ValueError()
        self.__saldo += v
    def sacar (self, v):
        if v < 0: raise ValueError()
        if v > self.__saldo: raise ValueError()
        self.saldo -= v


x = Conta()
x.set_titular(input())
x.set_numero(input())
x.set_saldo(input())
x.depositar(float(input()))
print(x.get_saldo())

