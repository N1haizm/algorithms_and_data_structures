mylist = [2,1,2,2,1,5,2,6,2,2,2]

# Boyer Moore Algorithm

def majelm():
    result = 0
    count = 0
    for n in mylist:
        if count == 0:
            result = n
        if n == result:
            count +=1
        else:
            -1
    return result
   
    
print(majelm())