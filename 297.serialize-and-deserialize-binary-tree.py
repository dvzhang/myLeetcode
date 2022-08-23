#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def trans(node):
            if node:
                val.append(str(node.val))
                trans(node.left)
                trans(node.right)
            else:
                val.append("#")
        val = []
        trans(root)
        return ' '.join(val)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def make():
            val = next()
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()

        val = iter(data.split())
        return make()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

