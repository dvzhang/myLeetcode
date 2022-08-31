#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
import time

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        
        left, right = 0, x
        while left <= right:
            mid = int((left+right) / 2)
            if mid*mid == x or (mid*mid < x and (mid+1)*(mid+1) > x):
                return mid
            elif mid*mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        
# @lc code=end


time1 = time.time()


n = 1
pro = Solution()
print(pro.mySqrt(n))

time2 = time.time()
print(time2-time1)