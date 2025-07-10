from random import randint
class Bingo:
    def __init__(self, b):
        self.set_numbolas(b)
        self.__bolas = []
    
    def set_numbolas(self, b):
        if b<1: raise ValueError
        if type(b) != int: raise ValueError
        self.__num_bolas = b
    
    def set_sorteado(self, s):
        self.__sorteado = s
    
    def sortear(self):
        if len(self.__bolas) == self.__num_bolas:
            print('Todas as bolas sorteadas')
            return -1
        else:
            s = randint(1, self.__num_bolas)
            while s in self.__bolas:
                s = randint(1, self.__num_bolas)
            self.set_sorteado(s)
            self.__bolas.append(self.__sorteado)
            return(self.__sorteado)

    def sorteados(self):
        return sorted(self.__bolas)

class BingoUI:
    __jogo_em_andamento = False
    @staticmethod
    def menu():
        print('1 - Iniciar novo jogo\n2 - Sortear\n3 - Verificar sorteados\n4 - Sair')
        opcao = int(input('Selecione uma opção: '))
        return opcao
    @staticmethod
    def main():
        while True:
            opcao = BingoUI.menu()
            if opcao == 1:
                BingoUI.iniciar_jogo()
            if opcao == 2:
                BingoUI.sortear()
            if opcao == 3:
                BingoUI.sorteados()
            if opcao == 4:
                print('Encerrando')
                break

    @classmethod
    def iniciar_jogo(cls):
        b = int(input('Quanta bolas tem a partida: '))
        cls.jogo = Bingo(b)
        cls.__jogo_em_andamento = True
        return cls.jogo

    @classmethod
    def sortear(cls):
        # jogo = x'
        if cls.__jogo_em_andamento:
            print(cls.jogo.sortear())
        else:
            print('Não há nenhum jogo em andamento')

    @classmethod
    def sorteados(cls):
        if cls.__jogo_em_andamento:
            # jogo_sorteados = cls.jogo.sorteados()
            print('Números sorteados: ')
            for i in cls.jogo.sorteados():
                print(i)
        else:
            print('Não há nenhum jogo em andamento')

BingoUI.main()