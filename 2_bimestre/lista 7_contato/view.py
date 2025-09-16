from models import Contato, ContatoDAO
import datetime

class View:
    @staticmethod
    def contato_inserir(nome, email, fone, aniversario):
        try:
            if isinstance(aniversario, str):
                aniversario = datetime.datetime.strptime(aniversario, '%d/%m')
            ContatoDAO.inserir(Contato(0, nome, email, fone, aniversario))
            return True
        except Exception as e:
           print(f'Erro ao inserir contato: {e}')
    
    @staticmethod
    def contato_listar():
        return ContatoDAO.listar()

    @staticmethod
    def contato_listar_id(id):
        ContatoDAO.listar_id(id)

    @staticmethod
    def contato_excluir(id):
        # for obj in ContatoDAO.__contatos:
        #     if obj.get_id == id:
        ContatoDAO.excluir(id)
            # else: return False

    @staticmethod
    def contato_atualizar(id, nome, email, fone, aniversario):
        aniversario = datetime.datetime.strptime(aniversario, '%d/%m')
        ContatoDAO.atualizar(id, nome, email, fone, aniversario)

    @staticmethod
    def contato_listar_id(id):
        for c in ContatoDAO.listar():
            if c.get_id() == id:
                return c

    @staticmethod
    def contato_aniversariantes(mes):
        mes = datetime.datetime.strptime(mes, '%m')
        print(mes)
        for c in ContatoDAO.listar():
            print(c.get_aniversario().month)
            if c.get_aniversario().month == mes.month:
                return c
        
    @staticmethod
    def contato_salvar():
        ContatoDAO._salvar()

    @staticmethod
    def contato_abrir():
        ContatoDAO._abrir()
    