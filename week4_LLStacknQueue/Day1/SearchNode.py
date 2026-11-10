class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def searchNode(head, target):

    current = head

    while current:

        if current.val == target:
            return True

        current = current.next

    return False


def main():

    head = ListNode(10)
    head.next = ListNode(20)
    head.next.next = ListNode(30)
    head.next.next.next = ListNode(40)
    head.next.next.next.next = ListNode(50)

    target = 30

    if searchNode(head, target):
        print(target, "found in Linked List")
    else:
        print(target, "not found in Linked List")


if __name__ == "__main__":
    main()