class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
  total = 0
  factor = 1
  a = l1
  while(a):
    total += a.val * factor
    factor *= 10
    a = a.next
  
  factor = 1
  while(l2):
    total += l2.val * factor
    factor *= 10
    l2 = l2.next
  
  if(total == 0):
    return l1

  dummy = ListNode()
  current = dummy
  while(total != 0):
    node = ListNode(val = total % 10)
    current.next = node
    current = node
    total = total // 10
  
  return dummy.next
