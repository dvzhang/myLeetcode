from collections import defaultdict
import time

def def_value():
    return []

class Solution():
    def __init__(self):
        pass
    
    def solve(self, strs):
        letters_to_words = defaultdict(def_value)
        for s in strs:
            letters_to_words[tuple(sorted(s))].append(s)
        return letters_to_words.values()
    
    def solve2(self, strs):
        
        letters_to_words = defaultdict(def_value)
        for s in strs:
            letters_to_words[''.join(sorted(s))].append(s)
        return letters_to_words.values()
        

time1 = time.time()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
pro = Solution()
print(pro.solve2(strs))
time2 = time.time()
print(time2-time1)