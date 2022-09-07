#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return (self.isRowValid(board) and self.isColValid2(board) and self.isSquareValid(board))
    
    def isRowValid(self, board):
        for row in board:
            saw = []

            for num in row:
                if num == ".":
                    continue
                if num in saw or not ("1"<= num <= "9") or len(num) != 1:
                    return False
                saw.append(num)
        return True
    
    def isColValid(self, board):
        for colId in range(len(board[0])):
            saw = []

            for row in board:
                num = row[colId]
                if num == ".":
                    continue
                if num in saw or not ("1"<= num <= "9") or len(num) != 1:
                    return False
                saw.append(num)
        return True
    def isColValid2(self, board):
        for col in zip(*board):
            if not self.validUnit(col):
                return False
        return True

    def isSquareValid(self, board):
        for i in (0,3,6):
            for j in (0,3,6):
                saw = []
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        num = board[x][y]
                        if num == ".":
                            continue
                        if num in saw or not ("1"<= num <= "9") or len(num) != 1:
                            return False
                        saw.append(num)
        return True
    def isSquareValid2(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i+3) for y in range(j+3)]
                if not self.validUnit(square):
                    return False
        return True

    def validUnit(self, square):
        saw = []
        for num in square:
            if num in saw:
                return False
        return True
    
    def validUnit2(self, square):
        saw = set()
        for num in square:
            saw.add(num)

        return len(saw) == len(square)
# @lc code=end

board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

import time
time1 = time.time()

nums = board
pro = Solution()
print(pro.isValidSudoku(nums))

time2 = time.time()
print(time2-time1)
