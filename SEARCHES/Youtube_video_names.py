from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


def youtube():
    input_search = input('Enter Youtube Search : ')

    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get('https://www.youtube.com/')

    titles = []
    description = []

    search = driver.find_element_by_name('search_query')
    search.send_keys(input_search, Keys.ENTER)

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.findAll('a', attrs={'id': 'video-title'}):
        name = a.find('yt-formatted-string', attrs={'class': 'style-scope ytd-video-renderer'})
        titles.append(name.text)

    for a in soup.findAll('div', attrs={'id': 'dismissable'}):
        desc = a.find('yt-formatted-string', attrs={'id': 'description-text'})
        description.append(desc.text)

    print(*titles, sep='\n')
    print('\n\n\n')
    print(*description, sep='\n')

    time.sleep(10)
    driver.close()