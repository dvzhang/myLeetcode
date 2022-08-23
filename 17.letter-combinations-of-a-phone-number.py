#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def comb(dict, digits, index, path, res):
            if index >= len(nums):
                res.append(path)
                return
            string1 = dict[digits[index]]
            for i in string1:
                comb(dict, digits, index+1, path + i, res)
        
        dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        results = []
        
        if len(digits) == 0:
            return results

        comb(dict, digits, 0, '', results)
        return results


# @lc code=end

