t = input()
t = t.split()
x = int(t[0])
y = int(t[1])
if (x >= 0 and y>=0) and (x <= 432 and y <= 468):
    print('dentro')
else:
    print('fora')