class MinStack:

    def __init__(self):
        self.elements = []
        

    def push(self, value: int) -> None:
        self.elements.append(value)
        

    def pop(self) -> None:
        return self.elements.pop()
        

    def top(self) -> int:
        return self.elements[-1]

    # def getMin(self) -> int:

stack = MinStack()
print(stack.__dict__)

stack.push(3)
stack.push("testing")
print(stack.top())
# print(stack.pop())