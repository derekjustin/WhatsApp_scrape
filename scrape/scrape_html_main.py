from scrape.scrape_html import MultiProcessHtml
from scrape.print_endpoints import *
from scrape.system_tools import SystemTools
import pandas as pd
import glob
import os


def main():

    system_tools = SystemTools()
    scrape_html = MultiProcessHtml()
    while True:
        print("\n" + 10 * "#" + " GROUP SCRAPE MENU " + 10 * "#" + "\nPlease choose one of the following options\n")
        user_input = input("\ngenerate_message_csv: generate a csv and save to " + system_tools.get_cwd_path() + "\n\n"
                           "back: return to main menu\n\nUSER INPUT: ")
        print("")
        if user_input == ("generate_message_csv"):
            scrape_html.process_all_raw_html_to_pickles()
            df = pd.DataFrame()
            df = scrape_html.get_message_frame_all_groups(glob.glob(os.getcwd() + "/scrape/group_files/processed_html_pickles/*.pkl"))
            scrape_html.generate_message_summary_csv(df)
        elif user_input == ("back"):
            break
        else:
            print("\n\n******** PLEASE ENTER A VALID OPTION OR 'quit' TO END PROGRAM.\n")
    print_endpoints()
    quit()
