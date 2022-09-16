

from heapq import merge


class Solution():
    def sort(self, arr, type="quick"):
        if type=="quick":
            return self.quickSort2(arr, 0, len(arr)-1)
        if type=="merge":
            return self.mergeSort2(arr, 0, len(arr)-1)

        
    def quickSort(self, arr, l, r):
        if l < r:
            i = self.partition(arr, l, r)
            self.quickSort(arr, l, i-1)
            self.quickSort(arr, i+1, r)
        return arr

    def partition(self, arr, l, r):
        j = l - 1
        target = arr[r]
        for i in range(l, r):
            if arr[i] < target:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]
        j += 1
        arr[j], arr[r] = arr[r], arr[j]
        return j


    def mergeSort(self, arr, l, r):
        if l < r:
            m = int((l + r - 1) / 2)
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m+1, r)
            self.merge(arr, l, m, r)
        return arr
    
    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        
        # create two tmp array to store the value
        tmp1 = [] 
        for i in range(l, m+1):
            tmp1.append(arr[i])
        tmp2 = []
        for i in range(m+1, r+1):
            tmp2.append(arr[i])
        
        # merge two tmp array
        i, j, q= 0, 0, l
        while i < n1 and j < n2:
            if tmp1[i] < tmp2[j]:
                arr[q] = tmp1[i]
                i += 1
            else:
                arr[q] = tmp2[j]
                j += 1
            q += 1
        while i < n1:
            arr[q] = tmp1[i]
            q += 1
            i += 1
        while j < n2:
            arr[q] = tmp2[j]
            q += 1
            j += 1




import time
time1 = time.time()
arr = [10, 7, 8, 9, 1, 5, 10, 7, 8, 9, 1, 5] 
arr = [10, 7, 8, 9, 1, 5] 
pro = Solution()
print(pro.sort(arr, type="merge"))

time2 = time.time()
print(time2-time1)