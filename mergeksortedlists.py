class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge(self, a, b):
        dummy = ListNode()
        current = dummy
        while(a and b):
            if(a.val < b.val):
                current.next = a
                a = a.next
            else:
                current.next = b
                b = b.next
            current = current.next
        if(a):
            current.next = a
        else:
            current.next = b
        return dummy.next
    def mergeKLists(self, lists):
        if(len(lists) == 0):
            return None
        
        while(len(lists) > 1):
            merged = []
            for i in range(0, len(lists), 2):
                if(i + 1 == len(lists)):
                    merged.append(lists[i])
                else:
                    merged.append(self.merge(lists[i], lists[i+1]))
            lists = merged
        
        return lists[0]
