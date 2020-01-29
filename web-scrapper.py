import requests
from bs4 import BeautifulSoup

def books_data():
  url = 'http://lectura-audio.blogspot.com/'

  while url:
    print(str(url).encode("utf8"))
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('h3', class_='post-title entry-title')
    print(str(results).encode("utf8"))

    # find next url
    url_element = soup.find(id='Blog1_blog-pager-older-link')

    if url_element:
      url = url_element['href']
    else:
      break


books_data()
