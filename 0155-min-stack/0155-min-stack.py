class MinStack:

    def __init__(self):
        self.nums = []
        self.mins = []

    def push(self, val: int) -> None:
        self.nums.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            if self.mins[-1] > val:
                self.mins.append(val)
            else:
                self.mins.append(self.mins[-1])
        

    def pop(self) -> None:
        self.mins.pop()
        self.nums.pop()
        

    def top(self) -> int:
        return self.nums[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()