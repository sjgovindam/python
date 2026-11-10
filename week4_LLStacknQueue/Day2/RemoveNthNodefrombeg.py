def remove_nth_node(head, n):

    if head is None or n <= 0:
        return head

    if n == 1:
        return head.next

    current = head

    for i in range(1, n - 1):
        if current is None:
            return head
        current = current.next

    if current and current.next:
        current.next = current.next.next

    return head