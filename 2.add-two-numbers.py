#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        while l1:
            num1.append(l1)
            l1 = l1.next
        while l2:
            num2.append(l2)
            l2 = l2.next
        num1 = int("".join(num1)[::-1])
        num2 = int("".join(num2)[::-1])
        res = str(num1+num2)[::-1]
        ans = node = ListNode(val=int(res[0]))
        for i in range(1, len(res)):
            node.next = ListNode(val=int(res[i]))
            node = node.next
        return ans

            
# @lc code=end

