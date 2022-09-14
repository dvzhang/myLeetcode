#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start

moves = {
    0: [1,3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4],
    4: [1, 3, 5],
    5: [4, 2]
}
class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        used = set()
        cnt = 0
        s = "".join(str(c) for row in board for c in row)
        q = [(s, s.index("0"))]

        while q:
            new = []
            for s, i in q:
                used.add(s)
                if s == "123450":
                    return cnt
                arr = [ c for c in s]
                for move in moves[i]:
                    new_arr = arr[:]
                    new_arr[i], new_arr[move] = new_arr[move], new_arr[i]
                    new_s = "".join(new_arr)
                    if new_s not in used:
                        new.append((new_s, move))
            cnt += 1
            q = new
        return -1
# @lc code=end

import time
time1 = time.time()

board = [[4,1,2],[5,0,3]]
# board = [[1,2,3],[4,0,5]]
pro = Solution()
print(pro.slidingPuzzle(board))
time2 = time.time()
print(time2-time1)