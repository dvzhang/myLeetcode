#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from unittest import result
import time

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        def DFS(queen, xy_dif, xy_sum):
            p = len(queen)
            if p == n:
                result.append(queen)
                return None
            for q in range(n):
                if q not in queen and p-q not in xy_dif and p+q not in xy_sum:
                    DFS(queen+[q], xy_dif+[p-q], xy_sum+[p+q])
        
        result = []
        DFS([], [], [])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result ]

    def solveNQueens2(self, n: int) -> list[list[str]]:
        results = []
        def dfs(queen, xySum, xyDif):
            p = len(queen)
            if p == n:
                results.append(queen)
                return 
            for q in range(n):
                if p+q not in xySum and p-q not in xyDif and q not in queen:
                    dfs(queen + [q], xySum + [p+q], xyDif + [p-q])
        dfs([], [], [])

        return [ ['.'*i + "Q" + (n-i-1)*"." for i in result] for result in results]

    def solveNQueens3(self, n: int) -> list[list[str]]:
        results = []
        def dfs(path, xySum, xyDiff):
            p = len(path)
            if p == n:
                results.append(path)
                return
            for q in range(n):
                if p+q not in xySum and p-q not in xyDiff and q not in path:
                    dfs(path+[q], xySum+[p+q], xyDiff+[p-q])

        dfs([],[],[])
        return [["."*i + "Q" + "."*(n-1-i) for i in range(n)] for result in results]
# @lc code=end

time1 = time.time()

nums = 3
pro = Solution()
print(pro.solveNQueens3(nums))

time2 = time.time()
print(time2-time1)