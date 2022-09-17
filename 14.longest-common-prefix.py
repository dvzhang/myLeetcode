#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from sys import prefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) < 2:
            return ""
        for i in range(len(strs[0])):
            for str in strs[1:]:
                if str[i] != strs[0][i] or len(str) <= i:
                    return strs[0][:i]
    def longestCommonPrefix2(self, strs: list[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix

# @lc code=end


import time
time1 = time.time()

n =["flower","flow","flight"]
pro = Solution()
print(pro.longestCommonPrefix(n))

time2 = time.time()
print(time2-time1)