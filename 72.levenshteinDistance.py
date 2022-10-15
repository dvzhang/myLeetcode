#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def levenshteinDistance(self, str1, str2):
        big = str1 if len(str1) > len(str2) else str2
        sma = str2 if big == str1 else str1

        prev_row = [k for k in range(len(sma) + 1)]
        curr_row = [None for k in range(len(sma) + 1)]
        
        for i in range(1, len(big) + 1):
            curr_row[0] = i
            for j in range(1, len(sma) + 1):
                repl_cost = 0 if big[i-1] == sma[j-1] else 1
                curr_row[j] = min(
                    prev_row[j] + 1,
                    curr_row[j-1] + 1,
                    prev_row[j-1] + repl_cost
                )
        prev_row, curr_row = curr_row, prev_row
        return prev_row[-1]

# @lc code=end

import time
time1 = time.time()

n = 3
pro = Solution()
print(pro.levenshteinDistance("abc", "yabd"))

time2 = time.time()
print(time2-time1)