def reverse_between(head, m , n):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(m - 1):
        prev = prev.next
    curr = prev.next

    for _ in range(n - m):
        next_node = curr.next
        curr.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
    return dummy.next