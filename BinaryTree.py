# define TreeNode with rightChild, LeftChild and data variable
# inset function : if income data is bigger than root, insert new node on right side
# and if income data is smaller than root, insert new node on left side
# printTree : we are pass tree untill last left node and print these from last to root
# and print right childs to end

class TreeNode:
    def __init__(self, data):
        self.rightChild = None
        self.leftChild = None
        self.data = data

    def insert(self, data):
        if self.data:
            if self.data < data:
                if self.rightChild is None:
                    self.rightChild = TreeNode(data)
                else:
                    self.rightChild.insert(data)
            elif self.data > data:
                if self.leftChild is None:
                    self.leftChild = TreeNode(data)
                else:
                    self.leftChild.insert(data)
        else:
            self.data = data

    def SearchIn(self, data):
        if self.data < data:
            if self.rightChild is None:
                return str(data)+"Not Found"
            return self.rightChild.SearchIn(data)
        elif self.data > data:
            if self.leftChild is None:
                return str(data)+"Not Found"
            return self.leftChild.SearchIn(data)
        else:
            return str(self.data)+" Is Found"

    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print(self.data)
        if self.rightChild:
            self.rightChild.PrintTree()

    def PrintRoot(self):
        print(self.data)


root = TreeNode(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.insert(16)
root.insert(13)
root.insert(11)

root.PrintTree()
print("________-")
root.PrintRoot()

print("________-")
print(root.SearchIn(16))
