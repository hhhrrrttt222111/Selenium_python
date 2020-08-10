# SElenium Web Scraper to Scrape the names of all Questions in Codechef

from selenium import webdriver
from bs4 import BeautifulSoup
import time

def codechef():
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get('https://www.codechef.com/problems/school/')


    names_beginner =[]
    names_easy =[]
    names_medium =[]
    names_hard =[]


    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.findAll('div', attrs={'class': 'problemname'}):
        name = a.find('b')
        names_beginner.append(name.text)

    print('\n \n BEGINNER \n')
    print(*names_beginner, sep='\n')

    time.sleep(3)

    driver.get('https://www.codechef.com/problems/easy/')

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.findAll('div', attrs={'class': 'problemname'}):
        name = a.find('b')
        names_easy.append(name.text)

    print('\n \n EASY \n')
    print(*names_easy, sep='\n')

    time.sleep(3)

    driver.get('https://www.codechef.com/problems/medium/')

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.findAll('div', attrs={'class': 'problemname'}):
        name = a.find('b')
        names_medium.append(name.text)

    print('\n \n MEDIUM \n')
    print(*names_medium, sep='\n')

    time.sleep(3)

    driver.get('https://www.codechef.com/problems/hard/')

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.findAll('div', attrs={'class': 'problemname'}):
        name = a.find('b')
        names_hard.append(name.text)

    print('\n \n HARD \n')
    print(*names_hard, sep='\n')

    time.sleep(3)

    driver.close()