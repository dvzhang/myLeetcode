#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import re


class Solution:
    def height(self, node):
        if not node:
            return 0
        return max(self.height(node.right), self.height(node.left)) + 1

    def isBalanced(self, root):
        if not root:
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    def isBalanced2(self, root):
        def check(node):
            if not node:
                return False
            left = check(node.left)
            right = check(node.right)
            if not( left or right ) or abs(left - right) > 1:
                return False
            return max(left, right) + 1
        return check(root) != -1
        
# @lc code=end


a = TreeNode(3)
b = TreeNode(9, left=None, right=None)
e = TreeNode(9, left=None, right=None)

c = TreeNode(-10, left=e)
d = TreeNode(20, left=c, right=a)
root = TreeNode(3, left=b, right=d)

pro = Solution()
print(pro.isBalanced2(root))
