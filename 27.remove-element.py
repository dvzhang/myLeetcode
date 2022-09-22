#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        for quick in nums:
            if quick != val:
                nums[slow] = quick
                slow += 1
        return slow
        # return nums

        
# @lc code=end

import time
time1 = time.time()

n = [3,2,2,3]
val = 3
pro = Solution()
print(pro.removeElement(n, val))

time2 = time.time()
print(time2-time1)