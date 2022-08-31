#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from unittest import result


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        results, queue = [], deque([root])
        level, nodeNumLevel, levelNodeVal = 1, 1, []
        while queue:
            node = queue.popleft()
            nodeNumLevel -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            levelNodeVal.append(node.val)
            
            if nodeNumLevel == 0:
                nodeNumLevel = len(queue)
                level += 1
                results.append(max(levelNodeVal))
                levelNodeVal = []
        return results
    def largestValues2(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        def dfs(node, level):
            if not node:
                return
            if level > len(results) - 1:
                results.append(node.val)
            else:
                results[level] = max(node.val, results[level])

            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)
        return results
# @lc code=end

