#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[31]:


# Connect to Website and pull in data

URL = 'https://www.amazon.in/dp/B0BGNQY58Y/ref=QAHzEditorial_en_IN_1?pf_rd_r=GEJA1AAR6PY3H9F27CG2&pf_rd_p=da092b0d-e8ad-4ffd-8bb9-d9ed23183f39&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-7&pf_rd_t=&pf_rd_i=2563504031&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

Ratings = soup2.find(id='acrPopover').get_text()

Price = soup2.find(class_='a-price-whole').get_text()




print(title)
print(Ratings)
print(Price)


# In[11]:


Ratings = Ratings.strip()[0:]
Price = Price.strip()[0:]
title = title.strip()
print(title)
print(Ratings)
print(Price)


# In[12]:


# Create a Timestamp for your output to track when data was collected

import datetime

today = datetime.date.today()

print(today)


# In[15]:


# Create CSV and write headers and data into the file

import csv 

header = ['Title', 'Ratings', 'Date' , 'Price']
data = [title, Ratings, today, Price]


with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[16]:


import pandas as pd

df = pd.read_csv(r'C:\Users\HP\AppData\Local\Programs\Python\Python39\Scripts\AmazonWebScraperDataset.csv')

print(df)


# In[17]:


#Now we are appending data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[18]:


def check_price():
    URL = 'https://www.amazon.in/dp/B0BGNQY58Y/ref=QAHzEditorial_en_IN_1?pf_rd_r=GEJA1AAR6PY3H9F27CG2&pf_rd_p=da092b0d-e8ad-4ffd-8bb9-d9ed23183f39&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-7&pf_rd_t=&pf_rd_i=2563504031&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    Ratings = soup2.find(id='acrPopover').get_text()
    
    Price = soup2.find(class_='a-price-whole').get_text()

    Ratings = price.strip()[0:]
    Price = Price.strip()[0:]
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Ratings', 'Date' , 'Price']
    data = [title, Ratings, today, Price]


    with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
 


# In[29]:


# Runs check_price after a set time and inputs data into your CSV
def check_price(Price):
    
    while(True):
        check_price(Price)
        time.sleep(60)


# In[21]:


import pandas as pd

df = pd.read_csv(r'C:\Users\HP\AppData\Local\Programs\Python\Python39\Scripts\AmazonWebScraperDataset.csv')

print(df)


# In[30]:


# If uou want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it
# out with this script

def send_mail():
    # Connect to the Gmail SMTP server using SSL
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    # Login to the Gmail account
    server.login('surajbanerjee100@gmail.com','8141066949')
    
    subject = "Casio G-Shock Analog-Digital Black Dial Men's Watch! is below the price tag right now!!"
    body = "Suraj, This is the moment we have been waiting for. Now is your chance to pick up the watch of your dreams. Don't mess it up! Link here: https://www.amazon.in/dp/B0BGNQY58Y/ref=QAHzEditorial_en_IN_1?pf_rd_r=GEJA1AAR6PY3H9F27CG2&pf_rd_p=da092b0d-e8ad-4ffd-8bb9-d9ed23183f39&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-7&pf_rd_t=&pf_rd_i=2563504031&th=1"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'surajbanerjee100@gmail.com',
        msg
     
    )
    print("Email sent!")
    # Close the server connection
    server.close()


# In[ ]:




