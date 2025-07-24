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
        self.__distancia = ds
    
    def set_tempo(self, t):
        self.__tempo = t

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
            cls.id_numero = 0
        id = cls.id_numero + 1
        try:
            dt = input('Data do treino: ')
            dt = datetime.datetime.strptime(dt, '%d/%m/%Y %H:%M')
            ds = float(input('Distância percorrida: '))
            h, m ,s = map(int, input('Tempo percorrido: ').split(':'))
            t = datetime.timedelta(hours = h, minutes = m, seconds = s)
            print(t)
            x = Treino(id, dt, ds, t)
            cls.__treinos.append(x)
            cls.id_numero += 1
        except ValueError:
            print('Informações inválidas, tente novamente')

    @classmethod
    def listar(cls):
        if not cls.__treinos:
            print('Nenhum treino cadastrado')
        else:
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
        TreinoUI.listar()
        id = int('Id do treino a ser atualizado: ')
        try:
            for t in cls.__treinos:
                if t.get_id() == id:
                    dthora = input('Nova data: ')
                    if dthora != 'M':
                        dthora = datetime.datetime.strptime(dthora, '%d/%m/%Y')
                        t.set_dthora(dthora)
                    ds = input('Nova distância: ')
                    if ds != 'M':
                        ds = float(ds)
                        t.set_distancia(ds)
                    t = input('Digite o tempo: ')
                    if t != 'M':
                        t = t.split(':')
                        t = map(int, t)
                        t = datetime.timedelta(t[0], t[1], t[2])
                        t.set_tempo(t)
        except ValueError:
            print('Informações inválidas')

    @classmethod
    def excluir(cls):
        encontrado = False
        if not cls.__treinos:
            print('Não há treinos cadastrados')
        else:
            id = int(input('Informe o id: '))
            for t in cls.__treinos:
                if t.get_id() == id:
                    encontrado = True
                    cls.__treinos.remove(t)
            if not encontrado:
                print('Treino não encontrado')

    @classmethod
    def mais_rapido(cls):
        mrapido = t[0]
        for t in cls.__treinos:
            if t.velocidade() > mrapido.velocidade():
                mrapido = t
        return mrapido


TreinoUI.main()
                
        
