from collections import deque
import queue
from typing import Deque

def transform(i, length):
    return i % length


# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, node):
        self.children.append(node)
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = Deque([self])
        while queue:
            node = queue.popleft()
            array.append(node.name)
            for child in node.children:
                queue.append(child)
                
        return array

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class matrix:
    def edge(self, x, y, matrix):
        if 0 == x or 0 == y or len(matrix)-1 == x or len(matrix[0])-1 == y:
            return True
        return False
    def dfs(self, x, y, matrix):
        stack = Deque([(x, y)])
        size = 0
        while stack:
            x, y = stack.popleft()
            # print(x, y)
            matrix[x][y] = 0
            size += 1
            for direction in directions:
                if not(0 <= x+direction[0] < len(matrix) and 0 <= y+direction[1] < len(matrix[0])):
                    continue
                if matrix[x+direction[0]][y+direction[1]] == 1 and (x+direction[0], y+direction[1]) not in stack:
                    stack.append((x+direction[0], y+direction[1]))
        return size, matrix
    
    def dfsIsland(self, x, y, matrix):
        queue = Deque([(x, y)])
        ans = [[i for i in l] for l in matrix]
        while queue:
            x, y = queue.popleft()
            if self.edge(x, y, matrix):
                return matrix
            ans[x][y] = 0
            for direction in directions:
                if not(0 <= x+direction[0] < len(matrix) and 0 <= y+direction[1] < len(matrix[0])):
                    continue
                if ans[x+direction[0]][y+direction[1]] == 1 and (x+direction[0], y+direction[1]) not in queue:
                    queue.append((x+direction[0], y+direction[1]))
        return ans
            
    def riverSizes(self, matrix):
        ans = []
        # Write your code here.
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    a, matrix = self.dfs(i, j, matrix) 
                    ans.append(a)
        return ans
    def removeIslands(self, matrix):
        for i in range(1, len(matrix)-1):
            for j in range(1, len(matrix[i])-1):
                if matrix[i][j] == 1:
                    matrix = self.dfsIsland(i, j, matrix)

        return matrix


class Solution:

    def hasSingleCycle(self, array):
        # Write your code here.
        seen = set([0])
        i = transform(array[0], len(array))
        while i not in seen and len(seen) < len(array) and array[i] != 0:
            seen.add(i)
            i = transform(i + array[i], len(array))
        return (len(seen) == len(array)) and i == 0


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None
    def getAncestor(self, num, fro):
        ans = self
        while num:
            num -= 1
            if ans.ancestor:
                ans = ans.ancestor
            else:
                ans = fro
        return ans
    def getAncestorPass(self):
        ances = self
        ans = []
        while ances: 
            ans.append(ans)
            ances = ances.ancestor
        return ans


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    one, two = descendantOne.getAncestorPass(), descendantTwo.getAncestorPass()
    for i in range(len(one)):
        if one[i] in two:
            return one[i]
    return


import time
time1 = time.time()

array = [1, 1, 1, 1, 2]

pro = Solution()
print(pro.hasSingleCycle(array))

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")
I = Node("I")
J = Node("J")
K = Node("K")
A.addChild(B).addChild(C).addChild(D)
B.addChild(E).addChild(F)
D.addChild(G).addChild(H)
F.addChild(I).addChild(J)
G.addChild(K)
array2 = []
print(A.breadthFirstSearch(array2))

ma = matrix()
array = [
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 1]
  ]

array2 = [
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1]
]
print(ma.riverSizes(array))
print(ma.removeIslands(array2))


time2 = time.time()
print(time2-time1)


