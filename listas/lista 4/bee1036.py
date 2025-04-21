a, b, c = float(input()), float(input()), float(input())
if (b**2 - 4 * a * c) < 0 or 2*a == 0:
    print('Impossível calcular')
else:
    print(f'R1: {(-b + (b**2 - 4 * a * c))/2 * a:.2f}')
    print(f'R2: {(-b - (b**2 - 4 * a * c))/2 * a:.2f}')