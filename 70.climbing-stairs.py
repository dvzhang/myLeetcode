#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    def climbStairs2(self, n: int) -> int:
        Anss = [0] * (n+1)
        Anss[0], Anss[1] = 1, 1
        if n <= 1:
            return Anss[n]
        
        for i in range(2, n+1):
            Anss[i] = Anss[i-1] + Anss[i-2]
        return Anss[-1]
    def climbStairs3(self, n: int) -> int:
        if n <= 1:
            return 1
        a = b = 1
        while n > 1:
            a, b = a+b, a
            n -= 1
        return a
# @lc code=end

import time
time1 = time.time()

n = 3
pro = Solution()
print(pro.climbStairs3(n))

time2 = time.time()
print(time2-time1)