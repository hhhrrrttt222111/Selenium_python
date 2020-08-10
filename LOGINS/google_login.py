from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def google_login():
    username = input('Enter Your Email : ')
    password = input('Enter Your Password : ')


    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get('https://accounts.google.com/')

    input_email = driver.find_element_by_name('identifier')
    input_email.send_keys(username)
    input_email.send_keys(Keys.ENTER)
    input_pass = driver.find_element_by_name('password')
    input_pass.send_keys(password)
    input_pass.send_keys(Keys.ENTER)





