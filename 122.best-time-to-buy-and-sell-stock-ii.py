#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
import time

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for id in range(len(prices)-1):
            if prices[id] < prices[id+1]:
                profit += prices[id+1] - prices[id]
        return profit
# @lc code=end

time1 = time.time()


n = [7,1,5,3,6,4]
pro = Solution()
print(pro.maxProfit(n))

time2 = time.time()
print(time2-time1)
