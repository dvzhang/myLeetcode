# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.


class BST:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        node = self
        while node:
            if node.val == value:
                return self
            elif node.val < value:
                if not node.right:
                    node.right = BST(value)
                    break
                node = node.right
    
            elif node.val > value:
                if not node.left:
                    node.left = BST(value)
                    break
                node = node.left
        return self

    def contains(self, value):
        # Write your code here.
        node = self
        while node:
            if node.val == value:
                return True
            elif node.val < value:
                node = node.right
            elif node.val > value:
                node = node.left
        return False
        

    def remove(self, value, parentNode = None):
        # Write your code here.
        # Do not edit the return statement of this method.
        parentNode, node = self.GetFirst(value, parentNode)

        if not node:
            return 
        if self.IsOnlyNode(parentNode, node):
            return

        if node.right:
            repNode = node.right.GetMinNode(parentNode)
            node.val = repNode.val
            node.right.remove(repNode.val, node)

        elif node.left is None and node.right is None:
            if parentNode.left == node:
                parentNode.left = None
            elif parentNode.right == node:
                parentNode.right = None
        elif node.left:
            repNode = node.left.GetMaxNode(parentNode)
            node.val = repNode.val
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
            if value == node.val:
                return parentNode, node
            elif node.val < value:
                parentNode = node
                node = node.right
                
            elif node.val > value:
                parentNode = node
                node = node.left
        return None, None
                



class TestProgram():
    def assertTrue(self, var):
        if not var:
            print("error:{}".format(var))
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)

        root.insert(12)
        print(root.right.left.left.val == 12)

        root.remove(10)
        print(not root.contains(10))
        print(root.val == 12)

        print(root.contains(15))

# a = TestProgram()
# a.test_case_1()

root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

root.insert(12)
print(root.right.left.left.val == 12)

root.remove(10)
print(not root.contains(10))
print(root.val == 12)

print(root.contains(15))