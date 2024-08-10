s = ['s', 'a', 'l', 'a', 'm']

def reverse(string, start: int,end: int):
    if start > end:
        return 
    string[start], string[end] = string[end], string[start]
    reverse(string, start+1, end-1)

reverse(s, 0, len(s)-1)
print(s)