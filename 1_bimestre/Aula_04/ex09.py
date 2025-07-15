def Vogais(texto):
    ls = []
    vogais = ['a', 'e', 'i', 'o', 'u']
    for i in texto:
        if i in vogais:
            ls.append(i)
    return ls

print(*Vogais('ai pq nao sei oq nao sei oq nao sei oq oq oq la'))