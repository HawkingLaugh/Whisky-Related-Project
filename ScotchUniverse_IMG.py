import requests
from bs4 import BeautifulSoup as soup

def get_link():
    url = 'https://www.scotch-universe.co.uk/actual-and-recent-bottlings/'
    r = requests.get(url)
    content = r.content
    page = soup(content,'lxml')
    images = page.find_all('img')
    image_list = []
    for image in images:
        image_list.append(image.attrs['src'])
    return image_list

def download(url):
    global filenum
    print('Processing {0} url:{1}'.format(filenum,url))
    img = open('{}.png'.format(filenum),'wb')
    respone = requests.get(url, stream=True).content
    img.write(respone)
    filenum += 1
    img.close()

if __name__ == "__main__":
    list = get_link()
    filenum = 1
    for i in list:
        download(i)