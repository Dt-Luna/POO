import datetime
class Treino:
    def __init__(self, id, dt, ds, t):
        self.set_id(id)
        self.set_dthora(dt)
        self.set_distancia(ds)
        self.set_tempo(t)
    
    def set_id(self, id):
        self.__id = id

    def set_dthora(self, dt):
        self.__dthora = dt
    
    def set_distancia(self, ds):
        self.__ds = ds
    
    def set_tempo(self, t):
        self.__t = t

    def get_id(self):
        return self.__id

    def get_dthora(self):
        return self.__dthora

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo
    
    def velocidade(self):
        return self.__distancia/self.__tempo.seconds

    def __str__(self):
        return f'{self.__id} - Treino às {self.__dthora} - {self.__distancia}m em {self.__tempo}'

class TreinoUI:
    __treinos = []
    @staticmethod
    def menu():
        print('1-Inserir, 2-Listar todos, 3-Listar por id, 4-Atualizar, 5-Excluir, 6-Mais rápido, 7-Fim')
        opcao = int(input('Escolha uma opção: '))
        return opcao
    
    @staticmethod
    def main():
        while True:
            opcao = TreinoUI.menu()
            if opcao == 1: TreinoUI.inserir()
            elif opcao == 2: TreinoUI.listar()
            elif opcao == 3: TreinoUI.listar_id()
            elif opcao == 4: TreinoUI.atualizar()
            elif opcao == 5: TreinoUI.excluir()
            elif opcao == 6: TreinoUI.mais_rapido()
            elif opcao == 7: break
            else: print('Opção inválida')

    @classmethod
    def inserir(cls):
        if not cls.__treinos:
            id_numero = 0
        id += id_numero
        dt = input('Data do treino: ')
        dt = datetime.datetime.strptime(dt, '%d/%m/%Y %H:%M')
        ds = float(input('Distância percorrida: '))
        h, m ,s = map(int, input('Tempo percorrido: ').oplit(':'))
        t = datetime.timedelta(hours = h, minutes = m, seconds = s)
        x = Treino(id, dt, ds, t)
        id_numero += 1

    @classmethod
    def listar(cls):
        for t in cls.__treinos:
            print(t)

    @classmethod
    def listar_id(cls):
        id = int(input('id do treino: '))
        for t in cls.__treinos:
            if id == t.get_id():
                print(t)

    @classmethod
    def atualizar(cls):
        id = int('Id do treino a ser atualizado: ')
        for t in cls.__treinos:
            if t.get_id() == id:
                
        
