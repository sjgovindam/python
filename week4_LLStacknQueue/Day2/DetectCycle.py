class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


def main():

    head = ListNode(10)
    head.next = ListNode(20)
    head.next.next = ListNode(30)
    head.next.next.next = ListNode(40)
    head.next.next.next.next = ListNode(50)

    # Create cycle: 50 -> 30
    head.next.next.next.next.next = head.next.next

    print("Cycle exists:", hasCycle(head))


if __name__ == "__main__":
    main()