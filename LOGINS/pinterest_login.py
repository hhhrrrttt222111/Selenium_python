from selenium import webdriver
from selenium.webdriver.common.keys import Keys


username = input('Enter Your Username : ')
password = input('Enter Your Password : ')


driver = webdriver.Chrome(executable_path=r"D:\Softwares\chromedriver_win32\chromedriver.exe")
driver.get('https://in.pinterest.com/')

login = driver.find_element_by_class_name('Jrn')
login.click()
input_email = driver.find_element_by_name('id')
input_email.send_keys(username)
input_pass = driver.find_element_by_name('password')
input_pass.send_keys(password)
btn = driver.find_element_by_class_name('red')
btn.click()





