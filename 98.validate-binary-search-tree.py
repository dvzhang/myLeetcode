#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque
from platform import node
import queue
import re


class Solution:

    # 直接深度搜索，将整个树排列成为一个有序的序列
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        
        def inorder(root, output):
            if not root:
                return
            inorder(root.left, output)
            output.append(root.val)
            inorder(root.right, output)

        inorder(root, output)
        for id in range(len(output)-1):
            if output[id] >= output[id+1]:
                return False
        return True

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        def dfs_order(root):
            output, stack = [], []
            while stack or root:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    tmp = stack.pop()
                    output.append(tmp.val)
                    root = tmp.right
            return output
            
        def isOrder(input):
            for id in range(len(output)-1):
                if output[id] >= output[id+1]:
                    return False
            return True

        output = dfs_order(root)
        return isOrder(output)

    def isValidBST3(self, root: Optional[TreeNode]) -> bool:
        output = []
        def dfs(root, output):
            queue = []

            while queue or root:
                if root:
                    queue.append(root)
                    root = root.left
                else:
                    tmp = queue.pop()
                    output.append(tmp.val)
                    root = tmp.right
            return output
        dfs(root, output)
        for id in range(len(output) - 1):
            if output[id] >= output[id+1]:
                return False
        return True

# @lc code=end

