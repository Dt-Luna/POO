vertebras = input()
classe = input()
alimentacao = input()
animal = ""
if vertebras == 'vertebrado':
    if classe == 'ave':
        if alimentacao == 'carnivoro':
            animal = 'aguia'
        elif alimentacao == 'onivoro':
            animal = 'pomba'
    elif classe == 'mamifero':
        if alimentacao == 'onivoro':
            animal = 'homem'
        elif alimentacao == 'herbivoro':
            animal = 'vaca'
elif vertebras == 'invertebrado':
    if classe == 'insetos':
        if alimentacao == 'hematofago':
            animal = 'pulga'
        elif alimentacao == 'herbivoro':
            animal = 'lagarta'
    elif classe == 'anelideo':
        if alimentacao == 'hematofago':
            animal = 'sanguessuga'
        elif alimentacao == 'onivoro':
            animal = 'minhoca'

print(animal)

