#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
import time

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        money = {
            "5": 0,
            "10": 0,
            "20": 0
        }
        def haveChange(bill, money):
            if bill == 5:
                money["5"] += 1
                return True
            elif bill == 10:
                if money["5"] > 0:
                    money["5"] -= 1
                    money["10"] += 1
                    return True
            elif bill == 20:
                if money["10"] > 0 and money["5"] > 0:
                    money["5"] -= 1
                    money["10"] -= 1
                    money["20"] += 1
                    return True
                elif money["5"] >= 3:
                    money["5"] -= 3
                    money["20"] += 1
                    return True
            return False
        
        for bill in bills:
            if not haveChange(bill, money):
                return False
        return True

# @lc code=end

time1 = time.time()


n = [5,5,20,10,20]
pro = Solution()
print(pro.lemonadeChange(n))

time2 = time.time()
print(time2-time1)