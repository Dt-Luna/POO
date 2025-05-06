n = int(input())
c = 0
s = 0
r = 0
for i in range(1, n+1):
    teste = input()
    lt = teste.split()
    lt[0] = int(lt[0])
    if lt[1] == 'C':
        c += lt[0]
    if lt[1] == 'S':
        s += lt[0]
    if lt[1] == 'R':
        r += lt[0]
total = r + s + c
print(f'Total: {total} cobaias\nTotal de coelhos: {c}\nTotal de ratos: {r}\nTotal de sapos:{s}')
print(f'Percentual de coelhos {(c/total * 100):.2f} %\nPercentual de ratos {(r/total * 100):.2f} %\nPercentual de sapos {(s/total * 100):.2f} %')
    