from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def spotify_login():
    username = input('Enter Your Username : ')
    password = input('Enter Your Password : ')


    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get('https://accounts.spotify.com/en/login')


    input_email = driver.find_element_by_name('username')
    input_email.send_keys(username)
    input_pass = driver.find_element_by_name('password')
    input_pass.send_keys(password)
    btn = driver.find_element_by_class_name('btn-green')
    btn.click()





