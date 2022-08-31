#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0
        subSum = maxSum = nums[0]
        for num in nums[1:]:
            subSum = max(num, num+subSum)
            maxSum = max(subSum, maxSum)
        return maxSum
# @lc code=end

import time
time1 = time.time()

n = [5,4,-1,7,8]
pro = Solution()
print(pro.maxSubArray(n))

time2 = time.time()
print(time2-time1)