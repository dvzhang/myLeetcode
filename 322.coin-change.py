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
            # 在硬币数量时nc个时候，会能组合出来哪些数字,并减去已经被看过的那些数字
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
    def coinChange3(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc = 0
        visited = [False] * (amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    num = coin + v
                    if num == amount:
                        return nc
                    elif num > amount:
                        continue
                    elif not visited[num]:
                        visited[num] = True
                        value2.append(num)
            value1, value2 = value2, []
        return -1
    def coinChange4(self, coins: list[int], amount: int) -> int:
        coins.sort()
        coinC = [0] + [float("inf") for _ in range(amount)]

        for coin in coins:
            for i in range(coin, amount+1):
                coinC[i] = min(coinC[i], 1 + coinC[i-coin])
        return coinC[-1] if coinC[-1] != float("inf") else -1 

    def coinChange_518(self, coins: list[int], amount: int) -> int:
        # 第n个数字有多少种组合办法，可以先问第n-1个
        waysToMakeChange = [1] + [0 for _ in range(amount)]
        for coin in coins:
            for change in range(coin, amount+1):
                waysToMakeChange[change] += waysToMakeChange[change-coin]
        return waysToMakeChange[-1]
# @lc code=end


import time
time1 = time.time()

coins = [2,5]
amount = 11
pro = Solution()
print(pro.coinChange3(coins, amount))
print(pro.coinChange4(coins, amount))

time2 = time.time()
print(time2-time1)

