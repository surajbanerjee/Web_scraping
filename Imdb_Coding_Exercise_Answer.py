from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


#Starts our driver and goes to the starting webpage which is google.com
driver = webdriver.Chrome(
    'C:/Web Scraping course/chromedriver.exe'
)

driver.get('https://google.com')

#Inputs text into the google search box
input_box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
input_box.send_keys('top 100 greatest movies of all time imdb')

#Presses the enter button to search
input_box.send_keys(Keys.ENTER)
time.sleep(2)

#Presses on the link for Imdb
press = driver.find_element_by_xpath('//*[@id="rso"]/div[2]/div/div[1]/a/h3').click()

#3 second wait time to let the entire page load in
time.sleep(3)

#Scrolls until Jaws the movie is on the screen
driver.execute_script('window.scrollTo(0,22500)')

#Takes a screenshot of the webpage
driver.save_screenshot('C:\Web Scraping course\jaws.png')

#Takes a screenshot of the Jaws movie poster
driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[3]/div[50]/div[1]/a/img').screenshot('C:\Web Scraping course\jaws2.png')

# My own code start from here:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('D:\PYTHONisHERE\Anaconda_setup\chromedriver_win32\chromedriver.exe')
driver.get('https://www.google.com/?gws_rd=ssl')
box = driver.find_elements(By.XPATH ,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box
box[0].send_keys('Top 100 movie of all time')
box[0].send_keys(Keys.ENTER)
button = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/div/a/div/div/div/cite')
time.sleep(3)
button.click()
    
driver.find_element(By.XPATH, '//*[@id="main"]/div/div[4]/div[3]/div[50]/div[1]/a/img').screenshot('D:\Jaws.png')

