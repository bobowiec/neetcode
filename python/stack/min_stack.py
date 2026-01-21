class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        if not self.stack:
            return None
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            raise IndexError("getMin from empty stack")
        return self.min_stack[-1]
