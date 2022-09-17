#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
import time
import math


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
        
    def mySqrt2(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            m = int((l + r)/2)
            m2 = math.pow( m, 2 )
            mp2 = math.pow( m+1, 2 )
            if m2 <= x and mp2 > x:
                return m
            elif m2 > x:
                r = m-1
            else:
                l = m+1
        return l
# @lc code=end


time1 = time.time()


n = 0
pro = Solution()
print(pro.mySqrt2(n))

time2 = time.time()
print(time2-time1)