from view import View

class UI:
    @staticmethod
    def main():
        while True:
            op = UI.menu()
            if op == '1': UI.inserir()
            elif op == '2': UI.listar()
            elif op == '3': UI.atualizar()
            elif op == '4': UI.excluir()
            elif op == '5': UI.pesquisar()
            elif op == '6': UI.aniversariantes()
            elif op == '7': UI.salvar()
            elif op == '8': UI.abrir()
            elif op == '9': break
            else: print('Opção inválida')

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Aniversariantes, 7-Salvar, 8-Abrir, 9-Fim")
        opcao = input("Escolha uma opção: ")
        return opcao
    
    @staticmethod
    def inserir():
        nome = input('Nome do contato: ')
        email = input('Email do contato: ')
        fone = input('Telefone do contato: ')
        aniversario = input('Aniversário do contato: ')
        # View.contato_inserir(nome, email, fone, aniversario)
        if View.contato_inserir(nome, email, fone, aniversario): print('Contato adicionado com sucesso')
            

    @staticmethod
    def listar():
        for contato in View.contato_listar():
            print(contato)

    @staticmethod
    def atualizar():
        id = int(input('ID do contato: '))
        View.contato_listar()
        print('Digite 0 para manter as informações')
        nome = input('nome do contato: ')
        email = input('email do contato: ')
        fone = input('fone do contato: ')
        aniversario = input('aniversario do contato: ')
        View.contato_atualizar(id, nome, email, fone, aniversario)

    @staticmethod
    def pesquisar():
        id = int(input('ID do contato: '))
        print(View.contato_listar_id(id))

    @staticmethod
    def excluir():
        id = int(input('ID do contato: '))
        View.contato_excluir(id)

    @staticmethod
    def aniversariantes():
        mes = input('mes escolhido (numero): ')
        print(View.contato_aniversariantes(mes))

    @staticmethod
    def salvar():
        View.contato_salvar()

    @staticmethod
    def abrir():
        View.contato_abrir()

UI.main()