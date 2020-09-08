from inspect import signature
# need to add menu description parameter

class Menu():
    """The menu class takes a list of choices, prints a menu in the console, and gets and returns a user choice"""
    
    def __init__(self, *args):
        self.args = args

    def append(self, arg):
        pass

    def print_menu(self):
        for i, choice in enumerate(self.args, 1):
            print(f'[{i}] {choice}')
        print('\n')

    def get_input(self):
        choice = input("> ")
        return choice

### runs menu
##if choice == '1':
##player.show_player_status()
##elif choice == '2':
##player.current_location.show_description()
##elif choice == '3':
##player.mine()
##elif choice == '4':
##player.breathe()
##elif choice == '5':
##player.set_location()
##elif choice != 'q':
##print("Invalid choice\n")
##else:
##print("Quitting...\n")
