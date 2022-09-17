#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()

        words = s.split(" ")
        return len(words[-1])
        
    def lengthOfLastWord2(self, s: str) -> int:
        ans = 0
        s = s.strip()
        for character in s[::-1]:
            if character == " ":
                break
            ans += 1

        return ans
        
# @lc code=end

import time
time1 = time.time()

nums = "Hello World"
pro = Solution()
print(pro.lengthOfLastWord2(nums))

time2 = time.time()
print(time2-time1)