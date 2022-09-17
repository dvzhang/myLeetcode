#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        next1, next2 = list1, list2
        re1 = True
        if next1.val < next2.val:
            ans = next1
            next1 = next1.next
        else: 
            ans = next2
            next2 = next2.next
            re1 = False

        while next1 and next2:
            if next1.val < next2.val:
                ans.next = next1
                next1 = next1.next
            else:
                ans.next = next2
                next2 = next2.next
            ans = ans.next

        if next1:
            ans.next = next1
        if next2:
            ans.next = next1
        
        if re1:
            return list1
        else: 
            return list2
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 精妙，如何记录要返回的取值
        dummy = cur = ListNode(0)
        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        # 精妙，如何将链中剩下的元素连上来
        cur.next = list1 or list2

        return dummy
# @lc code=end

