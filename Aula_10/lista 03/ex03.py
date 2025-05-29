class segundograu:
    def __init__(self,a , b, c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)
    def set_a(self, a):
        self.__a = a
    def set_b(self, b):
        self.__b = b
    def set_c (self, c ):
        self.__c  = c 
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c
    def delta(self):
        self.__delta = self.__b**2 - 4*self.__a*self.__c
        return self.__delta
    def raizes_reais(self):
        if self.delta<0: False
        else: True
    def raiz1(self):
        return (-self.__b + self.__delta**0.5)/