from datetime import datetime
import json
from models.dao import DAO
class Especialidade:
    def __init__(self, id, nome):
        self.set_id(id)
        self.set_nome(nome)
        
    def set_id(self, id): 
        self.__id = id
    def set_nome(self,nome):
        if nome=='': raise ValueError('Nome inválido')
        self.__nome = nome
        
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome


    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome}
        return dic
    
    def __str__(self):
        return f"{self.__id} - {self.__nome}"

    @staticmethod
    def from_json(dic):
        return Especialidade(dic["id"], dic["nome"])
        
class EspecialidadeDAO(DAO):
    _objetos = []
    arquivo = "especialidades.json"
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("especialidades.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Especialidade.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("especialidades.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Especialidade.to_json)




            