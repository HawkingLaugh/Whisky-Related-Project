from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'
# for browser option settings
chromeOptions = Options()
chromeOptions.add_argument("--disable-popup-blocking")
chromeOptions.add_argument("--lang=en")
driver = webdriver.Chrome(PATH,chrome_options=chromeOptions)


try:
    f = open('whisky_name1.txt', 'r+')
except:
    f = open('whisky_name1.txt', 'w+')

def brandToSearch(name):
    name = input("Enter Whisky Brand: ")
    return name

def getAllNames(list):
    names = driver.find_elements_by_class_name("name")
    for name in names:
        nameList.append(name.text)
    for name in nameList:
        # f.write(name)
        if '\n' in name:
            location = name.index('\n')
            f.write(name[0:location] + " : " + name[location + 1:])
            f.write('\n')
        else:
            f.write(name)
            f.write('\n')

def findElements():
    while True:
        try:
            getAllNames(nameList)
            link = driver.find_element_by_xpath("//*[text()='Next']")
            driver.execute_script("arguments[0].click();", link)
            time.sleep(2)
        except :
            f.close()
            break

if __name__ == "__main__":
    nameList = []
    driver.get('https://www.thewhiskyexchange.com/')
    print(driver.title)
    search = driver.find_element_by_id("txtSearchInput")
    search.send_keys(brandToSearch())
    search.send_keys(Keys.RETURN)