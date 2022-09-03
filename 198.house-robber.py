#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[-1]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        def myRob(nums):
            selfEnd = [nums[0], nums[1]]        
            selfNotEnd = [0, nums[0]]
            for i in range(2, len(nums)):
                selfEnd.append(selfNotEnd[-1]+nums[i])
                selfNotEnd.append(max(selfEnd[-2], selfNotEnd[-1]))    
                
            return max(selfNotEnd[-1], selfEnd[-1])
        return max(myRob(nums[1:]), myRob(nums[:-1]))


    def rob2(self, nums: list[int]) -> int:
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