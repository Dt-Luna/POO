def Senha(texto):
    senha = []
    texto = texto.split()
    for i in texto:
        senha.append(len(i))
    return