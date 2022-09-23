#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
from itertools import count
import collections

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1: count += 1
            n = n >> 1
        return count
    def hammingWeight2(self, n: int) -> int:
        counter = collections.Counter(bin(n)[2:])
        return counter.get("1", 0)

# @lc code=end

