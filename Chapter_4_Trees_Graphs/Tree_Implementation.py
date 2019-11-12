class TreeNode:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# 1) Visit root
#
# 2) Visit left sub-tree
#
# 3) Visit right sub-tree

    def PreorderTraversal(self, root):  # root --> left --> right
        result = []
        if root:
            result.append(root.data)
            result = result + self.PreorderTraversal(root.left)
            result = result + self.PreorderTraversal(root.right)
        return result

# 1) Visit left sub-tree
#
# 2) Visit root
#
# 3) Visit right sub-tree

    def inorderTraversal(self,root):
        result = []
        if root:
            result = self.inorderTraversal(root.left)
            result.append(root.data)
            result = result + self.inorderTraversal(root.right)
        return result

# 1) Visit left sub-tree
#
# 2) Visit right sub-tree
#
# 3) Visit root

    def PostorderTraversal(self, root):
        result = []
        if root:
            result = self.PostorderTraversal(root.left)
            result = result + self.PostorderTraversal(root.right)
            result.append(root.data)
        return result



    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


root = TreeNode(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(5)
root.insert(11)
root.insert(8)
root.insert(9)
root.insert(15)
root.insert(13)

# root = TreeNode(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)

# root.printTree()

print("PreOrder = ", root.PreorderTraversal(root))

print("InOrder = ", root.inorderTraversal(root))

print("PostOrder = ", root.PostorderTraversal(root))