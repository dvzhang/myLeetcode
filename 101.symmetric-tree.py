#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import queue


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root])
        while queue:
            leaf = [n.val for n in queue]
            if not leaf == leaf[::-1]:
                return False
            leaf = [(l.left, l.right) for n in queue]
            queue = [l for n in leaf for l in leaf if l]
            
            leaf = []
            for n in leaf: 
                for l in n:
                    leaf += 1 if l else 0
            if not leaf == leaf[::-1]:
                return False
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSem(L, R):
            if not L and not R: return True
            if L and R and L.val == R.val:
                return isSem(L.left, R.right) and isSem(L.right, R.left)
            return False
        return isSem(root, root)
# @lc code=end

