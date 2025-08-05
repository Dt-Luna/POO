from models import Contato, ContatoDAO
import datetime

class View:
    @staticmethod
    def contato_inserir(nome, email, fone, aniversario):
        if isinstance(aniversario, str):
            print(aniversario, type(aniversario))
            aniversario = datetime.datetime.strptime(aniversario, '%d/%m')
            print(aniversario, type(aniversario))
        ContatoDAO.inserir(Contato(0, nome, email, fone, aniversario))
        return True
        #  except Exception as e:
        #     print(f'Erro ao inserir contato: {e}')
        #     return False
    
    @staticmethod
    def contato_listar():
        ContatoDAO.listar()

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