from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


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
first.send_keys('Hemanth')

last = browser.find_element_by_name('lastname')
last.send_keys('Raj')

num = browser.find_element_by_name('reg_email__')
num.send_keys('0000000000')

password = browser.find_element_by_name('reg_passwd__')
password.send_keys('hrt21213')

day = Select(browser.find_element_by_id('day'))
day.select_by_visible_text('21')

month = Select(browser.find_element_by_id('month'))
month.select_by_value('1')

year = Select(browser.find_element_by_id('year'))
year.select_by_visible_text('2001')

gender = browser.find_element_by_css_selector("input[type='radio'][value='2']").click()

button = browser.find_element_by_name('websubmit')
button.click()
time.sleep(15)
browser.close()

