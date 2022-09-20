#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        results = []
        def dfs(node, path):
            if not node.left and not node.right:
                path.append(node.val)
                results.append(path)
            if node.left:
                dfs(node.left, path+[node.val])
            if node.right:
                dfs(node.right, path+[node.val])
        if not root:
            return
        dfs(root, [])
        for result in results:
            if targetSum == sum(result):
                return True
        return False
    def hasPathSum2(self, root, targetSum: int) -> bool:
        if not root: return
        if not root.left and not root.right and root.val == sum: return True
        sum -= root.val
        return self.hasPathSum2(root.left, sum) or self.hasPathSum2(root.right, sum)
        

# @lc code=end

a = TreeNode(3)
b = TreeNode(2, left=None, right=a)
c = TreeNode(-10)
d = TreeNode(-2, left=None, right=None)
# d = TreeNode(-5, left=c, right=d)
root = TreeNode(1, left=d, right=b)
pro = Solution()
print(pro.hasPathSum(root, -1))
