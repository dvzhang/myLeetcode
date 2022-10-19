from collections import defaultdict
from collections import Counter
import time

def longestPalindromicSubstring(string):
    # Write your code here.
    if not string:
        return
    ans = string[0]
    for i in range(len(string)-1):
        for j in range(i+len(ans), len(string)+1):
            if string[i:j] == string[i:j][::-1] and j - i > len(ans):
                ans = string[i:j]    
    return ans

def defV():
    return []

def groupAnagrams(words):
    # Write your code here.
    ans = defaultdict(defV)
    for word in words:
        sWord = "".join(sorted(word))
        ans[sWord].append(word)
        
    ansArray = [i for i in ans.values()]
    return ansArray

def groupAnagrams2(words):
    # Write your code here.
    ans = {}
    for word in words:
        key = frozenset(Counter(word).items())
        if key not in ans:
            ans[key] = []
        ans[key].append(word)
    return list(ans.values())

def isValidNum(num):
    if len(num) > 1 and num[0] == "0":
        return False
    return 0 <= int(num) <= 255

def validIPAddresses(string):
    # Write your code here.
    ans = []
    for i in range(1, len(string)-2):
        for j in range(i+1, len(string)-1):
            for k in range(j+1, len(string)):
                if isValidNum(string[:i]) and isValidNum(string[i:j]) and isValidNum(string[j:k]) and isValidNum(string[k:]):
                    ans.append("{}.{}.{}.{}".format(string[:i], string[i:j], string[j:k], string[k:]))

    return ans


print(longestPalindromicSubstring("noon"))
time1 = time.time()

print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))
time2 = time.time()
print(time2-time1)
print(groupAnagrams2(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))
time3 = time.time()
print(time3-time2)

print(validIPAddresses("1921680"))