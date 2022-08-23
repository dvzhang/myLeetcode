#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        length = float(len(nums)) / 2
        for num in nums:
            dict[str(num)] = dict.get(str(num), 0) + 1
        for key, value in dict.items():
            if value > length:
                return int(key)
        return False
    

    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)/2]
            
# @lc code=end

