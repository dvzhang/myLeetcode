#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from collections import deque
from unittest import result
import time


class Solution:
    def jump(self, nums: list[int]) -> int:
        self.results = 100000
        def dfs(id, nums, level):
            if level >= self.results:
                return
            if id == len(nums) - 1:
                self.results = min(self.results, level)
                return
            for step in range(1, nums[id]+1):
                if id + step < len(nums):
                    dfs(id+step, nums, level+1)
        dfs(0, nums, 0)
        return self.results
    def jump2(self, nums: list[int]) -> int:
        node, queue, searched = 0, deque([0]), set([0])
        level, numNodeLevel = 0, 1
        while queue:
            node = queue.popleft()

            for i in range(node+1, node+nums[node]+1):
                if i < len(nums) and i not in searched:
                    queue.append(i)
                    searched.add(i)
            numNodeLevel -= 1
            if numNodeLevel == 0:
                level += 1
                if len(num) - 1 in queue:
                    return level
                numNodeLevel = len(queue)
        return -1

    def jump3(self, nums: list[int]) -> int:
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step

# @lc code=end

time1 = time.time()


n = [2,0,3,1,4]
pro = Solution()
print(pro.jump3(n))

time2 = time.time()
print(time2-time1)