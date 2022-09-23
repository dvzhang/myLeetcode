#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)
# @lc code=end
import time
time1 = time.time()
n = 00000010100101000001111010011100
pro = Solution()
print(pro.reverseBits(n))