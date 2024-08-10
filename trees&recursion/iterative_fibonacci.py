# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2) and n>1

def iterativeFibonacci(n):
    x, y = 0,1

    for i in range(n):
        x,y = y, x+y
        print(x)
        print(y)
    
    return x

print(iterativeFibonacci(5))



