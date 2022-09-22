class Solution(object):
    def numRange(self, end, front):
        if front - end == 1:
            return 
        elif front - end == 2:
            return str(end + 1)
        else:
            return str(end + 1) + "->" + str(front - 1)
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ans = []
        if not nums:
            ans.append( self.numRange(lower-1, upper+1) )
        else:
            if lower < nums[0]:
                ans.append( self.numRange(lower-1, nums[0]) )

            for i in range(len(nums) - 1):
                ans.append( self.numRange(nums[i], nums[i+1]) )

            if upper > nums[-1]:
                ans.append( self.numRange(nums[-1], upper+1) )
        ans = [num for num in ans if num]
        return ans
    def findMissingRanges2(self, nums, lower, upper):
        # 有两种情况会加入数字，一种是中间只是隔了一个数字，一种是中间隔了多个
        ans, prev = [], lower - 1
        nums.append(upper + 1)
        for num in nums:
            if num - 1 > prev + 1:
                ans.append("{}->{}".format(prev+1, num-1))
            elif num - 1 == prev + 1:
                ans.append("{}".format(num-1))
            prev = num
        return ans
            

nums = [0,1,3,50,75]
lower = 0
upper = 99
pro = Solution()
print(pro.findMissingRanges2(nums, lower, upper))
