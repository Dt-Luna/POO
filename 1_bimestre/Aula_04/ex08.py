def Soma(inicio, fim):
    soma = 0
    while inicio != fim+1:
        soma += inicio
        inicio += 1
    return soma

print(Soma(1, 5))