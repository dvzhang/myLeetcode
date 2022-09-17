#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "": 0,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        if len(s)<2:
            return dict[s]

        ans = 0
        for i in range(len(s)-1):
            if dict[s[i]] < dict[s[i+1]]:
                ans += dict[s[i]] * -1
            else:
                ans += dict[s[i]]
        ans += dict[s[i+1]]
        
        return ans
    def romanToInt2(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
        
# @lc code=end

import time
time1 = time.time()

n = "LVIII"
pro = Solution()
print(pro.romanToInt(n))

time2 = time.time()
print(time2-time1)