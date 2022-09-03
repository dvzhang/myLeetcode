#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
import time


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        min = prices[0]
        maxp = profit = 0

        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
                maxp = min
            if prices[i] > maxp:
                maxp = prices[i]
                profit = max(maxp - min, profit)
        return profit
    def maxProfit2(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit
    def maxProfit3(self, prices: list[int]) -> int:
        left = profit = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = max(prices[right] - prices[left], profit)
            else:
                left = right

            right += 1
        return profit
    def maxProfit4(self, prices: list[int]) -> int:
        if not prices:
            return 0
            
        results = [[0, -prices[0]]] 

        for i in range(1, len(prices)):
            results.append([])
            results[i].append( max(results[i-1][0], results[i-1][1] + prices[i]) )
            results[i].append( max(results[i-1][1], results[i-1][0] - prices[i]) )
        return results[-1][0]
# @lc code=end





time1 = time.time()


n = [7,1,5,3,6,4]
n = [1,2,3,4,5]
pro = Solution()
print(pro.maxProfit4(n))
time2 = time.time()
print(time2-time1)
