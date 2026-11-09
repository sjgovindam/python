
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):

        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):

        if not self.stack:
            raise IndexError("Stack is empty")

        removed = self.stack.pop()

        if removed == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


def main():

    stack = MinStack()

    stack.push(5)
    stack.push(3)
    stack.push(7)
    stack.push(2)

    print("Minimum:", stack.getMin())  # 2

    stack.pop()

    print("Top:", stack.top())         # 7
    print("Minimum:", stack.getMin())  # 3

    stack.pop()

    print("Minimum:", stack.getMin())  # 3


if __name__ == "__main__":
    main()
