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
    def maxSubArray2(self, array: list[int]) -> int:
        start, end = 0, 0
        ans = float("-inf")
        while end <= len(array)-1:
            ans = max(ans, sum(array[start: end+1]))
            if array[end] < (-1 * sum(array[start: end])):
                start = end + 1
            end = end + 1
        return ans
# @lc code=end

import time
time1 = time.time()

n = [1, 2, 3, 4, 5, 6, -22, 7, 8, 9, 10]
pro = Solution()
print(pro.maxSubArray(n))
time2 = time.time()
print(time2-time1)
print(pro.maxSubArray2(n))

time2 = time.time()
print(time2-time1)