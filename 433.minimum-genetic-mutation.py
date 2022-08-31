#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start

import time

class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        results = []
        def instep(node, step):
            for i in range(len(node)-1):
                if node[i] != step[i] and node[0:i] == step[0:i] and node[i+1:] == step[i+1:]:
                    return True
            if node[-1] != step[-1] and node[0:-1] == step[0:-1]:
                return True
            return False
        def dfs(node,path,end):
            if node == end:
                results.append(path)
            for step in bank:
                if step not in path and instep(node, step):
                    dfs(step, path+[step], end)
        dfs(start, [], end)
        if len(results) == 0:
            return -1
        else:
            ans = 10000000
            for result in results:
                ans = min(ans, len(result))
            return ans
# @lc code=end

start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]

time1 = time.time()

pro = Solution()
print(pro.minMutation(start, end, bank))

time2 = time.time()
print(time2-time1)
