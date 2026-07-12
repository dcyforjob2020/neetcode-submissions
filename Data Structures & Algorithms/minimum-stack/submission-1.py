class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        min_val = val

        if self.min_stack:
            min_val = min(self.min_stack[-1], val)

        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]


    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        
