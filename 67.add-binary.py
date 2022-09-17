#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num = int(a, 2) + int(b, 2)
        return str(bin(num))[2:]
    def addBinary2(self, a: str, b: str) -> str:
        aNum = 0
        for i in a:
            aNum *= 2
            aNum += int(i)
        bNum = 0
        for i in b:
            bNum *= 2
            bNum += int(i)
        num = aNum + bNum
        return str(bin(num))[2:]

# @lc code=end


import time
time1 = time.time()

a = "11"
b = "1"
pro = Solution()
print(pro.addBinary2(a, b))

time2 = time.time()
print(time2-time1)