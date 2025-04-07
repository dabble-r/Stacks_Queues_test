from node import Node 
import math

class Queue():
  def __init__(self, max=math.inf):
    self.front = None 
    self.rear = None 
    self.size = 0
    self.max = max
  
  def __str__(self):
    ret = ''
    ret += '\nQueue - FIFO\n'
    ret += len(ret) * '=' + '\n'
    if self.front is None:
      print('Queue is empty!')
      return ret 
    traverser = self.front 
    while traverser is not None:
      ret += f'{traverser.val}\n'
      traverser = traverser.next 
    return ret
  
  def enqueue(self, val):
    new_node = Node(val)
    if self.front is None:
      self.front = self.rear = new_node
    else:
      temp = self.rear 
      temp.next = new_node 
      self.rear = new_node 
  
  def dequeue(self):
    if self.front is None:
      print('Queue is empty!')
      return 
    temp = self.front
    self.front = temp.next
    return temp.val
  
  def peek(self):
    if self.front is not None:
      return self.front.val
    print('Queue is empty!')
    return None