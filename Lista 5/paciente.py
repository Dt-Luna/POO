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
        self.__idade = hoje - self.__nascimento
    def __str__(self):
        return f"Paciente {self.__nome}\nIdade: {self.__idade}\nCPF: {self.__cpf}\nTelefone: {self.__fone}   "
    
class PacienteUI:
    def menu():
        
        