from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def flipkart():
    input_search = input('Enter Search  : ')

    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get("https://www.flipkart.com/")

    search = driver.find_element_by_name('q')
    search.send_keys(input_search, Keys.ENTER)

    print(driver.get_cookies())
