def formatar_nome(nome):
    nome = nome.split()
    for i in range(0, len(nome)):
        nome[i] = nome[i].capitalize()
    return(nome)

n = input()
print(*formatar_nome(n))
