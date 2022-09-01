#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort()
        def find(coins, amount):
            if amount == 0:
                return 0
            if not coins or amount < coins[0]:
                return -1
            max = coins[-1]
            subAmount = amount % max
            used = int(amount / max)
            coins.pop()
            for i in range(used, -1, -1):
                subRes = find(coins, subAmount)
                if subRes != -1:
                    return subRes+used
                else:
                    used -= 1
                    subAmount += max
            return -1
        return find(coins, amount)
    def coinChange2(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1



# @lc code=end


import time
time1 = time.time()

coins = [2,5]
amount = 11
pro = Solution()
print(pro.coinChange2(coins, amount))

time2 = time.time()
print(time2-time1)