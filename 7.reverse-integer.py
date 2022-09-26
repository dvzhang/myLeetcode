#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def cmp(self, a, b):
        return (a > b) - (a < b) 
    def reverse(self, x: int) -> int:
        if x < 0:
            str(x)[::-1]
        str(x)[::-1]

        s = self.cmp(x, 0)
        r = int(str(s*x)[::-1])
        return s*r * (r < 2**31)

# @lc code=end

import time
time1 = time.time()
n = 123
pro = Solution()
print(pro.reverse(n))
time2 = time.time()
print(time2-time1) 