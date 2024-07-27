mylist = [1,2,4,8,1,9]

def condup():
    haset = set()
    for n in mylist:
        if n in haset:
            return True
        haset.add(n)
    return False

print(condup())
            