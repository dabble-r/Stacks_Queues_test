You will provide a link to your GitHub repository. You will NOT write any code in the answer slot. If you write code in the answer slot, it is an automatic 0.

I advise you make sure you tackle the BARE MINIMUM REQUIREMENTS before tackling anything else. Remember: your files should be PYTHON FILES. Those end in .py. If you turn in a file that is not a .py file, I will no longer save it as a .py file. If it fails to run because you saved the wrong file, you will earn a 0.

Thibodeaux's Tech Triage offers tech support fixing phones, computers, and the like. The company has a number of technology support tickets and no way to organize them! You will build Thibodeaux's a ticketing system.  This will be a command line interface (CLI) program.

This program should use a complex data structure  to manage the support tickets. This data structure should make logical sense for the program. Consider: support tickets tend to operate as first ticket submitted or opened is the first ticket worked on, processed, and resolved.

All support tickets should have a 4-character ticket number and the issue to be solved. For example: #0001 - PC won't turn on

                                                                                    ************* 

This program should be able to (bare minimum requirements):

1 - prompt the user to choose from a menu of actions to take (remember: menus should keep prompting and executing actions until the user chooses to quit) and wait for response
    * if the user does not choose a listed menu item, the program re-prompts the user until an appropriate option is chosen
2 - use the correct data structure
3 - add tickets to the data structure (open a ticket)
4 - print out a list of tickets still to be worked on (that is, list all open tickets)
5 - remove a ticket from the data structure (close the ticket)
6 - the ticket to be closed should print out to the screen
    * You will have to determine what data structure should be used here (a stack or a queue).

For work that exceeds expectations, the program should also be able to:

1 - store all closed tickets in an appropriate data structure that implements last-in, first-out ( stack )
2 - this data structure should also be accessible from the menu with options to
    * "Review All Closed Tickets" to print out all closed tickets
    * "Review Previously Closed Ticket" to review the last closed ticket
3 - utilizes an additional class to create the ticket data used in the data structure's node

The ideal solution (i.e. the best solution) is  one that:

1 - utilizes an additional class to create the ticket data used in the data structure's node
2 - implements the Review All Closed Tickets functionality (will require another data structure)
3 - implements the Review Previously Closed Ticket functionality  (will require another data structure)

Below is a sample menu and output for the IDEAL solution. This is not exhaustive:

Welcome to Thibodeaux's Tech Triage
-----------------------------------
Type the number for the action you wish to perform and then hit Enter.
1. Open a new ticket
2. List All Open Tickets
3. Close ticket
4. Review All Closed Tickets
5. Review The Last Closed Ticket
6. Quit
What do you want to do? __7
I'm sorry, that is not an appropriate action.
    
Type the number for the action you wish to perform and then hit Enter.
1. Open a new ticket
2. List All Open Tickets
3. Close ticket
4. Review All Closed Tickets
5. Review The Last Closed Ticket
6. Quit
What do you want to do?__1
      Ticket Number: 0001
      Ticket: PC won't turn on
Ticket opened!

Type the number for the action you wish to perform and then hit Enter.
1. Open a new ticket
2. List All Open Tickets
3. Close ticket
4. Review All Closed Tickets
5. Review The Last Closed Ticket
6. Quit
What do you want to do?__1
      Ticket Number: 0002
      Ticket: Phone screen broke
Ticket opened!

Type the number for the action you wish to perform and then hit Enter.
1. Open a new ticket
2. List All Open Tickets
3. Close ticket
4. Review All Closed Tickets
5. Review The Last Closed Ticket
6. Quit
What do you want to do?__2
      Open Tickets:
      #001 PC won't turn on
      #002 Phone screen broke