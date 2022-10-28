from functools import *
from sys import *



a = [1, 1]
c = 0
for x in range(2, 1000):
    
        a.append(a[x//2] + 1) if x % 2 == 0 else a.append(a[x-3] + 3)

for x in range(len(a)):
    if a[x] == 31:
        print(x)
        break


