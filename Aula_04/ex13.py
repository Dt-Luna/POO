def Referencia(nome):
    nome = nome.split()
    preposicoes = ['de', 'da', 'do','des', 'das', 'dos', 
                   'De', 'Da', 'Do','Des', 'Das', 'Dos', 
                   'DE', 'DA', 'DO','DES', 'DAS', 'DOS']
    iniciais = []
    for p in nome[:-1]:
        if p not in preposicoes:
            iniciais.append(p[0].upper() + ".")
    ultimo_nome = nome[len(nome)-1].upper()
    return f"{ultimo_nome}, {"".join(iniciais)}"

print(Referencia('luna de oliveira bezerril deodato'))