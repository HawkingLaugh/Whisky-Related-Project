from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

name = input("Enter Whisky Brand: ")
PATH = 'C:\Program Files (x86)\chromedriver.exe'
# for browser option settings
chromeOptions = Options()
chromeOptions.add_argument("--disable-popup-blocking")
chromeOptions.add_argument("--lang=en")
driver = webdriver.Chrome(PATH,chrome_options=chromeOptions)

try:
    f = open('{}.txt'.format(name), 'r+')
except:
    f = open('{}.txt'.format(name), 'w+')

# def brandToSearch():
#     name = input("Enter Whisky Brand: ")
#     return name

def getAllNames(list):
    names = driver.find_elements_by_class_name("name")
    for name in names:
        nameList.append(name.text)
    for name in nameList:
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

def connectToSite(brandName):
    driver.get('https://www.thewhiskyexchange.com/')
    search = driver.find_element_by_id("txtSearchInput")
    search.send_keys(brandName)
    search.send_keys(Keys.RETURN)

if __name__ == "__main__":
    nameList = []
    connectToSite(name)
    findElements()