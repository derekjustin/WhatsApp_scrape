#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A test of beautiful soup 
"""

from bs4 import BeautifulSoup
from datetime import datetime
import re
import pandas as pd

class WhatsAppHtmlParser:

    def __init__(self, html_file_name):
        with open("/home/garage/Desktop/WhatsApp_scrape/scrape/group_files/raw_html_files/" + html_file_name , 'r') as f:
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
            
tester = WhatsAppHtmlParser("20210222+92 306 5249518")        
theThing = tester.get_messages_pd_frame()
message = tester.find_full_message_with_string( "How" )     
tester.print_html()
tester.save_pd_frame_to_pickle( theThing, "DerekRulz", "/home/garage/Desktop" )
someFrame = tester.read_pickle_to_frame("/home/garage/Desktop/DerekRulz.pkl")
tester.save_pd_frame_to_csv( theThing, "DerekRulz", "/home/garage/Desktop" )
someOtherFrame = tester.read_csv_to_frame("/home/garage/Desktop/DerekRulz.csv")

