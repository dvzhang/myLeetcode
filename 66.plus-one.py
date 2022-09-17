#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        num = int("".join([str(i) for i in digits]))
        num += 1
        return [int(i) for i in str(num)]
    def plusOne2(self, digits: list[int]) -> list[int]:
        num = 0
        for i in digits:
            num *= 10
            num += i
        return [int(i) for i in str(num+1)]

# @lc code=end

import time
time1 = time.time()

nums =[4,3,1,9]
pro = Solution()
print(pro.plusOne2(nums))

time2 = time.time()
print(time2-time1)