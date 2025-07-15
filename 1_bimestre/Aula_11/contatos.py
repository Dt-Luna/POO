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
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()
    @classmethod    
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Fim")
        return int(input("Escolha uma opção: "))
    @classmethod    
    def inserir(cls):
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        c = Contato(id, nome, email, fone)
        cls.__contatos.append(c)
    @classmethod    
    def listar(cls):
        #print(cls.__contatos)
        for c in cls.__contatos:
            print(c)
    @classmethod    
    def atualizar(cls):
        i = int(input('Informe o id do contato a ser atualizado: '))
        print('Digite 0 para manter as informações')
        for c in cls.__contatos:
            if c.get_id() == i:
                n = input('Digite o novo nome: ')
                if n != "0":
                    c.set_nome(n)
                e = input('Digite o novo email: ')
                if e != "0":
                    c.set_email(e)
                f = input('Digite o novo telefone: ')
                if f != "0":
                    c.set_fone(f)
    
    @classmethod    
    def excluir(cls):
        i = int(input('Infome o ID do contato a ser excluído: '))
        for c in cls.__contatos:
            if c.get_id() == i:
                cls.__contatos.remove(c)
    @classmethod    
    def pesquisar(cls):
        nome = input("Informe o nome: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome): print(c)

ContatoUI.main()