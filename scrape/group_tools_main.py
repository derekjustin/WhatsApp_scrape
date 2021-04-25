import pandas as pd

from scrape.group_tools import GroupTools
from scrape.scrape_html import MultiProcessHtml
from scrape.system_tools import SystemTools
from scrape.print_endpoints import *


def main(test=False):
    tool = GroupTools()
    scrape = MultiProcessHtml()
    system = SystemTools()
    last_func_called = ""

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
            tool.join_group_cli()
            last_func_called = "join_group"
        elif user_input == ("join_multiple_groups"):
            tool.join_multiple_groups_cli()
            last_func_called = "join_multiple_groups"
        elif user_input == ("single_group_data"):
            tool.save_single_groups_data_cli()
            last_func_called = "single_group_data"
        elif user_input == ("all_groups_data"):
            if test is False:
                tool.save_all_groups_data_cli()
            last_func_called = "all_groups_data"
        elif user_input == ("print_groups"):
            tool.print_groups()
            last_func_called = "print_groups"
        elif user_input == ("generate_csv"):
            df = pd.DataFrame()
            df = scrape.get_message_frame_all_groups(system.get_processed_pck_list())
            scrape.generate_message_summary_csv(df)
            last_func_called = "generate_csv"
        elif user_input == ("back"):
            break
        else:
            print("\n\n******** PLEASE ENTER A VALID OPTION OR 'back' TO END PROGRAM.\n")
            last_func_called = "invalid_input"
    print_endpoints()
    return last_func_called
