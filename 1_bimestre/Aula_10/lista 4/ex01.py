class Viagem:
    def __init__(self, d, k, l):
        self.set_destino(d)
        self.set_distancia(k)
        self.set_litros(l)
    def set_destino(self, d):
        if len(d)<5: raise ValueError('Valor invalido')
        self.__destino = d
    def set_distancia(self, k):
        if k<=0: raise ValueError('Valor invalido')
        self.__distancia = k
    def set_litros(self, l):
        if (l)<=0: raise ValueError('Valor invalido')
        self.__litros = l
    def get_litros(self):
        return self.__litros
    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def consumo(self):
        return self.__distancia/self.__litros
    def __str__(self):
        return f'Destino: {self.__destino}\nDistância: {self.__distancia}km\nCombustível: {self.__litros}L\nConsumo médio: {self.consumo()}L'
    
class ViagemUI:
    @staticmethod
    def menu():
        print('1 - Calcular\n2 - Fim')
        opcao = input('Escolha uma opção ')
        return opcao
    
    @staticmethod
    def main():
        while True:
            opcao = ViagemUI.menu()
            if opcao == '1':
                ViagemUI.calculo()
            elif opcao == '2':
                print('Encerrando o programa')
                break
            else:
                print('Opcção Inválida tente novamente')
    
    @staticmethod
    def calculo():
        try:
            distancia = float(input('Distância percorrida: '))
            destino = input('Destino: ')
            litros = float(input('Litros consumidos :'))
            v = Viagem(destino, distancia, litros)
            print(v)
        
        except ValueError:
            print('Você digitou algo inválido')

ViagemUI.main()