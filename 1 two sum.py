from collections import defaultdict
import time

def def_value():
    return []

class Solution():
    def __init__(self):
        pass
    
    def solve(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if( nums[i] + nums[j] == target ):
                    return [i, j]

    def solve2(self, nums, target):
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - value
            
            if ( str(remaining) in seen ):
                return [i, seen[str(remaining)]]
            seen[str(value)] = i

        

time1 = time.time()

nums = [2,7,11,15]
target = 9
pro = Solution()
print(pro.solve2(nums, target))

time2 = time.time()
print(time2-time1)