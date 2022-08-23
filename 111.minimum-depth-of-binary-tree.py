#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if ( None in [root.left, root.right]):
            return max( self.minDepth(root.left), self.minDepth(root.right) ) + 1
        else:
            return min( self.minDepth(root.left), self.minDepth(root.right) ) + 1
    def minDepth2(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level, num_nodeOfLevel = 1, 1
        while queue or node:
            node = queue.popleft()

            if ( node.left is None and node.right is None ):
                return level

            num_nodeOfLevel -= 1
            queue.append(node.left)
            queue.append(node.right)

            if num_nodeOfLevel == 0:
                level += 1
                num_nodeOfLevel = len(queue)
# @lc code=end

