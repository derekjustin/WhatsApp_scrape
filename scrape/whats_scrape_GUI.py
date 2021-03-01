import PySimpleGUI as sg

from scrape.group_tools import GroupTools


class WhatsScrapeGUI:

    def __init__(self):
        self.group_tools = GroupTools()

    def make_home_menu(self):
        layout = [
            [sg.Column([[sg.Text('Welcome to the WhatsApp Web Scraping Tool', font=['Comic', 30, 'bold'], text_color='#ffffff', background_color='#2e9688')]], background_color='#2e9688')],
            [sg.Column([[sg.Text('Please Choose One Of The Following Options!', font=['Comic', 20, 'bold'], text_color='#000000', background_color='#d8dbd4')]], background_color='#d8dbd4', justification='center', pad=(50, 50))],
            [sg.Column([[sg.Button('Join Group'),
                         sg.Button('Join Multiple Groups'),
                         sg.Button('Print Groups'),
                         sg.Button('Quit')]], background_color='#d8dbd4', justification='center')]]
        return sg.Window('Window Title', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])

    def make_print_groups_screen(self):
        group_list = self.group_tools.get_group_list()
        group_text = ""
        for group in group_list:
            group_text += (group + "\n")
        layout = [
            [sg.Column([[sg.Text('Your Joined Group List', font=['Comic', 20, 'bold'], text_color='#ffffff', background_color='#2e9688')]], background_color='#2e9688')],
            [sg.Column([[sg.Multiline(default_text=group_text, auto_size_text=True, size=(20, 30))]])],
            [sg.Column([[sg.Button('Return')]], background_color='#d8dbd4', justification='center')]]
        return sg.Window('Printed Groups', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])
