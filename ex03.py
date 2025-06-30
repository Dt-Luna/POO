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
        return f"Informações\nNome: {self.__nome}\nPopulação: {self.__populacao}\nÁrea: {self.__area}\nDensidade: {self.densidade()}"
    
class PaisUI:
    __paises = []
    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Listar o mais populoso, 6-Listar o mais povoado, 7-Fim")
        opcao = input('Escolha uma opção: ')
        return opcao
    
    @classmethod
    def main(cls):
        opcao = 0
        while opcao != 7:
            opcao = PaisUI.menu()
            if opcao == 1: PaisUI.inserir()
            if opcao == 2: PaisUI.listar()
            if opcao == 3: PaisUI.atualizar()
            if opcao == 4: PaisUI.excluir()
            if opcao == 5: PaisUI.mais_populuso()
            if opcao == 6: PaisUI.mais_povoado()

    @classmethod
    def inserir(cls):
            nome = input('Nome do país: ')
            populacao = int(input('População do país: '))
            area = float(input('Área do país: '))
            p = Pais(nome, area, populacao)
            cls.__paises.append(p)

    @classmethod    
    def listar(cls):
        for p in cls.__paises:
            print(p)      

    @classmethod    
    def atualizar(cls):
        n = int(input('Informe o nome do país a ser atualizado: '))
        print('Digite 0 para manter as informações')
        for p in cls.__paises:
            if p.get_nome() == n:
                n = input('Digite o novo nome: ')
                if n != "0":
                    p.set_nome(n)
                po = input('Digite a nova população: ')
                if po != "0":
                    p.set_populacao(po)
                ar = input('Digite o novo telefone: ')
                if ar != "0":
                    p.set_area(ar)
            
    @classmethod    
    def excluir(cls):
        n = int(input('Informe o nome do país a ser atualizado: '))
        for p in cls.__contatos:
            if p.get_nome() == n:
                cls.__paises.remove(p)

    @classmethod
    def mais_populuso(cls):
        mais = 0
        for p in cls.__paises:
            if p.__densidade > mais:
                mais = p.__densidade
        return mais
    
    @classmethod
    def mais_povoado(cls):
        mais = 0
        for p in cls.__paises:
            if p.__populacao > mais:
                mais = p.__populacao
        return mais
    
PaisUI.main()

