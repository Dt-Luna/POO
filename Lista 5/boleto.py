import enum
import datetime

class Pagamento(enum.Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3

    def __str__(self):
        return self.name.capitalize()

class Boleto:
    def __init__(self, cod, dte, dtv, vb):
        self.set_codigo(cod)
        self.set_dtemissao(dte)
        self.set_dtvencimento(dtv)
        self.set_vboleto(vb)
        self.__vpago = 0.0
        self.__dtpagamento = None

    def set_codigo(self, cod):
        if type(cod) != str:
            raise ValueError('Código deve ser uma string')
        self.__codigo = cod

    def set_dtemissao(self, dte):
        self.__dtemissao = dte

    def set_dtvencimento(self, dtv):
        self.__dtvencimento = dtv

    def set_dtpagamento(self, dtp):
        self.__dtpagamento = dtp

    def set_vboleto(self, vb):
        self.__vboleto = vb

    def set_vpago(self, vp):
        self.__vpago = vp

    def get_codigo(self):
        return self.__codigo

    def get_dtvencimento(self):
        return self.__dtvencimento

    def get_dtemissao(self):
        return self.__dtemissao

    def get_dtpagamento(self):
        return self.__dtpagamento

    def get_vboleto(self):
        return self.__vboleto

    def get_vpago(self):
        return self.__vpago

    def pagar(self, valor):
        if valor <= 0:
            print('Valor de pagamento deve ser maior que zero.')
            return
        self.__vpago += valor
        if self.__vpago > self.__vboleto:
            print(f'Valor pago excede o valor do boleto. Ajustando para {self.__vboleto}.')
            self.__vpago = self.__vboleto
        if self.__vpago == self.__vboleto:
            self.__dtpagamento = datetime.datetime.now()

    def situacao(self):
        if self.__vpago == 0:
            return Pagamento.EmAberto
        elif 0 < self.__vpago < self.__vboleto:
            return Pagamento.PagoParcial
        else:  # self.__vpago == self.__vboleto
            return Pagamento.Pago

    def __str__(self):
        dtpag = self.__dtpagamento.strftime('%d/%m/%Y %H:%M:%S') if self.__dtpagamento else 'Não pago'
        return (f'Código: {self.__codigo} | Emissão: {self.__dtemissao.strftime("%d/%m/%Y")} | '
                f'Vencimento: {self.__dtvencimento.strftime("%d/%m/%Y")} | Valor: R${self.__vboleto:.2f} | '
                f'Pago: R${self.__vpago:.2f} | Situação: {self.situacao()} | Data Pagamento: {dtpag}')

class BoletoUI:
    __boletos = []

    @staticmethod
    def menu():
        print('1 - Inserir boleto')
        print('2 - Ver boletos')
        print('3 - Pagar boleto')
        print('4 - Sair')
        opcao = input('Escolha uma opção: ')
        if opcao.isdigit():
            return int(opcao)
        else:
            return 0

    @classmethod
    def main(cls):
        while True:
            opcao = cls.menu()
            if opcao == 1:
                cls.inserir()
            elif opcao == 2:
                cls.listar()
            elif opcao == 3:
                cls.pagar()
            elif opcao == 4:
                print('Saindo...')
                break
            else:
                print('Opção inválida!')

    @classmethod
    def inserir(cls):
        try:
            codigo = input('Digite o código do boleto: ')
            dtemissao = input('Digite a data de emissão (dd/mm/aaaa): ')
            dtemissao = datetime.datetime.strptime(dtemissao, '%d/%m/%Y')
            dtvencimento = input('Digite a data de vencimento (dd/mm/aaaa): ')
            dtvencimento = datetime.datetime.strptime(dtvencimento, '%d/%m/%Y')
            valor = float(input('Digite o valor do boleto: '))
            boleto = Boleto(codigo, dtemissao, dtvencimento, valor)
            cls.__boletos.append(boleto)
            print('Boleto inserido com sucesso.')
        except ValueError:
            print('Informações inválidas, tente novamente.')

    @classmethod
    def listar(cls):
        if not cls.__boletos:
            print('Nenhum boleto cadastrado.')
            return
        for b in cls.__boletos:
            print(b)

    @classmethod
    def pagar(cls):
        if not cls.__boletos:
            print('Nenhum boleto para pagar.')
            return
        cls.listar()
        codigo = input('Digite o código do boleto a ser pago: ')
        boleto_encontrado = None
        for b in cls.__boletos:
            if b.get_codigo() == codigo:
                boleto_encontrado = b
                break
        if not boleto_encontrado:
            print('Boleto não encontrado.')
            return
        situacao = boleto_encontrado.situacao()
        if situacao == Pagamento.Pago:
            print('O boleto já foi totalmente pago.')
            return
        try:
            valor = float(input('Qual o valor a ser pago? R$ '))
            boleto_encontrado.pagar(valor)
            print('Pagamento efetuado com sucesso.')
            print(boleto_encontrado)
        except ValueError:
            print('Valor inválido.')

if __name__ == "__main__":
    BoletoUI.main()
