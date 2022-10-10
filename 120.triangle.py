#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# @lc code=start
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if not triangle:
            return 0
        res = [ [0 for i in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i-1][j]+triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    res[i][j] = res[i-1][j-1]+triangle[i][j]
                else:
                    res[i][j] = min(res[i-1][j], res[i-1][j-1])+triangle[i][j]
        return min(res[-1]) 
    
    def minimumTotal2(self, triangle: list[list[int]]) -> int:
        results = []
        
        if not triangle:
            return 0
        def inList(i, j, triangle =  triangle):
            if 1 <= i < len(triangle) and 0 <= j < len(triangle[i]):
                return True
            return False
        def dfs(i, j, path, triangle = triangle):
            if i >= len(triangle)-1:
                results.append(path+triangle[i][j])
                return
            if inList(i+1, j):
                dfs(i+1, j, path+triangle[i][j])
            if inList(i+1, j+1):
                dfs(i+1, j+1, path+triangle[i][j])
        dfs(0, 0, 0)
        return min(results)
    
    def minimumTotal3(self, triangle: list[list[int]]) -> int:
        if not triangle:
            return 0
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])
    def minimumTotal4(self, triangle: list[list[int]]) -> int:
        if not triangle:
            return 0
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
    def minimumTotal5(self, triangle: list[list[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i-1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i-1][j], triangle[i-1][j-1]) + triangle[i][j]
        return min(triangle[-1])
    def minimumTotal5(self, triangle: list[list[int]]) -> int:
        def dfs(triangle, i, j):
            if i == len(triangle) - 1:
                return triangle[i][j]
            return min(dfs(triangle, i+1, j), dfs(triangle, i+1, j+1)) + triangle[i][j]
        return dfs(triangle, 0, 0)
    def minimumTotal6(self, triangle: list[list[int]]) -> int:
        def isIn(i, j, triangle):
            if i < len(triangle) and j < len(triangle[i]):
                return True
            return False

        stack = [(0, 0)]
        results = []
        while stack:
            node = stack.pop()
            if node[0] == len(triangle):
                results.append()
            if isIn(node[0]+1, node[1], triangle):
                stack.append((node[0]+1, node[1]))
            if isIn(node[0]+1, node[1]+1, triangle):
                stack.append((node[0]+1, node[1]+1))
            





# @lc code=end
import time
time1 = time.time()

n = [[2],[3,4],[6,5,7],[4,1,8,3]]
pro = Solution()
print(pro.minimumTotal5(n))

time2 = time.time()
print(time2-time1)
