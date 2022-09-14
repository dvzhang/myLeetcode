#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        for i in range(len(nums)-1):
            dict = {}
            for j in range(i+1, len(nums)):
                
                if str(-1 * (nums[i] + nums[j])) in dict:
                    ans.append([nums[i], nums[j], -1 * (nums[i] + nums[j])])
                else:
                    dict[str(nums[j])] = 0
        return ans

    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    ans.append([nums[l], nums[r], nums[i]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans
                    

# @lc code=end

import time
time1 = time.time()

n = [0,0,0]
pro = Solution()
print(pro.threeSum(n))

time2 = time.time()
print(time2-time1)