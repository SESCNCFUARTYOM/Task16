from functools import *
import math
from sys import *

setrecursionlimit(115000)
@lru_cache()

def f(n):
    if (n**0.5) % 1 == 0:
        return n**0.5
    else:
        return f(n+1) + 1

print(f(114850) + f(115000))
    
