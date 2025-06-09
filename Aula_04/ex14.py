def UltimoDia(mes, ano):
    mes31 = ['janeiro', 'março', 'maio', 'julho', 'agosto', 'outubro', 'dezembro']
    mes30 = ['abril', 'junho', 'setembro', 'novembro']
    if ano%4 == 0 and mes=='fevereiro':
        dia = 29
    elif ano%4 != 0 and mes=='fevereiro':
        dia = 28
    if mes in mes31:
        dia = 31
    if mes in mes30:
        dia = 30
    return dia

print(UltimoDia('fevereiro', 2004))
print(UltimoDia('março', 2004))