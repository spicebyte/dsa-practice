class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
  if(not head):
    return False

  slow = head
  fast = slow.next
  while(fast):
    if(slow == fast):
      return True
    slow = slow.next
    if(fast.next):
      fast = fast.next.next
    else:
      return False
  return False
