class MinStack:

    def __init__(self):

        self.nums = []
        self.cur_mins = []
        

    def push(self, val: int) -> None:
        self.nums.append(val)

        if not self.cur_mins or val <= self.cur_mins[-1]:
            self.cur_mins.append(val)

    def pop(self) -> None:
        num = self.nums.pop()

        if self.cur_mins and num == self.cur_mins[-1]:
            self.cur_mins.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.cur_mins[-1]
