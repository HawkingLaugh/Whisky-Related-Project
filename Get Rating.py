from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# name = input("Pass me a Link: ")
PATH = 'C:\Program Files (x86)\chromedriver.exe'
# for browser option settings
chromeOptions = Options()
chromeOptions.add_argument("--disable-popup-blocking")
chromeOptions.add_argument("--lang=en")
chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(PATH,chrome_options=chromeOptions)

driver.get('https://www.whiskybase.com/whiskies/whisky/33372/glenfiddich-19-year-old')
rating = driver.find_elements_by_tag_name("span")
temp = []
f = open('rating.txt', 'w+')
for i in rating:
    temp.append(i.text)
print(temp)
for j in temp:
    if j.isnumeric():
        f.write(j)
        f.write('\n')
    else:
        continue
    