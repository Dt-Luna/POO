class segundograu:
    def __init__(self,a , b, c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)
        self.__delta = self.__b**2 - 4*self.__a*self.__c
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
        return self.__delta
    def raizes_reais(self):
        return self.__delta >= 0
    def raiz1(self):
        if self.raizes_reais():
            return (-self.__b + self.__delta**0.5)/2*self.__a
        else: return 'Inexistente'
    def raiz2(self):
        if self.raizes_reais():   
            return (-self.__b - self.__delta**0.5)/2*self.__a
        else:return 'Inexistente'
    def __str__(self):
        return f"A: {self.__a}\nB: {self.__b}\nC: {self.__c}\nDelta: {self.__delta}\n Raiz 1: {self.raiz1()}\nRaiz 2: {self.raiz2()}"

x = segundograu(3,2,1)
print(x)
