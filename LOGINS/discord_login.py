from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def discord_login():
    username = input('Enter Your Username : ')
    password = input('Enter Your Password : ')
    driver = webdriver.Chrome()

    driver.get('https://discord.com/login')
    wait = WebDriverWait(driver, 30)
    time.sleep(2)

    try:
        tb = driver.find_elements_by_tag_name("input")
        tb[0].send_keys(username)
        tb[1].send_keys(password)
        tb[1].submit()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME,"closeIcon-150W3V"))).click()

    except NoSuchElementException:
            driver.find_element_by_link_text("Open").click() 
    
    return driver,wait




