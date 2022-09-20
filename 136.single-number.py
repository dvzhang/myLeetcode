#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = {}
        for num in nums:
            res[str(num)] = res.get(num, 0) + 1
        for key in res:
            if res[key] == 1:
                return int(key)
        return -1
# @lc code=end
nums = [4,1,2,1,2]
pro = Solution()
print(pro.singleNumber(nums))