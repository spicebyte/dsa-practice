def reverseLinkedList(head):
    prev = None
    current = head
    while(current is not None):
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    return prev
