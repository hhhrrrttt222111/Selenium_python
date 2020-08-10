from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def fb_signup():
    input_first = input('Enter Firstname : ')
    input_last = input('Enter Lastname : ')
    input_num = input('Enter Phone Number : ')
    input_pass = input('Enter Password : ')
    input_day = input('Enter Day of Birth: ')
    input_month = input('Enter Month of Birth as number : ')
    input_year = input('Enter Year of Birth : ')
    input_gender = input('Select Gender : Male(1), Female(2), Custom(-1) : ')

    browser = webdriver.Chrome('../drivers/chromedriver.exe')
    browser.get("http://www.facebook.com")


    first = browser.find_element_by_name('firstname')
    first.send_keys(input_first)

    last = browser.find_element_by_name('lastname')
    last.send_keys(input_last)

    num = browser.find_element_by_name('reg_email__')
    num.send_keys(input_num)

    password = browser.find_element_by_name('reg_passwd__')
    password.send_keys(input_pass)

    day = Select(browser.find_element_by_id('day'))
    day.select_by_visible_text(input_day)

    month = Select(browser.find_element_by_id('month'))
    month.select_by_value(input_month)

    year = Select(browser.find_element_by_id('year'))
    year.select_by_visible_text(input_year)

    gender = browser.find_element_by_css_selector(f"input[type='radio'][value='{input_gender}']").click()

    button = browser.find_element_by_name('websubmit')
    button.click()
    time.sleep(15)
    browser.close()

