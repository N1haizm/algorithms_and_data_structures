# Writing deque using Lists

class Deque():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addLeft(self,item):
        self.items.insert(0,item)
        return self.items
        
    def addRight(self,item):
        self.items.append(item)
        return self.items
        
    def remove(self):
        return self.items.pop()
    
    def removeLeft(self):
        return self.items.pop(0)
    
    def showLast(self):
        return self.items[-1]
        
    def size(self):
        return len(self.items)

myDeque = Deque()
print(myDeque.addRight(2))
print(myDeque.addLeft(3))
print(myDeque.removeLeft())
print(myDeque.remove())