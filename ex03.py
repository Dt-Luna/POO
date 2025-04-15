from math import sqrt
'''Calcular área, perímetro e diagonal de um retângulo, dados sua base e sua altura. Considerar que os valores
podem ser números reais. Mostrar o resultado com duas casas decimais.
Digite a base e a altura do retângulo
33
4
Área = 12.00 - Perímetro = 14.00 - Diagonal = 5.00'''

base = int(input('Digite a base a altura do retângulo\n'))
altura = int(input())
print(f'Área = {base * altura} - Perímetro = {2 * base + 2 * altura} - Diagonal = {sqrt(base**2 + altura**2)}')