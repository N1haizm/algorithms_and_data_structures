import math

def logO(n):
    while n > 1:
        n = math.floor(n/2)
        print(n)

logO(32)