#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = numZero = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                i -= 1
                numZero += 1
            i += 1
        for j in range(numZero):
            nums.append(0)
        return nums

    def moveZeroes2(self, nums: list[int]) -> None:
        zero = noZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

    def moveZeroes3(self, nums: list[int]) -> None:
        top = noneZeroNum = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[top] = nums[i]
                top += 1
                noneZeroNum += 1
        for j in range(noneZeroNum, len(nums)):
            nums[j] = 0 
        return nums
    def moveZeroes4(self, nums: list[int]) -> None:
        top, b = 0, 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[top] = nums[i]
                top += 1
        for i in range(top, len(nums)):
            nums[i] = 0     
# @lc code=end

import time
time1 = time.time()

n = [0,1,0,3,12]
pro = Solution()
print(pro.moveZeroes3(n))

time2 = time.time()
print(time2-time1)
