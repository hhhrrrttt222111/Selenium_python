from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


def fb_login():
    path1 = os.path.abspath(os.path.abspath('../drivers/chromedriver.exe'))
    path = path1.replace('\\','/')
    pt = "../drivers/chromedriver.exe"
    username = input('Enter Your Username : ')
    password = input('Enter Your Password : ')
    driver = webdriver.Chrome(executable_path=path1)
    driver.get('https://www.facebook.com/')

    input_name = driver.find_element_by_name('email')
    input_name.send_keys(username)
    input_pass = driver.find_element_by_name('pass')
    input_pass.send_keys(password)
    btn = driver.find_element_by_id('loginbutton')
    btn.click()
    # print(path)
    # print(pt)

