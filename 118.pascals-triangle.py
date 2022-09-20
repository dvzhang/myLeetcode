#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        results = [[0 for j in range(i+1)]for i in range(numRows)] 
        for i in range(len(results)):
            for j in range(len(results[i])):
                if j == 0 or j == len(results[i]) - 1:
                    results[i][j] = 1
                else:
                    results[i][j] = results[i-1][j-1] + results[i-1][j]
        return results   
    def generate2(self, numRows: int) -> list[list[int]]:
        results = [[1 for j in range(i+1)]for i in range(numRows)] 
        for i in range(len(results)):
            for j in range(1, len(results[i])-1):
                results[i][j] = results[i-1][j-1] + results[i-1][j]
        return results    
# @lc code=end

pro = Solution()
print(pro.generate(7))
