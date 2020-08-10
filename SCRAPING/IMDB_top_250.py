# import necessary modules
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def imdb():
    # Set the location of your Webdriver
    # driver = webdriver.Firefox()  // For firefox
    driver = webdriver.Chrome('../drivers/chromedriver.exe')

    # Set URL
    driver.get('https://www.imdb.com/chart/top/')

    movies = []
    rating = []

    # Scrape content
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.findAll('td', attrs={'class': 'titleColumn'}):
        movie = a.find('a')
        movies.append(movie.text)

    for a in soup.findAll('td', attrs={'class': 'imdbRating'}):
        rate = a.find('strong')
        rating.append(rate.text)

    time.sleep(10)
    driver.close()

    imdb = dict(zip(movies, rating))

    for key, value in imdb.items():
        print(key, ' : ', value)
