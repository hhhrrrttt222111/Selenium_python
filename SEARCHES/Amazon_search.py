from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def amazon():
    categories = '''
        All Categories
        Deals
        Amazon Fashion
        Amazon Pantry
        App & Games
        Baby
        Beauty
        Books
        Car & Motorbike
        Clothing & Accessories
        Collectibles
        Computers & Accessories
        Electronics
        Furniture
        Garden & Outdoors
        Gift Cards
        Grocery & Gourmet Foods
        Health & Personal Care
        Home & Kitchen
        Industrial & Scientific
        Jewellery
        Kindle Store
        Luggage & Bags
        Luxury Beauty
        Movies & TV Shows
        Music
        Musical Instruments
        Office Products
        Pet Supplies
        Prime Video
        Shoes & Handbags
        Software
        Sports, Fitness & Outdoors
        Tools & Home Improvement
        Toys & Games
        Under ₹500
        Video Games
        Watches'''
    print(categories)
    input_category = input('Search Category from Above : ')
    print()
    input_search = input(f'Search  {input_category} : ')

    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get("https://www.amazon.in/")


    category = Select(driver.find_element_by_id('searchDropdownBox'))
    category.select_by_visible_text(input_category)

    time.sleep(1)

    search = driver.find_element_by_id('twotabsearchtextbox')
    search.send_keys(input_search)
    search.send_keys(Keys.ENTER)

