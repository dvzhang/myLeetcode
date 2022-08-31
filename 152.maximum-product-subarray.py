#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0
        maxRes = subMaxRes = subMinRes = subMaxRes2 = subMinRes2 = nums[0]
        for num in nums[1:]:
            subMaxRes = max(max(num, subMaxRes2*num), subMinRes2*num)
            subMinRes = min(min(num, subMaxRes2*num), subMinRes2*num)
            subMaxRes2 = subMaxRes
            subMinRes2 = subMinRes
            maxRes = max(maxRes, subMaxRes)
        return maxRes
# @lc code=end

import time
time1 = time.time()

n = [5,4,-1,7,8]
n = [-2,-3,-4]
pro = Solution()
print(pro.maxProduct(n))

time2 = time.time()
print(time2-time1)