import datetime
class Paciente:
    def __init__(self, n, c, f, d):
        self.set_nome(n)
        self.set_cpf(c)
        self.set_fone(f)
        self.set_nascimento(d)
    def set_nome(self, n):
        if len(n)<3: raise ValueError()
        self.__nome = n
    def set_cpf(self, c):
        if len(c)<11: raise ValueError()
        self.__cpf = c
    def set_fone(self, f):
        if len(f)<9: raise ValueError()
        self.__fone = f
    def set_nascimento(self, d):
        self.__nascimento = d
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_fone(self):
        return self.__fone
    def get_nascimento(self):
        return self.__nascimento
    def idade(self):
        hoje = datetime.date.today()
        self.__nascimento = self.__nascimento.date()
        anos = hoje.year - self.__nascimento.year
        meses = hoje.month - self.__nascimento.month
        if hoje.month == self.__nascimento.month:
            if hoje.day < self.__nascimento.day:
                anos -= 1
                meses = 12
        elif hoje.month < self.__nascimento.month:
            meses = hoje.month - self.__nascimento.month + 12
            ano -= 1
        return f'{anos} anos, {meses} meses'
            
    def __str__(self):
        return f"Paciente {self.__nome}\nIdade: {self.idade()}\nCPF: {self.__cpf}\nTelefone: {self.__fone}   "
    
class PacienteUI:
    __pacientes = []
    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Fim")
        opcao = int(input('Escolha uma opção: '))
        return opcao

    @staticmethod
    def main():
        while True:
            opcao = PacienteUI.menu()
            if opcao == 1: PacienteUI.inserir()
            if opcao == 2: PacienteUI.listar()
            if opcao == 3: PacienteUI.atualizar()
            if opcao == 4: PacienteUI.excluir()
            if opcao == 5: PacienteUI.pesquisar()
            if opcao == 5: break
        
    @classmethod
    def inserir(cls):
        try:
            nome = input('Digite o nome: ')
            cpf = input('Digite o CPF: ')
            fone = input('Digite o telefone: ')
            data = input('Digite a data de nascimento no formato dd/mm/yyyy: ')
            data = datetime.datetime.strptime(data, '%d/%m/%Y')
            x = Paciente(nome, cpf, fone, data)
            PacienteUI.__pacientes.append(x)
        except ValueError:
            print('Informações inválidas')

    @classmethod
    def listar(cls):
        if cls.__pacientes:
            for i in cls.__pacientes:
                print(i)
        else:
            print('Não há pacientes registrados')
        
    def atualizar(cls):
        encontrado = False
        cls.listar()
        i = int(input('Informe o cpf do paciente a ser atualizado: '))
        print('Digite 0 para manter as informações')
        for p in cls.__pacientes:
            if p.get_cpf() == i:
                encontrado = True
                n = input('Digite o novo nome: ')
                if n != "0":
                    p.set_nome(n)
                e = input('Digite o novo email: ')
                if e != "0":
                    p.set_nascimento(e)
                f = input('Digite o novo telefone: ')
                if f != "0":
                    p.set_fone(f)
                a = input('Digite o novo aniversário: ')
                if a != "0":
                    a = datetime.datetime.strptime(a, '%d/%m')
                    p.set_nascimento(a)
        if not encontrado: print('Paciente não encontrado')

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
    def excluir(cls):
        encontrado = False
        cls.listar()
        i = int(input('Infome o cpf do paciente a ser excluído: '))
        for p in cls.__pacientes:
            if p.get_cpf() == i:
                encontrado = True
                cls.__pacientes.remove(p)
        if not encontrado: print('Contato não encontrado')
PacienteUI.main()