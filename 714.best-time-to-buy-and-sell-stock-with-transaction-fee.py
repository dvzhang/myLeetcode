#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        if not prices:
            return 0

        results = [[[None for i in range(2)] for i in range(int(len(prices) / 2) + 1)] for _ in range(len(prices))]
        for i in range(len(results[0])):
            results[0][i][0] = 0
            results[0][i][1] = -1 * prices[0] - k
        for i in range(len(results)):
            results[i][0][0] = 0
            results[i][0][1] = float("-inf")
        
        for i in range(1, len(results)):
            for j in range(1, len(results[i])):
                results[i][j][0] = max(results[i-1][j][0], results[i-1][j][1] + prices[i])
                results[i][j][1] = max(results[i-1][j][1], results[i-1][j-1][0] - prices[i] - k)
            
        ans = 0
        for i in range(len(results[-1])):
            ans = max(ans, results[-1][i][0])

        return ans
    def maxProfit2(self, prices: list[int], fee: int) -> int:
        buying, selling = 0, -prices[0]
        for i in range(1, len(prices)):
            buying = max(buying, selling + prices[i] - fee)
            selling = max(selling, buying - prices[i])
        return buying
    
    def maxProfit3(self, prices: list[int], fee: int) -> int:
        if not prices:
            return 0

        results = [[None for i in range(2)]  for _ in range(len(prices))]
        results[0][0] = 0
        results[0][1] = -1 * prices[0] - fee
        
        for i in range(1, len(results)):
            results[i][0] = max(results[i-1][0], results[i-1][1] + prices[i])
            results[i][1] = max(results[i-1][1], results[i-1][0] - prices[i] - k)

        return results[-1][0]


# @lc code=end

import time
time1 = time.time()


n = [7,1,5,3,6,4]
n = [1,3,2,8,4,9]
k = 2
pro = Solution()
print(pro.maxProfit2(n, k))
time2 = time.time()
print(time2-time1)