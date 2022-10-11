# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.


from collections import deque


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        node = self
        while node:
            if node.value== value:
                return self
            elif node.value< value:
                if not node.right:
                    node.right = BST(value)
                    break
                node = node.right

            elif node.value> value:
                if not node.left:
                    node.left = BST(value)
                    break
                node = node.left
        return self
    
    def consMinHeight(self, array):
        left, right = 0, len(array) - 1
        mid = (left + right) // 2
        if left > right:
            return
        node = BST(array[mid])
        node.left = self.consMinHeight(array[:mid])
        node.right = self.consMinHeight(array[mid+1:])
        return node

    def contains(self, value):
        # Write your code here.
        node = self
        while node:
            if node.value== value:
                return True
            elif node.value< value:
                node = node.right
            elif node.value> value:
                node = node.left
        return False

    def remove(self, value, parentNode=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        parentNode, node = self.GetFirst(value, parentNode)

        if not node:
            return
        if self.IsOnlyNode(parentNode, node):
            return

        if node.right:
            repNode = node.right.GetMinNode(parentNode)
            node.value = repNode.value
            node.right.remove(repNode.value, node)

        elif node.left is None and node.right is None:
            if parentNode.left == node:
                parentNode.left = None
            elif parentNode.right == node:
                parentNode.right = None
        elif node.left:
            repNode = node.left.GetMaxNode(parentNode)
            node.value= repNode.val
            node.left.remove(repNode.val, node)

        return self

    def GetMinNode(self, parentNode=None):
        minParent = node = self
        while node:
            minParent = node
            node = node.left
        return minParent

    def GetMaxNode(self, parentNode=None):
        node = self
        while node.right:
            parentNode = node
            node = node.right
        return node

    def IsOnlyNode(self, value, parentNode=None):
        return parentNode is None and node.left is None and node.right is None

    def GetFirst(self, value, parentNode=None):
        node = self
        while node is not None:
            if value == node.value:
                return parentNode, node
            elif node.value< value:
                parentNode = node
                node = node.right

            elif node.value> value:
                parentNode = node
                node = node.left
        return None, None

    def validateBst(self, tree, leftParent = None, rightParent = None):
        # Write your code here.
        if tree is None:
            return True
        elif leftParent is not None and tree.value >= leftParent.value:
            return False
        elif rightParent is not None and tree.value < rightParent.value:
            return False
        return self.validateBst(tree.left, tree, rightParent) and self.validateBst(tree.right, leftParent, tree)

    def inOrderTraverse(self, tree):
        array=[]
        # Write your code here.
        Blue, Gray = 1, 0
        stack = [(Gray, tree)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color:
                array.append(node.value)
            else:
                stack.append((Gray, node.right))
                stack.append((Blue, node))
                stack.append((Gray, node.left))
        return array

    def preOrderTraverse(self, tree):
        array=[]
        # Write your code here.
        Blue, Gray = 1, 0
        stack = [(Gray, tree)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color:
                array.append(node.value)
            else:
                stack.append((Gray, node.right))
                stack.append((Gray, node.left))
                stack.append((Blue, node))
        return array

    def postOrderTraverse(self, tree):
        array=[]
        # Write your code here.
        Blue, Gray = 1, 0
        stack = [(Gray, tree)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color:
                array.append(node.value)
            else:
                stack.append((Blue, node))
                stack.append((Gray, node.right))
                stack.append((Gray, node.left))
        return array

    def reconstructBst(self, preOrderTraversalValues):
        if not preOrderTraversalValues:
            return
        node = BST(preOrderTraversalValues[0])
        i = 1
        for i in range(1, len(preOrderTraversalValues)+1):
            if i == len(preOrderTraversalValues) or preOrderTraversalValues[i] >= preOrderTraversalValues[0]:
                break
        node.left = self.reconstructBst(preOrderTraversalValues[1:i])
        node.right = self.reconstructBst(preOrderTraversalValues[i:])
        return node

root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)
# 1 2  5  5   10     13 14  15  22

root.insert(12)
print(root.right.left.left.value== 12)

root.remove(10)
print(not root.contains(10))
print(root.value== 12)

print(root.contains(15))
print(root.validateBst(root))
print(root.postOrderTraverse(root))
print(root.preOrderTraverse(root))
print(root.inOrderTraverse(root))
tree = root.reconstructBst([10, 4, 2, 1, 5, 17, 19, 18])

print(tree)




