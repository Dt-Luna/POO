class Pais:
    def __init__(self, n, a, p):
        self.set_nome(n)
        self.set_area(a)
        self.set_populacao(p)
    def set_nome(self, n):
        if len(n)<3: raise ValueError ('Nome inválido')
        self.__nome = n
    def set_area(self, a):
        if a<=0: raise ValueError ('Valor inválido')
        self.__area = a
    def set_populacao(self, p):
        if p<=0: raise ValueError ('Valor inválido')
        self.__populacao = p
    def get_populacao(self):
        return self.__populacao
    def get_area(self):
        return self.__area
    def get_nome(self):
        return self.__nome
    def densidade(self):
        return self.__populacao/self.__area
    def __str__(self):
        return f"Informações\nNome: {self.__nome}\nPopulação: {self.__populacao}\nÁrea: {self.__area}km2\nDensidade: {self.densidade()}pessoas por km2"
    
class PaisUI:
    @staticmethod
    def menu():
        print('1 - Calcular\n2 - Fim')
        opcao = input('Escolha uma opção: ')
        return opcao
    
    @staticmethod
    def main():
        while True:
            opcao = PaisUI.menu()
            if opcao == "1":
                PaisUI.calculo()
            elif opcao == "2":
                print('Encerrando programa')
                break
            else:
                print('Valor Inválido')
    
    @staticmethod
    def calculo():
        try:
            nome = input('Nome do país: ')
            populacao = int(input('População do país: '))
            area = float(input('Área do país: '))
            p = Pais(nome, area, populacao)
            print(p)

        except ValueError:
            print('Valor inválido')

PaisUI.main()

