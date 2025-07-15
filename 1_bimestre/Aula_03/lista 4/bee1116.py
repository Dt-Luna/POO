n = int(input())
for i in range (1, n+1):
    v = input()
    lv = v.split()
    for a in range(0, len(lv)):
        lv[a] = float(lv[a])
    if lv[1] == 0:
        print('impossivel calcular')
    else:
        print(round(lv[0] / lv[1], 1))
    