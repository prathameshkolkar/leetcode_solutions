class MinStack:

    def __init__(self):
        self.s=[]
        self.minst=[]

    def push(self, val: int) -> None:
        self.s.append(val)
        print("pushed: ",val)
        if not self.minst or self.minst[-1]>=val:
            self.minst.append(val)

        

    def pop(self) -> None:
        if len(self.s)==0:
            print("list is empty")
        else:
            p=self.s.pop()
            if p==self.minst[-1]:
                self.minst.pop()
                

    def top(self) -> int:
        return self.s[-1]

        

    def getMin(self) -> int:
        return self.minst[-1]


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()