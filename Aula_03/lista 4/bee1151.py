n = int(input())
ls = [0, 1]
for i in range(0, n-2):
    ls.append(ls[i]+ls[i+1])
print(*ls)