#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
from collections import deque
from inspect import stack


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def maxPal(s):
            if len(s) == 1 or s == s[::-1]:
                return s
            front = maxPal(s[1:])
            end = maxPal(s[:-1])
            return front if len(front) > len(end) else end
        return maxPal(s)       
    def longestPalindrome2(self, s: str) -> str:
        if not s:
            return 0
        stack = deque([s])
        while stack:
            node = stack.popleft()
            if len(node) == 1:
                continue
            if node == node[::-1]:
                return node
            stack.append(node[1:])
            stack.append(node[:-1])
        return s[0]
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]
    def longestPalindrome3(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for tmp in self.helper(s, i, i), self.helper(s, i, i+1):
                if len(tmp) > len(res):
                    res = tmp
        return res
                
# @lc code=end

import time
time1 = time.time()
n = "babaddtattarrattatddetartrateedredividerb"
pro = Solution()
print(pro.longestPalindrome3(n))