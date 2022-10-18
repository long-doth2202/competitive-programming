class ListNode:
  def __init__(self, key, val, nxt):
    self.key = key
    self.val = val
    self.nxt = nxt

class MyHashMap:

  def __init__(self):
    self.size = 19997
    self.mult = 12582917
    self.data = [None for i in range(self.size)]
  
  def hash(self, key):
    return key * self.mult % self.size
      
  def put(self, key: int, val: int) -> None:
    self.remove(key)
    h = self.hash(key)
    node = ListNode(key, val, self.data[h])
    self.data[h] = node

  def get(self, key: int) -> int:
    h = self.hash(key)
    node = self.data[h]
    while node:
      if node.key == key: return node.val
      node = node.nxt
    return -1

  def remove(self, key: int) -> None:
    h = self.hash(key)
    node = self.data[h]
    if not node: return
    if node.key == key:
      self.data[h] = node.nxt
      return
    while node.nxt:
      if node.nxt.key == key:
        node.nxt = node.nxt.nxt
        return
      node = node.nxt