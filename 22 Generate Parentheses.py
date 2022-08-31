from cgitb import reset
from collections import defaultdict
from operator import ge
import time


def def_value():
    return []

# 1、穷举所有可能然后删除不符合的
# 2、提前剪枝，去除不合法的


class Solution():
    def __init__(self):
        pass

    def solve(self, n):
        def generate(n, p, results=[]):
            if (n == 0):
                results.append(p)
                return results
            generate(n-1, p=p + "(")
            generate(n-1, p=p + ")")
            return results
        def valid(s):
            stack = []
            for c in s:
                if c == "(":
                    stack.append(c)
                elif(len(stack)==0 or stack.pop()!="("):
                    return False
            return len(stack)==0
        results_bef = generate(2*n, "")
        results = []
        for result in results_bef:
            if(valid(result)):
                results.append(result)

        return results

    def solve2(self, n):
        def generate(p, left, right, parens=[]):
            if right == 0:
                parens.append(p)

            if (left):
                generate(p+"(", left-1, right)
            if (right > left):
                generate(p+")", left, right-1)
            return parens
        return generate('', n, n)

    def solve3(self, n):
        results = []
        def generate(path, n, left, right):
            if len(path) == 2 * n:
                if path not in results:
                    results.append(path)
                return
            if right >= left:
                generate(path+"(", n, left+1, right)
            elif left >= n:
                generate(path+")", n, left, right+1)
            else:
                generate(path+"(", n, left+1, right)
                generate(path+")", n, left, right+1)

        generate('', n, 0, 0)
        return results



time1 = time.time()


n = 3
pro = Solution()
print(pro.solve3(n))

time2 = time.time()
print(time2-time1)
