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

        
        
        return generate(2*n, "")

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


time1 = time.time()


n = 2
pro = Solution()
print(pro.solve(n))

time2 = time.time()
print(time2-time1)
