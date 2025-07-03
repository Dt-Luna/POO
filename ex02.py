class Contato:
    def __init__(self, i, n, e, f):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
    def get_nome(self):
        return self.__nome
    def get_id(self):
        return self.__id
    def set_nome(self, n):
        if len(n)<0:raise ValueError
        self.__nome = n     
    def set_email(self, e):
        if len(e)<5:raise ValueError
        self.__email = e     
    def set_fone(self, f):
        if len(f)<9:raise ValueError
        self.__fone = f    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class ContatoUI:
    __contatos = []
    @classmethod    
    def main(cls):
        opcao = 0
        while opcao != 6:
            opcao = ContatoUI.menu()
            if opcao == 1: ContatoUI.inserir()
            if opcao == 2: ContatoUI.listar()
            if opcao == 3: ContatoUI.atualizar()
            if opcao == 4: ContatoUI.excluir()
            if opcao == 5: ContatoUI.pesquisar()
    @classmethod    
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Fim")
        return int(input("Escolha uma opção: "))
    
    @classmethod    
    def inserir(cls):
        if not cls.__contatos:
            cls.__numero_id = 0
        id = 1 + cls.__numero_id
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        c = Contato(id, nome, email, fone)
        cls.__contatos.append(c)
        cls.__numero_id +=1
    @classmethod    
    def listar(cls):
        if not cls.__contatos: print('Sem contatos salvos')
        else:
            for c in cls.__contatos:
                print(c)
    @classmethod    
    def atualizar(cls):
        encontrado = False
        cls.listar()
        i = int(input('Informe o id do contato a ser atualizado: '))
        print('Digite 0 para manter as informações')
        for c in cls.__contatos:
            if c.get_id() == i:
                encontrado = True
                n = input('Digite o novo nome: ')
                if n != "0":
                    c.set_nome(n)
                e = input('Digite o novo email: ')
                if e != "0":
                    c.set_email(e)
                f = input('Digite o novo telefone: ')
                if f != "0":
                    c.set_fone(f)
        if not encontrado: print('Contato não encontrado')
    
    @classmethod    
    def excluir(cls):
        encontrado = False
        cls.listar()
        i = int(input('Infome o ID do contato a ser excluído: '))
        for c in cls.__contatos:
            if c.get_id() == i:
                encontrado = True
                cls.__contatos.remove(c)
        if not encontrado: print('Contato não encontrado')
    @classmethod    
    def pesquisar(cls):
        encontrado = False
        nome = input("Informe o nome: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome): 
                print(c) 
                encontrado = True
        if not encontrado: print('Contato não encontrado')
            

ContatoUI.main()