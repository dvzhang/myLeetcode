class problem():
    def __init__(self):
        pass
    def solve(self, s, t):
        return sorted(s)==sorted(t)
    def solve2(self, s, t):
        hash = {}
        for ch in s:
            hash[ch] = hash.get(ch, 0) + 1
        for ch in t:
            hash[ch] = hash.get(ch, 0) - 1
        for value in hash.values():
            if value != 0:
                return False
        return True
    def solve3(self, s, t):
        dict = [0]*26
        for ch in s:
            dict[ord(ch) - ord('a')] += 1
        for ch in t:
            dict[ord(ch) - ord('a')] -= 1
        for value in hash.values():
            if value != 0:
                return False
        return True
        


s = "anagram"
t = "nagaram"
pro = problem()
print(pro.solve2(s, t))
