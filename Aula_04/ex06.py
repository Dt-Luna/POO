def Frete(massa, distancia):
    return(massa*distancia*0.01)

print(f'R${Frete(15, 30):.2f}')