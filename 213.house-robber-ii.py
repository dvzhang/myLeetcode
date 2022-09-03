#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]

# @lc code=end

import time
time1 = time.time()


n = [1,2,3,1]
n = [1,3,1,3,100]
pro = Solution()
print(pro.rob(n))

time2 = time.time()
print(time2-time1)