import math 
import random

class Ticket():
  def __init__(self):
    self.num = self.rand_num()
    self.info = self.get_info()
  
  def __str__(self):
    ret = 'Thibodeaux Tech\n'
    ret += len(ret) * '=' + '\n'
    ret += f'Ticket Number: {self.num}\n'
    ret += f'Info: {self.info}\n\n'
    return ret

  def rand_num(self):
    ticket_id = random.randint(100,1000)
    return ticket_id
  
  def get_info(self):
    user_info = input('\nEnter brief summary of problem: \n')
    return user_info
    #print('hello')