#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        dict = [["I",1],["IV",4],["V",5],["XI",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["C",400],["D",500],["CM",900],["M",1000]]
        for i in range(len(dict))[::-1]:
            carry, val = divmod(num, dict[i][1])
            ans += carry * dict[i][0]
            num = val
        return "".join(ans[::-1])
    def intToRoman2(self, num: int) -> str:

        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        for i, v in enumerate(values):
            res += (num//v) * numerals[i]
            num %= v
        return res
# @lc code=end

import time
time1 = time.time()

n = 58
pro = Solution()
print(pro.intToRoman2(n))

time2 = time.time()
print(time2-time1)
