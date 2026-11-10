class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycle(head):

    slow = head
    fast = head

    # Step 1: Detect cycle
    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow is fast:

            # Step 2: Find cycle start
            slow = head

            while slow is not fast:
                slow = slow.next
                fast = fast.next

            return slow

    return None


def main():

    head = ListNode(10)
    head.next = ListNode(20)
    head.next.next = ListNode(30)
    head.next.next.next = ListNode(40)
    head.next.next.next.next = ListNode(50)

    # Create cycle: 50 -> 30
    node30 = head.next.next
    node50 = head.next.next.next.next

    node50.next = node30

    cycle_start = detectCycle(head)

    if cycle_start:
        print("Cycle starts at:", cycle_start.val)
    else:
        print("No cycle found")


if __name__ == "__main__":
    main()