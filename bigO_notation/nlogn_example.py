import math

def nlogn(n):
    limit = n
    while n > 1:
        n = math.floor(n/2)
        for i in range(0,limit):
            print(i)

nlogn(8)