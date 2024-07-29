mylist = [2,6,2,9,6]

# Bit Manipulation

def finsin():
    result=0
    for i in mylist:
        result = i ^ result
    return result

print(finsin())