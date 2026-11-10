class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):

    dummy = ListNode(-1)
    dummy.next = head

    slow = dummy
    fast = dummy

    # Move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both pointers
    while fast.next:
        slow = slow.next
        fast = fast.next

    # Remove node
    slow.next = slow.next.next

    return dummy.next


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

    head = removeNthFromEnd(head, 2)

    printList(head)


if __name__ == "__main__":
    main()