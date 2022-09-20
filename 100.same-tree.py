#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def check(self, node1, node2):
        if (node1.val == node2.val) and ((not node1.left) == (not node2.left)) and ((not node1.right) == (not node2.right)):
            return True
        return False

    def isSameTree(self, p, q) -> bool:
        if not p or not q:
            if not p and not q:
                return True
            return False

        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not self.check(node1, node2):
                return False
            if node1.left:
                stack.append((node1.left, node2.left))
            if node1.right:
                stack.append((node1.right, node2.right))
        return True
    def isSameTree2(self, p, q) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree2(p.left, q.left) and self.isSameTree2(q.right, q.right)
        return p is q
# @lc code=end
import time
time1 = time.time()

a = TreeNode(3)
b = TreeNode(2, left=None, right=a)
c = TreeNode(-10)
d = TreeNode(-2, left=None, right=None)
d = TreeNode(-5, left=c, right=d)
root = TreeNode(1, left=d, right=b)

a2 = TreeNode(3)
b2 = TreeNode(2, left=None, right=a)
c2 = TreeNode(-10)
d2 = TreeNode(-2, left=None, right=None)
d2 = TreeNode(-5, left=c, right=d)
root2 = TreeNode(1, left=d, right=b)

pro = Solution()
print(pro.isSameTree(root, root2))

time2 = time.time()
print(time2-time1)
