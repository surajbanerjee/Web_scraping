### Overview

This ReadMe is used for learning web scraping and some basic commands with explanations and basic code, we can refer to this link for basic commands <a href="https://selenium-python.readthedocs.io/"> `Here` </a>
This Readme contains complete a course of Web Scraping in Python With BeautifulSoup and Selenium 2023 on Udemy 

#### Motive of Building this:
A idea for a project that combines Python and SQL would be to create a web scraping script using Python that collects data from a website and then stores that data in a SQL database. The script could then be scheduled to run regularly to collect updated information.
Once the data is stored in the SQL database, you could use Python to perform analysis on the data and create visualizations using a library such as Matplotlib or Seaborn. Additionally, you could use a web framework like Flask or Django to create a web application that allows users to interact with the data and visualizations stored in the SQL database.
This project would demonstrate your ability to work with both Python and SQL, as well as your understanding of web scraping, data analysis, and web development.

> Basic commands used:

You can find the basic commands <a href="https://github.com/surajbanerjee/Web_scraping/blob/8b445fc1822b3a20d255f7c73af126881fe14c0f/Amazon%20Web%20Scraping%20project.py"> `Here` </a> And for more Updated below.

> Project

#### Scraping_Table_Project

Scraping data form a table, <a href="https://github.com/surajbanerjee/Web_scraping/blob/4b9b0209487db0fe35067fa535f1187966f36349/Scraping_a_Table.py"> `⛓Code` </a> with explanition below:

Python Library used:
```
import requests
from bs4 import BeautifulSoup
import pandas as pd
```
The URL of the website from where we want to scrape the data. A GET request to the specified URL and retrieves the response. a GET request to the specified URL and saves the response in a variable named `page`. creates a BeautifulSoup object soup from the HTML content of the response received in page. The `lxml` argument specifies the parser to be used to parse the HTML content.
```
url = 'https://www.worldometers.info/world-population/'
requests.get(url)
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
```
Searches for the first `<table>` element in the HTML content that has the `class` `table table-striped table-bordered table-hover table-condensed table-list` and saves the result in a variable named `table`. To find the specific table on the page that contains the data we are interested in. initializes an empty `list` `headers` to store the column headers of the table. starts a for loop to iterate over all the `<th>` elements in the table variable. `<th>` elements represent table headers in HTML [ In the for loop for `i` in `table.find_all('th'):`, `i` is a temporary variable that represents each `<th>` element in the `table.find_all('th')` result. The loop iterates over all the `<th>` elements and each iteration `i` takes on the value of the next `<th>` element in the result. ]. Extracts the text content of the current `<th>` element and saves it in a variable named `title`. The `strip()` method is used to remove any extra whitespace from the beginning and end of the text. Then adds the `title` variable to the end of the `headers` list.
```
table = soup.find('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list')
headers = []
for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)
```
a new `pandas` DataFrame `df` with the specified `column` names.
The `pd.DataFrame` function creates a new dataframe and takes an argument `columns` that specifies the names of the columns in the dataframe. In this `line`, the value of columns is the `headers` `list`, which we obtained in the previous code.
So, `df = pd.DataFrame(columns = headers)` creates a new `empty` dataframe `df` with the columns specified in the `headers` `list`. The dataframe is `empty` because we have not yet added any data to it. This line sets up the structure of the dataframe and makes sure that it has the correct `columns`.
```
df = pd.DataFrame(columns = headers)
```
starts a for loop to iterate over all the `<tr>` elements in the `table.find_all('tr')` result. `<tr>` elements represent table rows in HTML. The `[1:]` slice notation is used to exclude the first row of the table, which is assumed to be the header row. Then searches for all the `<td>` elements within the current `<tr>` element `j` and saves the result in a variable named `row_data`. `<td>` elements represent table cells in `HTML`. Creates a list row that contains the text content of each `<td>` element in the `row_data` variable. The `[tr.text for tr in row_data]` syntax is a list comprehension that iterates over each `<td>` element in `row_data`, extracts the text content of each `<td>` element, and creates a new list row with the text content. Calculates the number of rows in the dataframe `df` using the `len()` function and saves the result in a variable named length. Adds the values in the row list to the dataframe `df` as a new row at the specified index `length`. The `df.loc[]` syntax is used to specify the index label of the row in the dataframe to be modified.
`At the end of the loop, the dataframe df should contain all the data from the table, excluding the header row.`
```
for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [tr.text for tr in row_data]
    length = len(df)
    df.loc[length] = row
```
This code writes the contents of the `pandas` `DataFrame` object named "df" to a `comma-separated values` `(CSV)` file at the specified `file path` `('A/File/Path/file_name.csv')`. The file will contain the data in the DataFrame, with each row representing a record and each `column` representing an attribute of that `record`.
```
df.to_csv('A/File/Path/file_name.csv')
```
> Second_project

#### Dealing with multiple web_pages

Here we are Scraping <a href="https://github.com/surajbanerjee/Web_scraping/blob/71c864c2039724920ade0a1a3870d4e7cfc3c3b3/Airbnb_page%20_scrap.py"> `Airbnb` </a> to get multiple pages data and anlysis the deals. Scraping data from multiple links [ All the code is done in Spider {Python-ide} ].

#### Imdb Scrap_page

Scraped Imdb for the top 100 movie till now, Find the code <a href ="https://github.com/surajbanerjee/Web_scraping/blob/e62553c6ec0fa61c307ef37739131f23b7c9f107/Imdb_Coding_Exercise_Answer.py"> `here` </a>.
1. Starts our driver and goes to the starting webpage which is google.com
2. Inputs text into the google search box
3. Presses the enter button to search
4. Presses on the link for Imdb
5. 3 second wait time to let the entire page load in
6. Scrolls until Jaws the movie is on the screen
7. Takes a screenshot of the webpage
8. Takes a screenshot of the Jaws movie poster
9. My own code start from here:

#### Infinite Scrolling

Here we learn about the scrolling the web page through automation so we can get the whole page data as per the dataframe. We have the <a href = https://github.com/surajbanerjee/Web_scraping/blob/b9bf0f5614691065b7be9e3720b9c7242160f314/Infinite_Scrolling.py> `Code` </a> here.

> Third_Project

Here we have scraped `Twitter` and scraped 200 twete to analys the most recent tweet, we had login with the help of python script and searched for one of my favourite  celebreaty and tried to get the most recent list of tweets.
My <a href = 'https://github.com/surajbanerjee/Web_scraping/blob/8b99730008e949375d4913720f5f3949f4718ed2/Twitter.py'> `Code` </a> is here 

As well we have done one more famous website, where we have scraped `Indeed` to get the most recent job listings. find the code <a href = 'https://github.com/surajbanerjee/Web_scraping/blob/8b99730008e949375d4913720f5f3949f4718ed2/Indeed_Coding_Exercise_Answer.py'> `here` </a>.
