#Writing stack using Lists

class Stack():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
        
    def push(self,item):
        self.items.append(item)
        return self.items
    
    def pop(self):
        return self.items.pop()
    
    def showLast(self):
        return self.items[-1]
        
    def size(self):
        return len(self.items)

myStack = Stack()
print(myStack.isEmpty())
print(myStack.size())
print(myStack.push(10))
print(myStack.push(20))
print(myStack.pop())
print(myStack.isEmpty())