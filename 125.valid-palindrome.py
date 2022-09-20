#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import re

class Solution:
    def remove_special_characters(self, word):
        regex = re.compile('[^a-z]')
        return regex.sub('', word)

    def isPalindrome(self, s: str) -> bool:
        s = self.remove_special_characters(s.lower())
        return s == s[::-1]
    
    def isPalindrome2(self, s: str) -> bool:
        l, r = 0, len(s)-1
        s = s.lower()
        while l < r:
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
# @lc code=end

import time
time1 = time.time()

n = "A man, a plan, a canal: Panama"
pro = Solution()
print(pro.isPalindrome2(n))

time2 = time.time()
print(time2-time1)