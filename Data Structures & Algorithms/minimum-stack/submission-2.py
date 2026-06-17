class MinStack:
# key is O(1) time complex, revolves around getMin
# 2 stack solution
# 1 stack is real
# other stack keeps track of current min so far
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
# this is where core logic lies as well as in pop()
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
# if the val or last elem in minstack is lower, we still append another minstack elem
# i need to check if my minstack is empty to avoid invalid index
        else:
            min_val = min(val, self.minstack[-1])
            self.minstack.append(min_val)

    def pop(self) -> None:
        # since we are keeping the current lowest, we dont care about popping
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

# I've got to watch the cases for arrays being empty and determine if accessing them is safe or not