from view import View

class UI:
    @staticmethod
    def main():
        while True:
            op = UI.menu()
            while op != 9:
                if op == 1: UI.inserir()
                if op == 2: UI.listar()
                if op == 1: pass
                if op == 1: pass
                if op == 1: pass

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Aniversariantes, 7-Salvar, 8-Abrir, 9-Fim")
        opcao = int(input("Escolha uma opção: "))
        return opcao
    
    @staticmethod
    def inserir():
        nome = input('Nome do contato: ')
        email = input('Email do contato: ')
        fone = input('Telefone do contato: ')
        aniversario = input('Aniversário do contato: ')
        # View.contato_inserir(nome, email, fone, aniversario)
        if View.contato_inserir(nome, email, fone, aniversario): print('Contato adicionado com sucesso')
        else: 
            print('Falha ao adicionar contato')
            # pass

    @staticmethod
    def listar():
        for contato in View.contato_listar():
            print(contato)

    @staticmethod
    def listar_id():
        id = int(input('ID do contato: '))
        View.contato_listar_id(id)

    @staticmethod
    def excluir():
        id = int(input('ID do contato: '))
        View.contato_excluir(id)

UI.main()