import json
class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def set_id(self, id):
        if id<0: raise ValueError()
        self.__id = id
    
    def set_nome(self, nome):
        if len(nome)<3: raise ValueError()
        self.__nome = nome

    def set_email(self, email):
        if len(email) < 4: raise ValueError()
        self.__email = email

    def set_fone(self, fone):
        if len(fone)<9: raise ValueError()
        self.__fone = fone

    def get_id(self):
        return self.__id
    
    def __str__(self):
        return f'{self.__id} - {self.__nome} - {self.__email} - {self.__fone}'
    
class ClienteUI:
    __clientes = []
    @staticmethod
    def menu():
        print('1-Inserir, 2-Listar, 3-Listar por ID, 4-Atualizar, 5-Excluir, 6-Abrir, 7-Salvar, 8-Fim')
        opcao = int(input('Escolha uma opção: '))
        return opcao
    
    @staticmethod
    def main():
        while True:
            opcao = ClienteUI.menu()
            if opcao == 1: ClienteUI.inserir()
            if opcao == 2: ClienteUI.listar()
            if opcao == 3: ClienteUI.listar_id()
            if opcao == 4: ClienteUI.atualizar()
            if opcao == 5: ClienteUI.excluir()
            if opcao == 6: ClienteUI.abrir
            if opcao == 7: ClienteUI.salvar()
            if opcao == 8: break

    @classmethod
    def inserir(cls):
        if not cls.__clientes:
            cls.__numero_id_atual = 0
        numero_id = cls.__numero_id_atual + 1
        try:
            nome = input('Nome: ')
            email = input('E-mail: ')
            fone = input('Telefone: ')
            x = Cliente(numero_id, nome, email, fone)
            cls.__clientes.append(x)
            cls.__numero_id_atual += 1
        except ValueError(): print('Informações inválidas')

    @classmethod
    def listar(cls):
        if not cls.__clientes: 
            print('Nenhum cliente cadastrado') 
            return 
        for c in cls.__clientes:
            print(c)

    @classmethod
    def listar_id(cls):
        encontrado = False
        id = int(input('ID: '))
        for c in cls.__clientes:
            if c.get_id() == id:
                encontrado = True
                print(c)    
        if not encontrado: print('Cliente não encontrado')

    @classmethod
    def atualizar(cls):
        encontrado = False
        try:
            id = int(input('ID do cliente: '))
            for c in cls.__clientes:
                if c.get_id() == id:
                    encontrado = True
                    nome = input('Nome: ')
                    if nome != '0':
                        c.set_nome(nome)
                    email = input('Email: ')
                    if email != '0':
                        c.set_email(email)
                    fone = input('Fone: ')
                    if fone != '0':
                        c.set_fone(fone)
                print('Cliente atualizado')
                if not encontrado:
                    print('Cliente não encontrado')
        except ValueError(): print('Informações inválidas')

    @classmethod
    def excluir(cls):
        encontrado = False
        try:
            id = int(input('Cliente a ser excluído: '))
            for c in cls.__clientes:
                if c.get_id() == id:
                    encontrado = True
                    cls.__clientes.remove(c)
            if not encontrado: print('Cliente não encontrado')
        except ValueError(): print('ID inválido')
    
    @classmethod
    def abrir(cls):
        with open("2_bimestre/LISTA 6/clientes.json", mode="r") as arquivo:
            clientes_json = json.load(arquivo)
            for obj in clientes_json:
                c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                cls.__clientes.append(c)
 

    @classmethod
    def salvar(cls):
        with open("2_bimestre/LISTA 6/clientes.json", mode="w") as arquivo:
            json.dump(cls.__clientes, arquivo, default = vars)

ClienteUI.main()