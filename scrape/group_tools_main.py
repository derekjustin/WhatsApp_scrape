from scrape.group_tools import GroupTools

def main():
    tool = GroupTools()
    user_input = input("Hey what ya wanna do?")
    if user_input == ('join_groups'):
        tool.join_groups()
