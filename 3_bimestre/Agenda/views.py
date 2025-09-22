from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO

class View:
    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_inserir(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente,)
    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente)
    def cliente_excluir(id):
        cliente = Cliente(id, '', '', '')
        ClienteDAO.excluir(cliente)
 
    def servico_listar():
        return ServicoDAO.listar()
    def servico_inserir(desc, valor):
        servico = Servico(0, desc, valor)
        ServicoDAO.inserir(servico)
    def servico_atualizar(id, desc, valor):
        servico = Servico(id, desc, valor)
        ServicoDAO.atualizar(servico)
    def servico_excluir(id):
        servico = Servico(id, "", "", "" )
        ServicoDAO.excluir(servico)
