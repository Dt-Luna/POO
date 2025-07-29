import datetime
import json
class Contato:
    def __init__(self, i, n, e, f, a):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
        self.__aniversario = a
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
    def set_aniversario(self, a):
        self.__aniversario = a
    def get_aniversario(self):
        return self.__aniversario
    def get_nome(self):
        return self.__nome
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__aniversario}"

class ContatoUI:
    __contatos = []
    @classmethod    
    def main(cls):
        opcao = 0
        while opcao != 7:
            opcao = ContatoUI.menu()
            if opcao == 1: ContatoUI.inserir()
            if opcao == 2: ContatoUI.listar()
            if opcao == 3: ContatoUI.atualizar()
            if opcao == 4: ContatoUI.excluir()
            if opcao == 5: ContatoUI.pesquisar()
            if opcao == 6: ContatoUI.aniversariantes()
            if opcao == 7: ContatoUI.salvar()
            if opcao == 8: ContatoUI.abrir()
    @classmethod    
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Aniversariantes, 7-Salvar, 8-Abrir, 9-Fim")
        return int(input("Escolha uma opção: "))
    
    @classmethod    
    def inserir(cls):
        if not cls.__contatos:
            cls.__numero_id = 0
        try:
            id = 1 + cls.__numero_id
            nome = input("Informe o nome: ")
            email = input("Informe o e-mail: ")
            fone = input("Informe o fone: ")
            aniversario = input('informe seu aniversário(dd/mm): ')
            aniversario = datetime.datetime.strptime(aniversario, '%d/%m')
            c = Contato(id, nome, email, fone, aniversario)
            cls.__contatos.append(c)
            cls.__numero_id +=1
        except ValueError:
            print('Informações inválidas')
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
                a = input('Digite a nova data: ')
                if a != '0':
                    a = datetime.datetime.strptime(a, '%d/%m')
                    c.set_aniversario(a)
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
            
    @classmethod
    def aniversariantes(cls):
        encontrado = False
        mes = input('Informe o mês(numero): ')
        mes = datetime.datetime.strptime(mes, '%m')
        print('Aniversariantes:')
        for c in cls.__contatos:
            aniversario = c.get_aniversario()
            if aniversario.month == mes.month:
                print(c.get_nome())
                encontrado = True
        if not encontrado: print('Não há aniversariantes neste mês')

    @classmethod
    def salvar(cls):
        with open('2_bimestre/lista 7_contato/contatos.json', mode='w') as arquivo:
            contatos_json = json.dump(cls.__contatos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        with open('2_bimestre/lista 7_contato/contatos.json', mode='r') as arquivo:
            contatos_json = json.load(arquivo)
            for obj in contatos_json:
                contato = Contato(obj['id'], obj['nome'], obj['email'], obj['fone'], obj['aniversario'])
                cls.__contatos.append(contato)

ContatoUI.main()