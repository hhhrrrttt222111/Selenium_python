from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def twitter_login():
    username = input('Enter Your Username : ')
    password = input('Enter Your Password : ')


    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get('https://twitter.com/login')


    input_name = driver.find_element_by_name('session[username_or_email]')
    input_name.send_keys(username)
    input_pass = driver.find_element_by_name('session[password]')
    input_pass.send_keys(password)
    btn = driver.find_element_by_class_name('css-18t94o4')
    btn.click()





