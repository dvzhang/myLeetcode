class TwoSum(object):

    def __init__(self):
        self.data = []

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.data.append(number)
        self.data.sort()


    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """
        front, end = 0, len(self.data) - 1
        while front < end:
            if self.data[front] + self.data[end] > value:
                end -= 1
            elif self.data[front] + self.data[end] < value:
                front += 1
            else: 
                return True
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)