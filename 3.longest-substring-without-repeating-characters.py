#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from tracemalloc import start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        length = len(s)
        for i in range(len(s)):
            ans = [s[i]]
            j = 1
            while i+j<length and s[i+j] not in ans:
                ans.append(s[i+j])
                j += 1
            res = max(res, len(ans))
        return res
    def lengthOfLongestSubstring2(self, s: str) -> int:
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
    def lengthOfLongestSubstring3(self, s: str) -> int:
        used = {}
        res, start = 0, 0
        for i in range(len(s)):
            if s[i] in used:
                start = max(start, used[s[i]] + 1)

            res = max(res, i - start + 1)

            used[s[i]] = i
        return res

# @lc code=end
import time
time1 = time.time()
n = "tmmzuxt"
pro = Solution()
print(pro.lengthOfLongestSubstring3(n))

