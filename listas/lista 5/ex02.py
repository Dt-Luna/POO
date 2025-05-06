def maior(x, y, z):
    ls=[]
    ls.append(x)
    ls.append(y)
    ls.append(z)
    return(max(ls))

x, y, z = int(input()), int(input()), int(input())
print(maior(x, y, z))