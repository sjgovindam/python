class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def get_intersection_node(headA, headB):

    pA = headA
    pB = headB

    while pA != pB:

        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next

    return pA


def main():

    # Common part: 30 -> 40 -> 50
    common = ListNode(30)
    common.next = ListNode(40)
    common.next.next = ListNode(50)

    # List A: 10 -> 20 -> 30 -> 40 -> 50
    headA = ListNode(10)
    headA.next = ListNode(20)
    headA.next.next = common

    # List B: 15 -> 25 -> 30 -> 40 -> 50
    headB = ListNode(15)
    headB.next = ListNode(25)
    headB.next.next = common

    intersection = get_intersection_node(headA, headB)

    if intersection:
        print("Intersection at node:", intersection.val)
    else:
        print("No intersection")


if __name__ == "__main__":
    main()