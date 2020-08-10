from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

def wikipedia():
    input_search = input('Search Wikipedia : ')

    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get("https://www.wikipedia.org/")

    search = driver.find_element_by_name('search')
    search.send_keys(input_search)
    search.send_keys(Keys.ENTER)

    time.sleep(5)

    url = driver.current_url

    res = requests.get(url)
    res.raise_for_status()

    wiki = BeautifulSoup(res.text, 'html.parser')

    for i in wiki.select('p'):
        print(i.getText(), end='')
