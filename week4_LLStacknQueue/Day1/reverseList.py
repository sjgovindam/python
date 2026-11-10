class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):

    prev = None
    current = head

    while current:

        next_node = current.next

        current.next = prev

        prev = current
        current = next_node

    return prev


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("null")


def main():

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original:")
    printList(head)

    head = reverseList(head)

    print("Reversed:")
    printList(head)


if __name__ == "__main__":
    main()