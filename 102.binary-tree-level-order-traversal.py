#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        ans, queue = [], [root]
        if root:
            while queue:
                ans.append(lf.val for lf in queue)
                LfQueue = [(lf.left, lf.right) for lf in queue]

                # 这一步需要注意确认lf不是none才能加入队列
                queue = [lf for lfPair in LfQueue for lf in lfPair if lf]
        return ans
        
    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, queue = [], [root]
        if root:
            while queue:
                ans.append(lf.val for lf in queue)
                queue = [nlf for lf in queue for nlf in (lf.left, lf.right) if nlf]

        return ans
# @lc code=end

