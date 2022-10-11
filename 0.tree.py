import time
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans_inorderTraversal_recursion = []

    def preorder(self, root):
        return [root.val] + self.preorder(root.left) + self.preorder(root.right) if root else []

    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

    def postorder(self, root):
        return self.postorder(root.left) + self.postorder(root.right) + [root.val] if root else []

    def inorderTraversal_recursion(self, root) -> list[int]:
        if not root:
            return
        if root.left:
            self.inorderTraversal_recursion(root.left)
        self.ans_inorderTraversal_recursion.append(root.val)
        if root.right:
            self.inorderTraversal_recursion(root.right)
        return self.ans_inorderTraversal_recursion

    def inorderTraversal_notrecursion(self, root) -> list[int]:
        if not root:
            return
        output, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                output.append(node.val)
                root = node.right
        return output

    def postOrderTraversal_notrecursion(self, root) -> list[int]:
        WHITE, GREY = 0, 1
        stack = [(WHITE, root)]
        ans = []
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            elif color == WHITE:
                stack.append((WHITE, node.left))
                stack.append((GREY, node))
                stack.append((WHITE, node.right))
            else:
                ans.append(node.val)
        return ans

    def dfs(self, root) -> list[int]:
        if not root:
            return
        output, stack = [], [root]
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.left:
                stack.append(node.right)
        return output

    def bfs(self, root) -> list[int]:
        if not root:
            return
        output, queue = [], deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            output.append(node.val)
        return output

    def levelOrder(self, root) -> list[int]:
        if not root:
            return
        ans, queue = [], [root]
        while queue:
            ans.append([node.val for node in queue])
            queue = [(node.left, node.right) for node in queue]
            queue = [lf for lfPair in queue for lf in lfPair if lf]
        return ans

    def levelOrder2(self, root) -> list[int]:
        if not root:
            return
        ans, queue, subresult = [], deque([root]), []
        level, nodeOfLevel = 1, 1
        while (queue):
            node = queue.popleft()
            subresult.append(node.val)
            level -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if level == 0:
                level = len(queue)
                ans.append(subresult)
                subresult = []
        return ans

    def invertBinaryTree(self, tree):
        stack = [tree]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return tree     

    def binaryTreeDiameter(self, tree):
        def longestPath(tree):
            global ans
            if not tree:
                return 0
            leftDepth = longestPath(tree.left)
            rightDepth = longestPath(tree.right)
            ans = max(ans, leftDepth+rightDepth)
            return max(leftDepth, rightDepth) + 1            

        global ans 
        ans = 0
        longestPath(tree)
        return ans



time1 = time.time()

a = TreeNode(3)
b = TreeNode(2, left=None, right=a)
c = TreeNode(-10)
d = TreeNode(-2, left=None, right=None)
d = TreeNode(-5, left=c, right=d)
root = TreeNode(1, left=d, right=b)

pro = Solution()
print(pro.inorderTraversal_notrecursion(root))
print(pro.postOrderTraversal_notrecursion(root))
print(pro.preorder(root))
print(pro.inorder(root))
print(pro.postorder(root))
print(pro.dfs(root))
print(pro.bfs(root))
print(pro.levelOrder(root))
print(pro.levelOrder2(root))


print(pro.binaryTreeDiameter(root))

time2 = time.time()
print(time2-time1)
