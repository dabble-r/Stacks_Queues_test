import math
import random
from ticket import Ticket


class Menus():
  def __init__(self):
    self.options = [
      {'1) Open a new ticket': lambda: self.get_action()}, 
      {'2) List all open tickets': lambda: self.get_action()}, 
      {'3) Close a ticket': lambda: self.get_action()}, 
      {'4) Review all closed tickets': lambda: self.get_action()},
      {'5) Review Last Closed Ticket': lambda: self.get_action()},
      {'6) Quit': lambda: print('quit')}
    ]
  
  def __str__(self):
    ret = ''
    ret += 'User Menu\n'
    for el in self.options:
      key = list(el.keys())[0]
      ret += f'{key}\n'
    return ret

  def get_input_1(self):
    print(self)
    raw = input('Choose a menu item: ')
    try:
      indx = int(raw) - 1
      if indx <= len(self.options):
        #print('hello')
        return indx + 1
    except:
      print('Error: Enter a valid menu option')
    
  
  def do_action(self, stack, queue):
    action = self.get_input_1()
    #print('action', action)
    match action:
      case 1:
        new_ticket = Ticket()
        queue.enqueue(new_ticket)
        print(new_ticket)
      case 2:
        print(queue)
      case 3:
        last_ticket = queue.dequeue()
        print(f'Closing ticket!\n{last_ticket}')
        stack.push(last_ticket)
      case 4:
        print(stack)
      case 5:
        last_closed_ticket = stack.get_last()
        print(f'Last ticket:\n{last_closed_ticket}')
      case 6:
        print('Ending sessions!\n')
        return 6

  def rand_num(self):
    ticket_id = random.randint(100,1000)
    return ticket_id
  
  def user_continue(self):
    action_1 = input('Would you like to continue? y/n').lower()
    if action_1 == 'y':
      self.do_action()
    elif action_1 == 'n':
      return 
    else:
      action_1 = input('Enter a valid response: y/n')

    
  

