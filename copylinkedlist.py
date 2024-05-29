
# Definition for a Node.
class Node:
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    if not head:
        return None
    ref = dict()
    a = head
    while a:
        node = Node(x=a.val)
        ref[a] = node
        a = a.next

    a = head
    while a:
        current = ref[a]
        if a.next:
            current.next = ref[a.next]
        if a.random:
            current.random = ref[a.random]
        a = a.next

    return ref[head]
