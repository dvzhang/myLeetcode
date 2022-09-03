#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
from email.errors import NonASCIILocalPartDefect
from email.mime import nonmultipart
from unittest import result


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices:
            return 0
        
        results = [[[None for j in range(2)] for i in range(min(int(len(prices) / 2) + 1, k+1))] for _ in range(len(prices))]
        for i in range(len(results[0])):
            results[0][i][0] = 0
            results[0][i][1] = -1 * prices[0]
        for i in range(len(results)):
            results[i][0][1] = float("-inf")
            results[i][0][0] = 0

        for i in range(1, len(results)):
            for j in range(1, len(results[i])):
                results[i][j][0] = max(results[i-1][j][0], results[i-1][j][1]+prices[i])
                results[i][j][1] = max(results[i-1][j][1], results[i-1][j-1][0]-prices[i])
        ans = 0
        for i in range(len(results[-1])):
            ans = max(ans, results[-1][i][0])
        return ans


# @lc code=end

import time
time1 = time.time()


n = [7,1,5,3,6,4]
n = [3,2,6,5,0,3]
k = 2
pro = Solution()
print(pro.maxProfit(k, n))
time2 = time.time()
print(time2-time1)
