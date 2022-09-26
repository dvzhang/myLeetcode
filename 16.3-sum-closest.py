#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from asyncio.windows_events import INFINITE


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float("inf")
        nums.sort()
        for i in range(len(nums)):
            start, end = i+1, len(nums)-1
            while start < end:
                sumT = nums[i] + nums[start] + nums[end]
                if abs(target - sumT) < abs(target - ans):
                    ans = sumT
                if target - sumT > 0:
                    start += 1
                else:
                    end -= 1
        return ans
        


        


        
# @lc code=end

