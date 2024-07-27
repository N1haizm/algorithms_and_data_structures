mylist = [1,2,4,5,4,8]

# Time Complexity -> O(n^2)
# Space Complexity -> O(1)

def condup():
    for i in range(len(mylist)):
        for j in range(i+1,len(mylist)):
            if mylist[i] == mylist[j]:
                return True
    return False

print(condup())