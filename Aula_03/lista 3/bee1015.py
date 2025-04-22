import math
um = input()
dois = input()
um = um.split()
dois = dois.split()
x1 = um[0]
y1 = um[1]
x2 = dois[0]
y2 = dois[1]
print(math.sqrt((x2 - x1) ** 2 + (y2  - y1) ** 2))