#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        stack = []
        for character in s:
            if character in dict:
                stack.append(character)
            elif character != dict[ stack.pop() ] or len(stack) == 0: 
                # 注意加上 len(stack) == 0
                return False
        return True
# @lc code=end

import time
time1 = time.time()

n = "(]{}"
pro = Solution()
print(pro.isValid(n))

time2 = time.time()
print(time2-time1)