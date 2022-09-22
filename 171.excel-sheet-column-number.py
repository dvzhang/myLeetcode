#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def getNum(self, character):
        return ord(character) - ord("A") + 1
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for character in columnTitle:
            ans = ans * 26 + self.getNum(character)
        return ans
# @lc code=end

n = "ALL"
pro = Solution()
print(pro.titleToNumber(n))