#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#
import time

# @lc code=start


class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        contentNum = 0
        sid = 0
        lenS = len(s)
        s.sort()
        g.sort()
        for id in range(len(g)):
            for sid in range(sid, lenS):
                if s[sid] >= g[id]:
                    contentNum += 1
                    sid += 1
                    break
        return contentNum


time1 = time.time()


g = [1, 2, 3]
s = [3]
pro = Solution()
print(pro.findContentChildren(g, s))

time2 = time.time()
print(time2-time1)

# @lc code=end
