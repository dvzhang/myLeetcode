#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
from turtle import down


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        rowIndex += 1
        result = [1 for i in range(rowIndex)]
        for i in range(2, rowIndex):
            
            for j in range(1, i)[::-1]:
                result[j] = result[j] + result[j-1]
        return result
    def getRow1(self, rowIndex: int) -> list[int]:
        result = [1] * (rowIndex+1)
        up = rowIndex
        down = 1
        for i in range(1, rowIndex):
            result[i] = result[i-1]*up/down
            up += 1
            down -= 1
        
        return result
# @lc code=end
pro = Solution()
print(pro.getRow(3))
