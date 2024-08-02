class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

first = Node(100)
second = Node(200)
third = Node(300)

first.next = second
second.next = third 

print(first.next.next.value)