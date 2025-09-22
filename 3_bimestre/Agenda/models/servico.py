import json
class Servico:
    def __init__(self, id, desc, valor):
        self.set_id(id)
        self.set_desc(desc)
        self.set_valor(valor)
    
    def set_id(self, id): self.__id = id
    def set_desc(self, desc): self.__desc = desc
    def set_valor(self, valor): self.__valor = valor

    def get_id(self): return self.__id
    def get_desc(self): return self.__desc
    def get_valor(self): return self.__valor

    def to_json(self):
        dic = {"id":self.__id, "desc":self.__desc, "valor":self.__valor}
        return dic
    
    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["desc"], dic["valor"])
    
    def __str__(self):
        return f"{self.__id} - {self.__desc} - {self.__valor}"
    
class ServicoDAO:
    __objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id: id = aux.get_id()
            obj.set_id(id+1)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.salvar()
    
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("servicos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Servico.to_json)
            