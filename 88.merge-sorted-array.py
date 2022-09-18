#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1, n2, j = 0, 0, 0
        num1_tem = [i for i in nums1]
        while n1 < m and n2 < n:
            if num1_tem[n1] < nums2[n2]:
                nums1[j] = num1_tem[n1]
                n1 += 1
            else:
                nums1[j] = nums2[n2]
                n2 += 1
            j += 1
        while n1 < m:
            nums1[j] = num1_tem[n1]
            n1 += 1
            j += 1

        while n2 < n:
            nums1[j] = nums2[n2]
            j += 1
            n2 += 1
        return nums1
    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        a, b, write_index = m-1, n-1, m + n - 1

        while b >= 0:
            if a >= 0 and A[a] > B[b]:
                A[write_index] = A[a]
                a -= 1
            else:
                A[write_index] = B[b]
                b -= 1

            write_index -= 1
        
# @lc code=end

import time
time1 = time.time()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
pro = Solution()
print(pro.merge(nums1, m, nums2, n))

time2 = time.time()
print(time2-time1)