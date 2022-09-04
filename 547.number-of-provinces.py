#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        if not isConnected:
            return 0
        
        n = len(isConnected)
        p = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    self.union(p, i ,j)
        return len(set( [self.parent(p, i) for i in range(n)] ))

    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p1] = p2

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x = i
            i = p[i]
            p[x] = root
        return root

# @lc code=end

import time
time1 = time.time()

board = [[1,0,0],[0,1,0],[0,0,1]]
pro = Solution()
print(pro.findCircleNum(board))
time2 = time.time()
print(time2-time1)