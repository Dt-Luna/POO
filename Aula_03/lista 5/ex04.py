def aprovado(n1, n2):
    if (n1 + n2) / 2 >= 60:
        return True
    else:
        return False
    
x, y = int(input()), int(input())
print(aprovado(x, y))