#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def area(self, i, j, height):
        return (j-i) * min(height[i], height[j])

    def maxArea(self, height: list[int]) -> int:
        ans = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                ans = max(ans, self.area(i,j,height))
        return ans
    
    def maxArea2(self, height: list[int]) -> int:
        if not height:
            return 0
        i, j, ans = 0, len(height)-1, 0
        while i != j:
            ans = max(ans, self.area(i, j, height))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans
    def maxArea3(self, height: list[int]) -> int:
        if not height:
            return 0
        start, end, ans = 0, len(height) - 1, 0
        while start != end:
            ans = max(ans, self.area(start, end, height))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return ans

# @lc code=end
import time
time1 = time.time()

n = [1,8,6,2,5,4,8,3,7]
pro = Solution()
print(pro.maxArea3(n))

time2 = time.time()
print(time2-time1)
