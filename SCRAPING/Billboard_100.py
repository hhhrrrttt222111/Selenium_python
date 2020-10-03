# import necessary modules
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def billboard():
    # Set the location of your Webdriver
    # driver = webdriver.Firefox()  // For firefox
    driver = webdriver.Chrome('../drivers/chromedriver.exe')

    # Set URL
    driver.get('https://www.billboard.com/charts/hot-100')

    songs = []
    artists = []

    # Scrape content
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.findAll('li', attrs={'class': 'chart-list__element'}):
        song = a.find('span', 'chart-element__information__song')
        artist = a.find('span', 'chart-element__information__artist')
        songs.append(song.text)
        artists.append(artist.text)

    time.sleep(10)
    driver.close()

    # convert to dictionary
    tracks = dict(zip(songs, artists))

    # Print dictionary line by line
    for key, value in tracks.items():
        print(key, ' - ', value)


