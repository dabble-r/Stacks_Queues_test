from node import Node 
from ticket import Ticket 
from stack import Stack 
from queue_t import Queue
from menus import Menus

def main():
  menus = Menus()
  curr_tickets_q = Queue()
  closed_tickets_s = Stack()
  #user_input = menus.get_input_1()
  flag = True
  while flag is True:
    user_action = menus.do_action(closed_tickets_s, curr_tickets_q)
    if user_action == 6:
      flag = False

if __name__ == "__main__":
  main()
