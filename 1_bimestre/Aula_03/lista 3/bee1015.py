<<<<<<< HEAD
import math
=======
>>>>>>> 52d1696a75f418c2d933b8a975553bd92a9f0165
um = input()
dois = input()
um = um.split()
dois = dois.split()
<<<<<<< HEAD
x1 = um[0]
y1 = um[1]
x2 = dois[0]
y2 = dois[1]
print(math.sqrt((x2 - x1) ** 2 + (y2  - y1) ** 2))
=======
um[0] = float(um[0])
um[1] = float(um[1])
dois[0] = float(dois[0])
dois[1] = float(dois[1])
print(round(((dois[0] - um[0]) ** 2 + (dois[1]  - um[1]) ** 2) ** 0.5, 4))
>>>>>>> 52d1696a75f418c2d933b8a975553bd92a9f0165
