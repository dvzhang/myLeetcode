#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
import time
# @lc code=start


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def findmin(nums):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right) / 2
                if mid > mid + 1:
                    return mid + 1
                elif left < mid:
                    left = mid
                elif left >= mid:
                    pass
                    # print(findmin(nums))
    def search2(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        low, high = 0, len(nums)-1
        while low <= high:
            mid = int((low+high) / 2)
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:  # 证明从mid到末尾是顺序的
                if nums[mid] <= target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1
# @lc code=end


time1 = time.time()


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
pro = Solution()
print(pro.search2(nums, target))

time2 = time.time()
print(time2-time1)
