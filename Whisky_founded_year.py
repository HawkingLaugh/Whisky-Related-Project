import requests
from bs4 import BeautifulSoup as soup

url = open('WDList.html', 'r', encoding='utf-8')
output = open('output.txt', 'w+')
page = soup(url,'lxml')
target = soup.find(page, class_="wikitable").find_all('a')[1:]
for i in target:
    if 'redlink' not in i.attrs['href']:
        try:
            output.write(i.attrs['title'])
            output.write(' ')
            output.write(i.attrs['href'])
            output.write('\n')
        except :
            output.write(i.attrs['href'])
            output.write('\n')
            continue