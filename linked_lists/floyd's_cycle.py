nums = list[1,2,3,4,4]

def cycle(list):
    slowP = 0
    fastP = 0

    while True:
        slowP = list[slowP]
        fastP = list[list[fastP]]
        if slowP == fastP:
            break
    
    secondSlowP = 0

    while True:
        slowP = list[slowP]
        secondSlowP = list[secondSlowP]
        if slowP == secondSlowP:
            break
    
    return slowP
    

print(cycle(nums))