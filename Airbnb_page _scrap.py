# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 14:05:11 2023

@author: HP
"""
import requests 
    #The requests library is imported to send a GET request to the specified URL, which returns the HTML content of the page.
from bs4 import BeautifulSoup
    #The BeautifulSoup library is imported to parse the HTML content and extract the desired information.
import pandas as pd
    #The pandas library is imported to store the extracted information in a dataframe.

url='https://www.airbnb.co.in/s/Hyderabad--Telangana/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=2&date_picker_type=calendar&checkin=2023-02-14&checkout=2023-02-16&source=structured_search_input_header&search_type=user_map_move&query=Hyderabad%2C%20Telangana&place_id=ChIJx9Lr6tqZyzsRwvu6koO3k64&ne_lat=17.48235783903782&ne_lng=78.45147263800379&sw_lat=17.382453793437378&sw_lng=78.35909950739358&zoom=13&search_by_map=true'
page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
soup

df = pd.DataFrame({'link':[''], 'title':[''], 'price':[''], 'rateing':[''], 'detail':[''],'bed':['']})
    #An empty pandas dataframe df is created with columns for link, title, price, rating, detail, and bed.

while True:
#An infinite loop while True is started to scrape information from multiple pages. 
#The loop is broken using the break statement at the end of the loop.
    post = soup.find_all('div', class_ = 'cy5jw6o  dir dir-ltr')
    for pose in post:
        link = post.find('a', class_ = 'bn2bl2p dir dir-ltr').get('href')
        link_full = 'https://www.airbnb.co.in' + link
        title = post.find('div', class_ = 't1jojoys dir dir-ltr').text
        price = post.find('span', class_ = '_1y74zjx').text
        rateing = post.find('span', class_ = 'r1dxllyb dir dir-ltr').text
        detail = post.find('span', class_ = 't6mzqp7 dir dir-ltr').text
        bed = post.find('span', class_ = ' dir dir-ltr').text
        df = df.append({'link':link, 'title':title, 'price':price, 'rateing':rateing, 
                        'detail':detail,'bed':bed}, ignore_index= True)
        #The extracted information is then appended to the dataframe df using the append method.
        break
        

detail = soup.find('span', class_ = 't6mzqp7 dir dir-ltr')
detail.text

next_page = soup.find('a', {'aria-label':'Next'}).get('href')
next_page
next_page_full = 'https://www.airbnb.co.in' + next_page
next_page_full


df.to_csv('D:\PYTHONisHERE\Anaconda_setup')
#The dataframe df is saved to a CSV file located at 'D:\PYTHONisHERE\Anaconda_setup'.