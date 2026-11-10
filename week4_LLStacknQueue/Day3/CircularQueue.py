class CircularQueue:

    def __init__(self, k):
        self.capacity = k
        self.arr = [0] * k
        self.front = 0
        self.rear = -1
        self.size = 0

    def enQueue(self, value):

        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = value
        self.size += 1

        return True

    def deQueue(self):

        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        return True

    def Front(self):

        if self.isEmpty():
            return -1

        return self.arr[self.front]

    def Rear(self):

        if self.isEmpty():
            return -1

        return self.arr[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


def main():

    queue = CircularQueue(5)

    queue.enQueue(10)
    queue.enQueue(20)
    queue.enQueue(30)
    queue.enQueue(40)
    queue.enQueue(50)

    print("Front:", queue.Front())
    print("Rear:", queue.Rear())

    queue.deQueue()
    queue.deQueue()

    queue.enQueue(60)
    queue.enQueue(70)

    print("Front:", queue.Front())
    print("Rear:", queue.Rear())

    print("Is Full:", queue.isFull())
    print("Is Empty:", queue.isEmpty())


if __name__ == "__main__":
    main()