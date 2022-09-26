#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
from ast import Num


class Solution:
    def check(self, c):
        return True if 0 <= self.num(c) <= 9 else False

    def num(self, c):
        return ord(c) - ord("0")
            
    def myAtoi(self, s: str):
        s = s.strip()
        if not s:
            return 0
        ans = 0
        if s[0] == "-":
            mark = -1 
            s = s[1:]
        elif s[0] == "+": 
            mark = 1
            s = s[1:]
        else:
            mark = 1 
        for c in s:
            res = self.num(c)
            if not 0 <= res <= 9:
                break
            ans = ans*10 + res
        ans = mark * ans
        ans = 2**31-1 if ans >= 2**31 else ans
        ans = -1*2**31 if ans < -1*2**31 else ans
        return ans

    def myAtoi2(self, s: str):

        if len(s) == 0 : return 0
        ls = list(s.strip())
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))
import time
time1 = time.time()
n = "  -42"
pro = Solution()
print(pro.myAtoi(n))
time2 = time.time()
print(time2-time1) 

# @lc code=end

