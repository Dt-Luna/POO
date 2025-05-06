<<<<<<< HEAD
a, b, c = float(input()), float(input()), float(input())
if (b**2 - 4 * a * c) < 0 or 2*a == 0:
    print('Impossível calcular')
else:
    print(f'R1: {(-b + (b**2 - 4 * a * c))/2 * a:.2f}')
    print(f'R2: {(-b - (b**2 - 4 * a * c))/2 * a:.2f}')
=======
t = input()
t = t.split()
a = float(t[0])
b = float(t[1])
c = float(t[2])
delta = b**2 - 4 * a * c
if delta < 0 or 2*a == 0:
    print('Impossivel calcular')
else:
    print(f'R1 = {(-b + (delta ** 0.5)) / (2*a):.5f}')
    print(f'R2 = {(-b - (delta ** 0.5)) / (2*a):.5f}')
>>>>>>> 52d1696a75f418c2d933b8a975553bd92a9f0165
