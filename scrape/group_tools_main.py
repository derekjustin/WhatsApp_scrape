from scrape.group_tools import GroupTools
from scrape.print_endpoints import *

def main():
    tool = GroupTools()
    while True:
        print("\n" + 10 * "#" + " GROUP TOOLS MENU " + 10 * "#" + "\nPlease choose one of the following options\n")
        user_input = input("\njoin_group: joins a single WhatsApp group\n\njoin_multiple_groups: joins all groups listed in a file\n\nquit: end program\n\nUSER INPUT: ")
        if user_input == ("join_group"):
            tool.join_group()
        elif user_input == ("join_multiple_groups"):
            tool.join_multiple_groups()
        elif user_input == ("quit"):
            break
        else:
            print("\n\n******** PLEASE ENTER A VALID OPTION OR 'quit' TO END PROGRAM.\n")
    print_endpoints()
    quit()