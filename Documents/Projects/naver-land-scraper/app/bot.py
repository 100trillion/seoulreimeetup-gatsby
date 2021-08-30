from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format','{:.2f}'.format)

sleep(5)

driver = webdriver.Chrome('/Users/Leese/Documents/Projects/naver-land-scraper/app/chromedriver')

driver.get('https://new.land.naver.com/houses?ms=37.563517,126.9084,15&a=VL:DDDGG:JWJT:SGJT:HOJT&b=A1&e=RETAIL&g=30000')


latest = driver.find_element_by_xpath("//*[@id='list']/div[2]/div/div[1]/div/a[2]")

# Order properties by upload date
latest = driver.find_element_by_xpath("//*[@id='list']/div[2]/div/div[1]/div/a[2]")

# Click the latest button so to upload properties by upload date
latest.click()

# Allow the page 5 seconds to load before grabbing the HTML.
sleep(5)

# Take a screenshot of the page
driver.save_screenshot('screenshot.png')

# Grab the HTML.
html = driver.page_source

# Parse the HTML.
soup = BeautifulSoup(html, "html.parser")

# Get the listings element
all_listings_element = soup.find("div", {"id": "listContents1"})

items = all_listings_element.find_all('div', {'class': 'item'})

listings = []
for i in items:
  item_title = soup.find("div", {"class": "item_title"}).text.strip()
  price_line = soup.find("div", {"class": "price_line"}).text.strip()
  info_area = soup.find("div", {"class": "info_area"}).text.strip()
  tag_area = soup.find("div", {"class": "tag_area"}).text.strip()
  label_area = soup.find("div", {"class": "label_area"}).text.strip()
  listings.append([item_title, price_line, info_area, tag_area, label_area])

df = pd.DataFrame(listings, columns=['Title', 'Price', 'Specs', 'Tags', 'Date posted'])
print(df)

driver.close()