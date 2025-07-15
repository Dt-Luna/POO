'''Calcular a média parcial de uma disciplina semestral, dadas as notas dos 1o e 2o bimestres (pesos 2 e 3).
Considerar as notas com valores inteiros entre zero e cem.
Digite a nota do primeiro bimestre da disciplina:
50
Digite a nota do segundo bimestre da disciplina:
70
Média parcial = 62'''

primeiro_bimestre = int(input('Digite a nota do primeiro bimestre da disciplina:\n'))
segundo_bimestre = int(input('Digite a nota do segundo bimestre da disciplina:\n'))
media = (2 * primeiro_bimestre + 3 * segundo_bimestre) / 5
print(f'Média parcial = {media}')
 