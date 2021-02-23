from bs4 import BeautifulSoup
from datetime import datetime
import re
import pandas as pd
import os

from scrape.system_tools import SystemTools

class WhatsAppHtmlParser:

    def __init__(self, html_file_name):
        self.sys_tools = SystemTools()
       # print (self.sys_tools.get_html_dir_path + '/' + html_file_name)
        with open(self.sys_tools.get_html_dir_path() + '/' + html_file_name , 'r') as f:
            contents = f.read()
        self.soup = BeautifulSoup(contents, 'html.parser')
        
    def get_messages_pd_frame( self ):       
        df = pd.DataFrame(columns=['Datetime' , 'Author', 'Message'])
        for tag in self.soup.find_all('div'):
            currentDict = tag.attrs
            if "class" in currentDict:
                if self.__search(currentDict, 'copyable-text'):
                    if (len(currentDict) <= 2):
                        theFinalDict = currentDict
                        dateNameString = theFinalDict["data-pre-plain-text"]
                        timestamp = self.__find_between( dateNameString , "[", "]" )
                        datetime_object = datetime.strptime(timestamp, '%I:%M %p, %m/%d/%Y')
                        msgAuthor = self.__find_between( dateNameString , "] ", ":" )
                        df = df.append( {'Datetime' : datetime_object ,'Author' : msgAuthor  , 'Message' : tag.text }, ignore_index = True)
        df = df.set_index('Datetime')    
        return df  
    




    def save_pd_frame_to_pickle(self, df, file_name, dest_folder ):
        df.to_pickle( dest_folder + "/" + file_name + ".pkl")
    
    def save_pd_frame_to_csv(self, df, file_name, dest_folder):
        df.to_csv( dest_folder + '/'+ file_name + '.csv') 
        
    def read_pickle_to_frame(self, file_path ):
        return pd.read_pickle(file_path)
    
    def read_csv_to_frame(self, file_path):
        df = pd.read_csv(file_path) 
        return df.set_index('Datetime')
    
    def find_full_message_with_string(self, instance_of ):         
        return self.soup.find(string=re.compile(instance_of)) 
    
    def print_html(self):
        print(self.soup.prettify())
            
    def __find_between(self, s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""    
    
    def __search(self, values, searchFor):
        for k in values:
            for v in values[k]:
                if searchFor in v:
                    return k
        return None        


class MultiProcessHtml:

    def __init__(self):
        self.sys_tools = SystemTools()
        self.raw_html_list = self.sys_tools.get_raw_html_list()
        print(self.raw_html_list)
        for html_file in self.raw_html_list:
            print(type(html_file))
        self.html_list = self.sys_tools.get_raw_html_list()
        self.html_pickle_dir = self.sys_tools.get_processed_html_pickles_dir()


    def process_all_raw_html_to_pickles(self):
   #     sys_tools = SystemTools()
   #     raw_html_list = sys_tools.get_raw_html_list()
        self.sys_tools.clean_processed_pickle_dir()

        for html_file in self.raw_html_list:
            html_parser = WhatsAppHtmlParser(html_file)
            df = html_parser.get_messages_pd_frame()
            html_parser.save_pd_frame_to_pickle(df, html_file, self.html_pickle_dir )
    
#    def clean_processed_pickle_dir(self):        
#        if not os.path.isdir(self.html_pickle_dir):
#            os.mkdir(self.sys_tools.get_processed_html_pickles_dir)
#        else:
#            sys_tools.delete_all_files_in_dir(self.html_pickle_dir)

#tester = WhatsAppHtmlParser("20210222+92 306 5249518")        
#theThing = tester.get_messages_pd_frame()
#message = tester.find_full_message_with_string( "How" )     
#tester.print_html()
#tester.save_pd_frame_to_pickle( theThing, "DerekRulz", "/home/garage/Desktop" )
#someFrame = tester.read_pickle_to_frame("/home/garage/Desktop/DerekRulz.pkl")
#tester.save_pd_frame_to_csv( theThing, "DerekRulz", "/home/garage/Desktop" )
#someOtherFrame = tester.read_csv_to_frame("/home/garage/Desktop/DerekRulz.csv")
stuff = MultiProcessHtml()
#test = WhatsAppHtmlParser('2021022219:26:32_Testing')
stuff.process_all_raw_html_to_pickles()
