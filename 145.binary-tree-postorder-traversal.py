#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root) -> list[int]:
        if not root:
            return
        ans, stack = [], [(0, root)]
        while stack:
            label, node = stack.pop()
            if not node:
                continue
            if not label:
                stack.append((1, node))
                stack.append((0, node.right))
                stack.append((0, node.left))
            else:
                ans.append(node.val)
        return ans

        
# @lc code=end

a = TreeNode(3)
b = TreeNode(2, left=None, right=a)
c = TreeNode(-10)
d = TreeNode(-2, left=None, right=None)
d = TreeNode(-5, left=c, right=d)
root = TreeNode(1, left=d, right=b)

pro = Solution()
print(pro.postorderTraversal(root))
