from selenium import webdriver


def swiggy():
    input_mobile = input('Enter Mobile : ')
    input_name = input('Enter Name : ')
    input_email = input('Enter Email : ')
    input_pass = input('Enter Password : ')

    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get('https://www.swiggy.com/')

    signup = driver.find_element_by_class_name('r2iyh')
    signup.click()

    mobile = driver.find_element_by_id('mobile')
    mobile.send_keys(input_mobile)

    name = driver.find_element_by_id('name')
    name.send_keys(input_name)

    email = driver.find_element_by_id('email')
    email.send_keys(input_email)

    passwd = driver.find_element_by_id('password')
    passwd.send_keys(input_pass)

    btn = driver.find_element_by_class_name('_25qBi')
    btn.click()

