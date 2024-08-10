'''
This code is copy of the code in ./tree&recursion/tree_insert_method.py . 
Plus, BFS method added to code.
'''

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binarySearchTree():
    def __init__(self):
        self.root = None

    #BFS

    def BFS(self):
        currentNode = self.root
        myQueue = []
        values = []
        myQueue.append(self.root)

        while len(myQueue) > 0:
            currentNode = myQueue.pop(0)
            values.append(currentNode.value)
            if currentNode.left is not None:
                myQueue.append(currentNode.left)
            if currentNode.right is not None:
                myQueue.append(currentNode.right)
        return values


    
    def insert(self, value):

        newNode = Node(value)

        if self.root is None:
            self.root = newNode
            return True
        
        tempN = self.root
        
        while True:
            if newNode.value == tempN.value:
                return False

            if newNode.value < tempN.value:
                if tempN.left is None:
                    tempN.left = newNode
                    return True
                
                tempN = tempN.left
            else:
                if tempN.right is None:
                    tempN.right = newNode
                    return True

                tempN = tempN.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def minOfNode(self, crrntNode):
        while crrntNode.left:
            crrntNode = crrntNode.left
        return crrntNode.value
    
    def maxOfNode(self, crrntNode):
        while crrntNode.right:
            crrntNode = crrntNode.right
        return crrntNode.value

myTree = binarySearchTree()
myTree.insert(40)
myTree.insert(72)
myTree.insert(12)
myTree.insert(24)
myTree.insert(59)
myTree.insert(95)
myTree.insert(19)
print(myTree.BFS())