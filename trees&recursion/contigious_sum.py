def conSum(num):
    if num == 0:
        return 0
    else:
        return num + conSum(num-1)
    
print(conSum(7))