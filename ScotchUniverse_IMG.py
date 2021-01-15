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

def download(url, name):
    print('Processing {0} url:{1}'.format(name,url))
    img = open('ScotchUniverse\{}'.format(name),'wb')
    respone = requests.get(url, stream=True).content
    img.write(respone)
    img.close()

if __name__ == "__main__":
    list = get_link()
    list2 = []
    for j in list:
        if '-300x300' in j:
            k = j.replace('-300x300', '')
            list2.append(k)
    for k in list2:
        name = k.split('/')[-1]
        download(k, name)