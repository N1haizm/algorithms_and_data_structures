class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binarySearchTree():
    def __init__(self):
        self.root = None
    
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
print(myTree.insert(5))
print(myTree.insert(15))
print(myTree.insert(10))
print(myTree.insert(30))
print(myTree.insert(31))
print(myTree.insert(6))

print(myTree.minOfNode(myTree.root.right))
print(myTree.maxOfNode(myTree.root))
            


        

        