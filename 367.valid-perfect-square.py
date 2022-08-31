#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

import time
# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num4
        while left <= right:
            mid = int((left + right)/2)
            if mid*mid == num:
                return True
            elif mid*mid < num and (mid+1)*(mid+1) > num:
                return False
            elif mid*mid < num:
                left = mid + 1
            elif mid*mid > num:
                right = mid -1
        return False
# @lc code=end


time1 = time.time()


n = 16
pro = Solution()
print(pro.isPerfectSquare(n))

time2 = time.time()
print(time2-time1)

