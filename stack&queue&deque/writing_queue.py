# Writing Queue using Lists

class Queue():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
        
    def enqueue(self,item):
        self.items.append(item)
        return self.items
    
    def dequeue(self):
        return self.items.pop(0)
    
    def showLast(self):
        return self.items[-1]
        
    def size(self):
        return len(self.items)
    

'''
Queue
enqueue
dequeue
'''

myQueue = Queue()
print(myQueue.enqueue(10))
print(myQueue.enqueue(20))
print(myQueue.dequeue())