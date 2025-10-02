from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.profisional import Profissional, ProfissionalDAO

class View:
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return 
        View.cliente_inserir("admin", "admin", "fone", "1234")
    
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha: return {"id": c.get_id(), "nome": c.get_nome()}
        return None

    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente,)
    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)
    def cliente_excluir(id):
        cliente = Cliente(id, '', '', '', '')
        ClienteDAO.excluir(cliente)
    def cliente_listar_id(id):
        cliente = ClienteDAO.listar_id(id)
        return cliente
 
    def servico_listar():
        return ServicoDAO.listar()
    def servico_inserir(desc, valor):
        servico = Servico(0, desc, valor)
        ServicoDAO.inserir(servico)
    def servico_atualizar(id, desc, valor):
        servico = Servico(id, desc, valor)
        ServicoDAO.atualizar(servico)
    def servico_excluir(id):
        servico = Servico(id, "", "" )
        ServicoDAO.excluir(servico)
    def servico_listar_id(id):
        servico = ServicoDAO.listar_id(id)
        return servico

    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.inserir(c)
    def horario_listar():
        return HorarioDAO.listar()  
    def horario_listar_id(id):
        horario = HorarioDAO.listar_id(id)
        return horario
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(c)
    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)

    def profissional_listar():
        return ProfissionalDAO.listar()
    def profissional_inserir(nome, especialidade, conselho):
        profissional = Profissional(0, nome, especialidade, conselho)
        ProfissionalDAO.inserir(profissional)
    def profissional_atualizar(id, nome, especialidade, conselho):
        profissional = Profissional(id, nome, especialidade, conselho)
        ProfissionalDAO.atualizar(profissional)
    def profissional_excluir(id):
        profissional = Profissional(id, '', '', '')
        ProfissionalDAO.excluir(profissional)
    def profissional_listar_id(id):
        profissional = ProfissionalDAO.listar_id(id)
        return profissional
    