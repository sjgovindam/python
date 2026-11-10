from collections import deque


def main():

    queue = deque()

    # Enqueue
    queue.append(10)
    queue.append(20)
    queue.append(30)
    queue.append(40)

    print("Queue:", list(queue))

    # Peek
    print("Front:", queue[0])

    # Dequeue
    print("Removed:", queue.popleft())

    print("After Dequeue:", list(queue))

    # Enqueue
    queue.append(50)

    print("After Enqueue:", list(queue))

    print("Size:", len(queue))

    print("Is Empty:", len(queue) == 0)


if __name__ == "__main__":
    main()