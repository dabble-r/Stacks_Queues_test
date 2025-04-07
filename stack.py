from node import Node

class Stack():
  def __init__(self):
    self.top = None 
    self.size = 0 
  
  def __str__(self):
    ret = ''
    ret += '\nStack - LIFO\n'
    ret += len(ret) * '=' + '\n'
    if self.top is None:
      print('Stack is empty!')
      return ret
    traverser = self.top 
    while traverser is not None:
      ret += f'{traverser.val}\n'
      traverser = traverser.next 
    return ret

  def push(self, val):
    new_node = Node(val)
    if self.top is None:
      self.top = new_node 
    else:
      temp = self.top 
      self.top = new_node
      self.top.next = temp 
    self.size += 1

  def pop(self):
    if self.top is None:
      print('Stack is empty!')
      return 
    temp = self.top 
    self.top = temp.next 
    self.size -= 1
    return temp.val 
  
  def get_last(self):
    if self.top is None:
      print('Stack is empty!')
      return None 
    return self.top.val
  
   