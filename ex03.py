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
        opcao = '0'
        while True:
            opcao = PaisUI.menu()
            if opcao == '1': PaisUI.inserir()
            elif opcao == '2': PaisUI.listar()
            elif opcao == '3': PaisUI.atualizar()
            elif opcao == '4': PaisUI.excluir()
            elif opcao == '5': PaisUI.mais_populoso()
            elif opcao == '6': PaisUI.mais_povoado()
            elif opcao == '7': 
                print('Encerrando')
                break
            else: print('Valor inválido. Tente novamente')

    @classmethod
    def inserir(cls):
            nome = input('Nome do país: ')
            populacao = int(input('População do país: '))
            area = float(input('Área do país: '))
            p = Pais(nome, area, populacao)
            cls.__paises.append(p)

    @classmethod    
    def listar(cls):
        if not cls.__paises:
            print('Não há países registrados\n')
        else:
            for p in cls.__paises:
                print(f'{p}\n')      

    @classmethod    
    def atualizar(cls):
        if not cls.__paises:
            print('Não há países registrados\n')
        else:
            try:
                n = input('Informe o nome do país a ser atualizado: ')
                print('Digite M para manter as informações')
                for p in cls.__paises:
                    if p.get_nome() == n:
                        encontrado = True
                        n = input('Digite o novo nome: ')
                        if n != "M":
                            p.set_nome(n)
                        po = input('Digite a nova população: ')
                        if po != "M":
                            po = int(po)
                            print(type(po))
                            p.set_populacao(po)
                        ar = input('Digite a nova área: ')
                        if ar != "M":
                            ar = int(ar)
                            p.set_area(ar)
                    else: encontrado = False
                if not encontrado: print('País não encontrado')
            except ValueError:
                print('Informações inválidas')
            
    @classmethod    
    def excluir(cls):
        if not cls.__paises:
            print('Não há países registrados\n')
        else:
            try:
                n = input('Informe o nome do país a ser excluído: ')
                for p in cls.__paises:
                    if p.get_nome() == n:
                        encontrado = True
                        cls.__paises.remove(p)
                    else: encontrado = False
                if not encontrado: print('País não encontrado')
            except ValueError:
                print('Informações inválidas')

    @classmethod
    def mais_populoso(cls):
        if not cls.__paises:
            print('Não há países registrados\n')
        else:
            mais_populoso = cls.__paises[0]
            for p in cls.__paises[1:]:
                if p.get_populacao() > mais_populoso.get_populacao():
                    mais_populoso = p
            print(f'O país mais populoso é {mais_populoso.get_nome()}')
    
    @classmethod
    def mais_povoado(cls):
        if not cls.__paises:
            print('Não há países registrados\n')
        else:
            mais_povoado = cls.__paises[0]
            for p in cls.__paises[1:]:
                if p.densidade() > mais_povoado.densidade():
                    mais_povoado = p
            print(f'O país mais povoado é {mais_povoado.get_nome()}')   
    
PaisUI.main()


