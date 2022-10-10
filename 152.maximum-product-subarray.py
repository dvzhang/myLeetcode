#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from platform import mac_ver


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0
        maxRes = subMaxRes = subMinRes = subMaxRes2 = subMinRes2 = nums[0]
        # 每次记录以num为结尾的字串的最大值、最小值
        for num in nums[1:]:
            subMaxRes = max(max(num, subMaxRes2*num), subMinRes2*num)
            subMinRes = min(min(num, subMaxRes2*num), subMinRes2*num)
            subMaxRes2 = subMaxRes
            subMinRes2 = subMinRes
            maxRes = max(maxRes, subMaxRes)
        return maxRes
    def maxProduct2(self, nums: list[int]) -> int:
        maxR = subMax1 = subMax2 = subMin1 = subMin2 = nums[0]
        for num in nums[1:]:
            subMax1 = max(max(num, subMax2*num), subMin2*num)
            subMin1 = min(min(num, subMax2*num), subMin2*num)
            subMax2 = subMax1
            subMin2 = subMin1
            maxR = max(maxR, subMax2)
        return maxR
        
# @lc code=end

import time
time1 = time.time()

n = [5,4,-1,7,8]
n = [-2,-3,-4]
pro = Solution()
print(pro.maxProduct2(n))

time2 = time.time()
print(time2-time1)