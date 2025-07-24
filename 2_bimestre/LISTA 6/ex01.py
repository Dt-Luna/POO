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

    def __str__(self):
        return f'{self.__id} - {self.__nome} - {self.__email} - {self.__fone}'
    
class ClienteUI:
    __clientes = []
    @staticmethod
    def menu():
        print('1-Inserir, 2-Listar, 3-Listar por ID, 4-Atualizar, 5-Excluir, 6-Abrir, 7-Salvar')
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
            if opcao == 6: pass

    @classmethod
    def inserir(cls):
        if not cls.__clientes:
            cls.__numero_id_atual = 0
        numero_id = cls.__numero_id_atual + 1
        nome = input('Nome: ')
        email = input('E-mail: ')
        fone = input('Telefone: ')
        x = (numero_id, nome, email, fone)
        cls.__numero_id_atual += 1

    @classmethod
    def listar(cls):
        for c in cls.__clientes:
            print(c)

    @classmethod
    def listar_id(cls):
        id = int(input())


import json
with open("2_bimestre/LISTA_6/.json", "w") as file:
    json.dump({"video1": "feifeifkef"}, file)

with open("Aula_12/arquivo.json", "r") as file:
    caralhoooo: dict = json.load(file)
print(caralhoooo)   