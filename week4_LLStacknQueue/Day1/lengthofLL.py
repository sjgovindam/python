class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findLength(head):

    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    return count


def main():

    head = ListNode(10)
    head.next = ListNode(20)
    head.next.next = ListNode(30)
    head.next.next.next = ListNode(40)
    head.next.next.next.next = ListNode(50)

    print("Length:", findLength(head))


if __name__ == "__main__":
    main()