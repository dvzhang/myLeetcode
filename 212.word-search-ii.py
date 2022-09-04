#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
from turtle import fd


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        def createPrefixTree(words):
            root = {}
            endOfWord = "#"
            for word in words:
                node = root
                for char in word:
                    node = node.setdefault(char, {})
                node[endOfWord] = endOfWord
            return root

        def search(root, word):
            node = root
            for char in word:
                if char not in node:
                    return False
                node = node[char]
            return "#" in node

        def DFS(i, j, board, root, path):
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            if "#" in root[board[i][j]]:
                self.results.add(path+board[i][j])
            tmp, board[i][j] = board[i][j], "@"
            for n in range(len(dx)):
                if 0 <= dx[n]+i < len(board) and 0 <= dy[n]+j < len(board[0]) and board[dx[n]+i][dy[n]+j] != "@" and board[dx[n]+i][dy[n]+j] in root[tmp]:
                    DFS(dx[n]+i, dy[n]+j, board, root[tmp], path+tmp)
            board[i][j] = tmp

        self.results = set()
        root = createPrefixTree(words)
        results = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root:
                    DFS(i, j, board, root, "")
        return list(self.results)

# @lc code=end
import time
time1 = time.time()

board = [["o", "a", "a", "n"], 
         ["e", "t", "a", "e"], 
         ["i", "h", "k", "r"], 
         ["i", "f", "l", "v"]]
words= ["oath", "pea", "eat", "rain"]
pro = Solution()
print(pro.findWords(board, words))
time2 = time.time()
print(time2-time1)
