class Ingresso:
    def __init__(self):
        self.dia = 'dom'
        self.hora = 18
    def entrada_inteira(self):
        if self.dia == 'qua': return 8
        valor = 16
        if self.dia == 'sex' or self.dia == 'sab' or self.dia == 'dom':
            valor = 20
        if self.hora == 0 or self.hora >= 17: valor = valor * 1.5
        return valor
    def meia_entrada(self):
        if self.dia == 'qua': return 8 
        return self.entrada_inteira()/2
    
x = Ingresso()
x.dia = 'dom'
x.hora = 19
print(x.entrada_inteira())
print(x.meia_entrada())