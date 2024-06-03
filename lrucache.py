class Node:
  def __init__(self, key, val, prev=None, next= None):
    self.key = key
    self.val = val
    self.prev = prev
    self.next = next

class LRUCache:
    def __init__(self, capacity: int):
      self.capacity = capacity
      self.hash = dict()
      self.lru = None
      self.mru = None

    def get(self, key: int) -> int:
      if(key not in self.hash):
        return -1

      node = self.hash[key] 
      if(node != self.lru and node != self.mru):
        node.next.prev = node.prev
        node.prev.next = node.next

      if(node == self.lru and node.prev):
        self.lru = node.prev
        self.lru.next = None
      
      if(node != self.mru):
        self.mru.prev = node
        node.next = self.mru
        self.mru = node
        node.prev = None
      
      return node.val

    def put(self, key: int, value: int) -> None:
      if(key in self.hash):
        node = self.hash[key]
        node.val = value

        if(node != self.lru and node != self.mru):
          node.next.prev = node.prev
          node.prev.next = node.next
        if(self.lru == node and node.prev):
          self.lru = node.prev
          self.lru.next = None
        if(self.mru != node):
          self.mru.prev = node
          node.next = self.mru
          self.mru = node
          node.prev = None
      else:
        if(len(self.hash) < self.capacity):
          node = Node(key=key, val=value)
          self.hash[key] = node
          if(not self.lru):
            self.lru = node
          if(not self.mru):
            self.mru = node
          else:
            self.mru.prev = node
            node.next = self.mru
            self.mru = node
        elif(len(self.hash) == self.capacity):
          node = Node(key=key, val=value)
          del self.hash[self.lru.key]
          self.hash[key] = node
  
          self.mru.prev = node
          node.next = self.mru
          self.mru = node
  
          if(self.lru.prev):
            self.lru = self.lru.prev
          else:
            self.lru = node
          self.lru.next = None
