#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
from turtle import distance


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int], perMile=1) -> int:
        for i in range(len(gas)):
            ans = 0
            search = [j for j in range(i, len(gas))]
            search += [j for j in range(i)]
            for j in search:
                ans += gas[j]
                ans -= cost[j] * perMile
                if ans < 0:
                    break
            if ans >= 0:
                return i
        return -1

    def canCompleteCircuit2(self, gas: list[int], cost: list[int], perMile=1) -> int:
        left = right = 0
        while left == right:
            if canGo(right):
                pass
            left = (left - 1) % len(gas)
            right = (right + 1) % len(gas)
    def canCompleteCircuit3(self, gas: list[int], cost: list[int], perMile=1) -> int:
        fuel, distances, mpg = gas, cost, perMile
        biggestNegative = 0
        bestStartIndex = 0
        curSum = 0
        for i in range(len(distances)):
            curSum += fuel[i] * mpg - distances[i]
            if curSum < biggestNegative:
                biggestNegative = curSum
                bestStartIndex = (i+1) % len(distances)
        return bestStartIndex
# @lc code=end


gas = [1,2,3,4,5]
cost =[3,4,5,1,2]
import time
time1 = time.time()

pro = Solution()
print(pro.canCompleteCircuit3(gas, cost))

time2 = time.time()
print(time2-time1)