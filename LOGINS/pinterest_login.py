from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def pinterest_login(d):
    username = input('Enter Your Username : ')
    password = input('Enter Your Password : ')

    driver = webdriver.Chrome(d)
    driver.get('https://in.pinterest.com/')

    login = driver.find_element_by_class_name('Jrn')
    login.click()
    input_email = driver.find_element_by_name('id')
    input_email.send_keys(username)
    input_pass = driver.find_element_by_name('password')
    input_pass.send_keys(password)
    btn = driver.find_element_by_class_name('red')
    btn.click()





