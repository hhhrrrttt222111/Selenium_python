from selenium import webdriver
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome(executable_path=r"D:\Softwares\chromedriver_win32\chromedriver.exe")
driver.get('https://www.billboard.com/charts/hot-100')

songs = []
artists = []

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
for a in soup.findAll('li', attrs={'class': 'chart-list__element'}):
    song = a.find('span', 'chart-element__information__song')
    artist = a.find('span', 'chart-element__information__artist')
    songs.append(song.text)
    artists.append(artist.text)

# convert to dictionary
tracks = dict(zip(songs, artists))

# Print dictionary line by line
for key, value in tracks.items():
    print(key, ' - ', value)
