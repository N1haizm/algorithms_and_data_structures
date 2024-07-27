mylist = [1,2,3,6,9,3]

# Short version of "condup_example0.py"

def condup():
    return len(mylist) != len(set(mylist))

print(condup())