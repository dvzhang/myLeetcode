from collections import defaultdict
import time

def def_value():
    return []


class Solution():
    def __init__(self):
        pass
    
    def solve(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.solve(n-1)+self.solve(n-2)

    def solve2(self, n):
        results = [0]*(n+1)
        results[0], results[1] = 1, 2
        if n != 1 or n != 2:
            for i in range(2, n):
                results[i] = results[i-1] + results[i-2]
        
        return results[n-1]
    
    def solve3(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a + tmp
            a = tmp
        return b

    def solve4(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a + tmp
            a = tmp
        return b



time1 = time.time()


n = 50
pro = Solution()
print(pro.solve3(n))

time2 = time.time()
print(time2-time1)