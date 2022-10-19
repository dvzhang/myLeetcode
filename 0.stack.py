# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.maxes = []
        self.minies = []
        self.storage = []
        
    def peek(self):
        # Write your code here.
        return self.storage[-1] if self.storage else None

    def pop(self):
        # Write your code here.
        if self.storage:
            self.maxes.pop()
            self.minies.pop()
            return self.storage.pop()
        else: return None
            
    def push(self, number):
        # Write your code here.
        if self.storage:
            self.maxes.append(number if number > self.maxes[-1] else self.maxes[-1])
            self.minies.append(number if number < self.minies[-1] else self.minies[-1])
        else:
            self.maxes.append(number)
            self.minies.append(number)
        self.storage.append(number)
        
    def getMin(self):
        # Write your code here.
        if self.storage:
            return self.minies[-1]
        return None

    def getMax(self):
        # Write your code here.
        if self.storage:
            return self.maxes[-1]
        return None
