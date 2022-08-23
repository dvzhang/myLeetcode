#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        visited = set()
        def dfs(node):
            if not node:
                return
            visited.add(node)
            tmp = node.left
            node.left = node.right
            node.right = tmp
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 
            stack = [root]
            while stack:
                node = stack.pop()
                tmp = node.left
                node.left = node.right
                node.right = tmp
                if not node.left:
                    stack.append(node.left)
                if not node.right:
                    stack.append(node.right)
        dfs(root)
        return root
    def invertTree3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root
# @lc code=end

