#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        arr = str(x)
        for i in range(int(len(arr)/2+1)):
            if arr[i] != arr[-1 - i]:
                return False
        return True
    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

    def isPalindrome3(self, x: int) -> bool:
        # 创建逆序数字
        if x < 0:
            return False
        inputNum, reverseNum = x, 0
        while inputNum > 0:
            reverseNum = reverseNum*10 + inputNum%10
            inputNum = inputNum // 10
        return x == reverseNum

# @lc code=end
     
import time
time1 = time.time()

n = 121
pro = Solution()
print(pro.isPalindrome3(n))

time2 = time.time()
print(time2-time1)