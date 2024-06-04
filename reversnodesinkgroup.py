class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseKGroup(head, k):
    if(k == 1):
        return head
    dummy = ListNode()
    tail = dummy
    curr = head
    while(curr):
        check = curr
        for i in range(k):
            if(check):
                check = check.next
            else:
                tail.next = curr
                return dummy.next

        for i in range(k):
            if(curr):
                if(i == 0):
                    buffer = curr
                    prev = None
                elif(i == k - 1):
                    tail.next = curr
                    tail = buffer
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
    return dummy.next
