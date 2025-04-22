'''Ler uma frase com mais de uma palavra e mostrar sua última palavra (sem usar if – for – while – split).
Digite uma frase:
Bem-vindo(a) ao Python
Python'''

s = input('Digite uma frase:\n')
print(s[s.rindex(" ")+1: ])
