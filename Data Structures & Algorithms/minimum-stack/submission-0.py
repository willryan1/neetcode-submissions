class MinStack:

    def __init__(self):
        self.d = {}
        self.stack = deque()

    def push(self, val: int) -> None:
        if not self.stack:
            self.d[1] = val
        else:
            if val < self.d[len(self.stack)]:
                self.d[len(self.stack) + 1] = val
            else:
                self.d[len(self.stack) + 1] = self.d[len(self.stack)]
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.d[len(self.stack)]
