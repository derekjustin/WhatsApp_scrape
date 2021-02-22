from scrape.group_tools import GroupTools
from scrape.print_endpoints import *

def main():
    tool = GroupTools()
    while True:
        print("\n" + 10 * "#" + " GROUP TOOLS MENU " + 10 * "#" + "\nPlease choose one of the following options\n")
        user_input = input("\njoin_group: joins a single WhatsApp group\n\n" +
                           "join_multiple_groups: joins all groups listed in a file\n\n" +
                           "single_group_data: retrieves and saves raw html containing single group messages\n\n" +                           
                           "all_groups_data: retrieves and saves raw html containing group messages for all groups\n\n" +
                           "print_groups: prints group list to the console\n\n" +
                           "back: return to main menu\n\nUSER INPUT: ")
        print("")
        if user_input == ("join_group"):
            tool.join_group()
        elif user_input == ("join_multiple_groups"):
            tool.join_multiple_groups()
        elif user_input == ("single_group_data"):
            tool.save_single_groups_data()
        elif user_input == ("all_groups_data"):
            tool.save_all_groups_data()
        elif user_input == ("print_groups"):
            tool.print_groups()
        elif user_input == ("back"):
            break
        else:
            print("\n\n******** PLEASE ENTER A VALID OPTION OR 'quit' TO END PROGRAM.\n")
    print_endpoints()
    quit()