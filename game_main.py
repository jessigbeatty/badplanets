import os
import time
import threading

from location import Location
from player import Player
from menu import Menu

############################ THREADING ###############################

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # get lock to sync threads
        threadLock.acquire()
        clock()
        # free lock to release next thread
        threadLock.release()

def clock():
    t = 0
    while True:
        return (t)
        t += 1
        time.sleep(1)

threadLock = threading.Lock()
threads = []

# create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

############################## FUNCTIONS ############################## 

def show_title():
    # clears screen and prints title graphic
    os.system('clear')
    print("                                                                            .::. ")
    print("                                                                         .:'  .: ")
    print("                                                               ,MMM8&&&.:'   .:' ")
    print("                                                              MMMMM88&&&&  .:'   ")
    print("                    BAD PLANETS                              MMMMM88&&&&&&:'     ")
    print("                                                             MMMMM88&&&&&&       ")
    print("                                                           .:MMMMM88&&&&&&       ")
    print("                                                         .:'  MMMMM88&&&&        ")
    print("                                                       .:'   .:'MMM8&&&'         ")
    print("                                                       :'  .:'                   ")
    print("                                                       '::'                    \n")
    print(f"  =============================================================================" + str(clock()) + "\n")

def get_location(key):
    if key == '1':
        return alpha
    elif key == '2':
        return beta

########################### SETUP ###############################

# define game world. definitely a better place to do this, maybe its own file game_world?
alpha = Location("on a rocky planet", "It's rocky and bad.", 1000, )
alpha_orbit = Location("orbiting a rocky planet", "", 0, )
beta = Location("on a desert planet", "It's sandy and bad.", 500, )
beta_orbit = Location("orbiting a desert planet", "", 0, )

player = Player(alpha, 0, 0)

mainMenu = Menu('Check your status', 'Scan your surroundings', 'Mine', 'Breathe', 'Move', 'Quit')

locationMenu = Menu('Alpha', 'Beta')
############################## MAIN ############################## 

show_title()

choice = ''

# loop while user doesn't quit
running = True
while running == True:
    mainMenu.print_menu()
    choice = mainMenu.get_input()
    show_title()

  # runs mainMenu
    if choice == '1':
        player.show_status()
    elif choice == '2':
        player.current_location.show_description()
    elif choice == '3':
        player.mine()
    elif choice == '4':
        player.breathe()
    elif choice == '5':
        locationMenu.print_menu()
        key = locationMenu.get_input()              # gets numerical key of location
        destination = get_location(key)             # returns name of destination
        player.current_location = destination       # sets player location to destination
    elif choice == '6':
        running = False
        print("Quitting...\n")
    else:
        print("Invalid choice\n")
