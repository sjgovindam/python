class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNode(head, target):

    if head is None:
        return None

    if head.val == target:
        return head.next

    current = head

    while current.next and current.next.val != target:
        current = current.next

    if current.next:
        current.next = current.next.next

    return head


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("null")


def main():

    head = ListNode(10)
    head.next = ListNode(20)
    head.next.next = ListNode(30)
    head.next.next.next = ListNode(40)
    head.next.next.next.next = ListNode(50)

    head = removeNode(head, 30)

    printList(head)


if __name__ == "__main__":
    main()