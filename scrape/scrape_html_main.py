from scrape.scrape_html import MultiProcessHtml
from scrape.print_endpoints import *
from scrape.system_tools import SystemTools

def main():
    system_tools = SystemTools()
    scrape_html = MultiProcessHtml()
    while True:
        print("\n" + 10 * "#" + " GROUP SCRAPE MENU " + 10 * "#" + "\nPlease choose one of the following options\n")
        user_input = input("\nscrape_html_messages: scrape all messages from folder " +  system_tools.get_html_dir_path() + "\n\n" +
                           "back: return to main menu\n\nUSER INPUT: ")
        print("")
        if user_input == ("scrape_html_messages"):
            scrape_html.process_all_raw_html_to_pickles()
            print( "\n\n\n *****Scraped messages saved to*****\n" + system_tools.get_processed_html_pickles_dir() )
        elif user_input == ("back"):
            break
        else:
            print("\n\n******** PLEASE ENTER A VALID OPTION OR 'quit' TO END PROGRAM.\n")
    print_endpoints()
    quit()
