class Node:
    def __init__(self, val =0, next=None):
        self.val = val
        self.next = next

def removeNthNode(head, n):
    count = 0
    current = head
    while(current):
        count += 1
        current = current.next

    pos = count - n
    dummy = Node()
    dummy.next = head
    current = head
    count = 0

    while(count != pos):
        current = current.next
        count += 1
    current.next = current.next.next

    return dummy.next
