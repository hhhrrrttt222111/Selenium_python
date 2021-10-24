from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def instagram_login():
    username = input('Enter Your Username : ')
    password = input('Enter Your Password : ')

    driver = webdriver.Chrome() #Set path to web driver
    driver.get('https://www.instagram.com/?hl=en')
    wait = WebDriverWait(driver, 10)#driver, upper limit
    login = wait.until(ec.presence_of_element_located((By.XPATH,"//*[@id='loginForm']/div/div[3]")))
    login.click()
    userfield = wait.until(ec.presence_of_element_located((By.XPATH,"//input[@aria-label = 'Phone number, username, or email']")))
    passfield = wait.until(ec.presence_of_element_located((By.XPATH,"//input[@name = 'password']")))

    userfield.send_keys(username)
    passfield.send_keys(password)

    btn = driver.find_element_by_tag_name('button')
    btn.submit()
    for _ in range(2):
        time.sleep(3)
        try:
            driver.find_element_by_xpath("//*[contains(text(), 'Not Now')]").click() 
        except NoSuchElementException:
            pass




