from bs4 import BeautifulSoup
from datetime import datetime
import os
import re
import pandas as pd
from scrape.system_tools import SystemTools


class WhatsAppHtmlParser:

    def __init__(self, html_file_path):
        with open(html_file_path, 'r') as f:
            contents = f.read()
        self.soup = BeautifulSoup(contents, 'html.parser')

    def get_messages_pd_frame(self):
        df = pd.DataFrame(columns=['Datetime', 'Author', 'Message'])
        for tag in self.soup.find_all('div'):
            currentDict = tag.attrs
            if "class" in currentDict:
                if self.__search(currentDict, 'copyable-text'):
                    if (len(currentDict) <= 2):
                        theFinalDict = currentDict
                        dateNameString = theFinalDict["data-pre-plain-text"]
                        timestamp = self.__find_between(dateNameString, "[", "]")
                        datetime_object = datetime.strptime(timestamp, '%I:%M %p, %m/%d/%Y')
                        msgAuthor = self.__find_between(dateNameString, "] ", ":")
                        df = df.append({'Datetime': datetime_object, 'Author': msgAuthor, 'Message': tag.text}, ignore_index=True)
        df = df.set_index('Datetime')
        return df

    def save_pd_frame_to_pickle(self, df, file_name, dest_folder):
        df.to_pickle(dest_folder + "/" + file_name + ".pkl")

    def save_pd_frame_to_csv(self, df, file_name, dest_folder):
        df.to_csv(dest_folder + '/' + file_name + '.csv')

    def __find_between(self, s, first, last):
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]

    def __search(self, values, searchFor):
        for k in values:
            for v in values[k]:
                if searchFor in v:
                    return k
        return None


class MultiProcessHtml:
    sys_tools = SystemTools()

    def process_all_raw_html_to_pickles(self, raw_html_list=sys_tools.get_raw_html_list(), html_pickle_dir=sys_tools.get_processed_html_pickles_dir(), html_dir_path=sys_tools.get_html_dir_path()):
        if not os.path.isdir(html_pickle_dir):
            os.mkdir(html_pickle_dir)
        else:
            for root, dirs, files in os.walk(html_pickle_dir):
                for file in files:
                    os.remove(os.path.join(root, file))
        if raw_html_list != []:
            for html_file in raw_html_list:
                html_parser = WhatsAppHtmlParser(html_dir_path + '/' + html_file)
                df = html_parser.get_messages_pd_frame()
                html_parser.save_pd_frame_to_pickle(df, html_file, html_pickle_dir)
        else:
            raise Exception("There are no files to process in " + html_dir_path)
