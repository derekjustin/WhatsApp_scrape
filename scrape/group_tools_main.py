from scrape.group_tools import GroupTools

def main():
    tool = GroupTools()
    while True:
        print("\n" + 10 * "#" + " GROUP TOOLS MENU " + 10 * "#" + "\nPlease choose one of the following options\n")
        user_input = input("\njoin_group: joins a single WhatsApp group\n\nquit: end program\n\nUSER INPUT: ")
        if user_input == ("join_group"):
            tool.join_group()
        elif user_input == ("quit"):
            quit()
        else:
            print("\n\n******** PLEASE ENTER A VALID OPTION OR 'quit' TO END PROGRAM.\n")