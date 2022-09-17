#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while(l <= r):
            m = int((l+r) / 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l

# @lc code=end
import time
time1 = time.time()
n = [3,5,7,9,10]
tar = 8
pro = Solution()
print(pro.searchInsert(n, tar))

time2 = time.time()
print(time2-time1)