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

    def to_dict(self):
        dic = {"id":self.__id, "desc":self.__desc, "valor":self.__valor}
        return dic
    
    @staticmethod
    def from_dict(dic):
        return Servico(dic["id"], dic["desc"], dic"[valor"])
    
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

    @classmethod
    def atualizar(cls, obj):