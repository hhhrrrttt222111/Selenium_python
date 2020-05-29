from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(executable_path=r"D:\Softwares\chromedriver_win32\chromedriver.exe")
driver.get("https://www.flipkart.com/")

search = driver.find_element_by_name('q')
search.send_keys('Mobiles', Keys.ENTER)

driver.close()