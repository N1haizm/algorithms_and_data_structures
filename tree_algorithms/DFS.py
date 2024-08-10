'''
This code is copy of the code in ./tree&recursion/tree_insert_method.py . 
Plus, DFS methods added to code.
'''

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binarySearchTree():
    def __init__(self):
        self.root = None
    
    # DFS (PRE ORDER)

    def DFSpreOrder(self):
        values = []
        
        def traverse(currentNode):
            # The line below replaces 3 times for 3 dfs methods
            values.append(currentNode.value)

            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
        
        traverse(self.root)
        
        return values
    
    # DFS (POST ORDER)

    def DFSpostOrder(self):
        values = []
        
        def traverse(currentNode):

            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
            # The line below replaces 3 times for 3 dfs methods
            values.append(currentNode.value)
        
        traverse(self.root)
        
        return values

    # DFS (IN ORDER)
    
    def DFSinOrder(self):
        values = []
        
        def traverse(currentNode):

            if currentNode.left is not None:
                traverse(currentNode.left)
            # The line below replaces 3 times for 3 dfs methods
            values.append(currentNode.value)

            if currentNode.right is not None:
                traverse(currentNode.right)
        
        traverse(self.root)
        
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
myTree.insert(12)
myTree.insert(6)
myTree.insert(72)
myTree.insert(59)
myTree.insert(95)
myTree.insert(24)
myTree.insert(100)
myTree.insert(92)
myTree.insert(62)
myTree.insert(54)
myTree.insert(30)
myTree.insert(20)
myTree.insert(9)
myTree.insert(3)

print(myTree.DFSpreOrder())
print(myTree.DFSpostOrder())
print(myTree.DFSinOrder())


        

        