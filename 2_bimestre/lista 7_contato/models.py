import datetime
import json
class Contato:
    def __init__(self, i, n, e, f, a):
        self.id = i
        self.nome = n
        self.email = e
        self.fone = f
        self.aniversario = a
    def set_nome(self, n):
        if len(n)<3:raise ValueError
        self.nome = n     
    def set_email(self, e):
        if len(e)<5:raise ValueError
        self.email = e     
    def set_fone(self, f):
        if len(f)<9:raise ValueError
        self.fone = f    
    def set_aniversario(self, a):
        if type(a) != datetime.date: raise ValueError
        self.aniversario = a
    
    def get_id(self):
        return self.id
    def get_aniversario(self):
        return self.__aniversario
    def get_nome(self):
        return self.__nome
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone} - {self.aniversario}"
    
    def dict(self):
        return{
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'fone': self.fone,
            'aniversario': datetime.datetime.strptime(self.aniversario, '%d/%m')
        }

class ContatoDAO:
    __contatos = []

    @classmethod
    def inserir(cls, obj):
        try:
            cls.__abrir()
            id = 0
            for aux in cls.__contatos:
                if aux.id > id: id = aux.id
            obj.id = id + 1
            cls.__contatos.append(obj)
            cls.__salvar()
            return True
        except ValueError:
            return False

    @classmethod
    def listar(cls):
        cls.__abrir()
        return cls.__contatos
    
    @classmethod
    def listar_id(cls, id):
        cls.__abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id: return obj

    @classmethod
    def atualizar(cls, id, nome, email, fone, aniversario):
        cls.__abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id:
                obj.set_nome(nome)
                obj.set_email(email)
                obj.set_fone(fone)
                obj.set_aniversario(aniversario)

    @classmethod
    def excluir(cls, id):
        cls.listar()
        for c in cls.__contatos:
            if c.get_id() == id:
                cls.__contatos.remove(c)
                cls.__salvar()
                return True

    @classmethod    
    def pesquisar(cls, nome):
        cls.__abrir()
        for c in cls.__contatos:
            if c.get_nome().startswith(nome): 
                return c             

    @classmethod
    def aniversariantes(cls, mes):
        cls.__abrir()
        for c in cls.__contatos:
            aniversario = c.get_aniversario()
            if aniversario.month == mes.month:
                return c.get_nome()

    @classmethod
    def __salvar(cls):
        with open('2_bimestre/lista 7_contato/contatos.json', mode='w') as arquivo:
            contatos_json = [c.dict() for c in cls.__contatos]
            json.dump(contatos_json, arquivo, indent=2)


    @classmethod
    def __abrir(cls):
        cls.__contatos.clear()
        try:
            with open('2_bimestre/lista 7_contato/contatos.json', mode='r') as arquivo:
                contatos_json = json.load(arquivo)
                for obj in contatos_json:
                    # Convertendo string para datetime.date
                    obj['aniversario'] = datetime.datetime.strptime(obj['aniversario'], '%d/%m')
                    contato = Contato(obj['id'], obj['nome'], obj['email'], obj['fone'], obj['aniversario'])
                    cls.__contatos.append(contato)
        except FileNotFoundError:
            pass
                



