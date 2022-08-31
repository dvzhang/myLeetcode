#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# @lc code=start
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if not triangle:
            return 0
        res = [ [0 for i in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i-1][j]+triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    res[i][j] = res[i-1][j-1]+triangle[i][j]
                else:
                    res[i][j] = min(res[i-1][j], res[i-1][j-1])+triangle[i][j]
        return min(res[-1]) 


# @lc code=end
import time
time1 = time.time()

n = [[2],[3,4],[6,5,7],[4,1,8,3]]
pro = Solution()
print(pro.minimumTotal(n))

time2 = time.time()
print(time2-time1)
