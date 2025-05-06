def nome(n):
    n = n.split()
    for i in range(0, len(n)):
        n[i] = (n[i])[0]
    return(n)

n = input()
print(*nome(n))



