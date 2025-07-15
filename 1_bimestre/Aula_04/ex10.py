def Palavra(texto, pos):
    pz = pos
    while texto[pos] != ' ':
        pos +=1
    pf = pos
    return(texto[pz:pf])

print(Palavra('OIIII POR QUE VOCE NAO SE MATA =)', 6))

        