#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        num = columnNumber
        while columnNumber:
            num = columnNumber % 27
            columnNumber = columnNumber // 27

            ans.append(chr(ord("A") + num))
        # ans.append(chr(ord("A") - 1 + columnNumber))

        return "".join(ans[::-1])
    def convertToTitle2(self, columnNumber: int) -> str:
        capitals = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        ans = []
        # 将0-25映射到A-Z之上
        while columnNumber > 0:
            ans.append(capitals[(columnNumber-1) % 26])
            columnNumber = (columnNumber - 1) // 26

        return "".join(ans[::-1])
# @lc code=end
n = 1000
pro = Solution()
print(pro.convertToTitle2(n))