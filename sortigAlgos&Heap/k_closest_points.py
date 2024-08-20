import math

def kClosest(points, k):
    result = []
    for i in points:
        length = 0
        for j in i:
            length = length + math.pow(j,2)
        result.append((length, i))

    result.sort()

    result = [point for _,point in result[:k]]
    
    return result

print(kClosest([[1,3],[-2,2]],1))