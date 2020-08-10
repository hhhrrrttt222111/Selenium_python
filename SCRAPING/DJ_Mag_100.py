from selenium import webdriver
from bs4 import BeautifulSoup
import time

def djmag():
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get('https://djmag.com/top100djs')


    artists = []

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.findAll('div', attrs={'class': 'top100dj-name'}):
        artist = a.find('a')
        artists.append(artist.text)

    print(*artists, sep='\n')
