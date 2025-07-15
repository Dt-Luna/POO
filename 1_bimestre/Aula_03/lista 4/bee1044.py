t = input()
t = t.split()
a = float(t[0])
b = float(t[1])
if a%b == 0 or b%a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
