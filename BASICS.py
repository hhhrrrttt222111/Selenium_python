from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path=r"D:\Softwares\chromedriver_win32\chromedriver.exe")

browser.get('http://hhhrrrttt222111.me/')



print(browser.title)
print(browser.current_url)
print(browser.current_window_handle)

time.sleep(5)
browser.get('https://hhhrrrttt222111.github.io/PyBox/')
time.sleep(3)
browser.back()
time.sleep(3)
browser.forward()

time.sleep(10)
browser.close()