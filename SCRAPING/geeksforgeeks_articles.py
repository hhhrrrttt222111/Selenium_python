from selenium import webdriver
from bs4 import BeautifulSoup
import time


def geeksforgeeks():
    url = 'https://www.geeksforgeeks.org/'
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get(url)

    titles = []

    for i in range(2,30):
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        for a in soup.findAll('h2', attrs={'class': 'entry-title'}):
            title = a.find('a')
            titles.append(title.text)

        print(*titles, sep='\n')

        # Go to next page
        time.sleep(2)
        driver.get(url + 'page/' + str(i) + '/')
        i = i + 1
