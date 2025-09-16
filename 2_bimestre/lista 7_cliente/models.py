class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

    def __str__(self):
        return f'{self.id} - {self.nome} - {self.email} - {self.fone}'
    
class ClienteDAO:
    __clientes = []
    @classmethod
    def inserir(cls, obj):
        for c