class doubleNode():
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

first = doubleNode(1)
second = doubleNode(2)
third = doubleNode(3)

# for first node 
first.next = second

# for second node
second.previous = first
second.next = third

# for third node
third.previous = second

print(second.next.previous.previous.value)