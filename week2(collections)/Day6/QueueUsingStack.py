
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Insert element
    def enqueue(self, x):
        self.stack1.append(x)

    # Remove front element
    def dequeue(self):

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            raise IndexError("Queue is empty")

        return self.stack2.pop()

    # Get front element
    def peek(self):

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            raise IndexError("Queue is empty")

        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2


def main():

    queue = MyQueue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(queue.peek())     # 10
    print(queue.dequeue())  # 10
    print(queue.dequeue())  # 20

    queue.enqueue(40)

    print(queue.dequeue())  # 30
    print(queue.dequeue())  # 40

    print(queue.empty())    # True


if __name__ == "__main__":
    main()
