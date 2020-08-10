from selenium import webdriver
from bs4 import BeautifulSoup


def covid():
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get('https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/')


    cases = []
    new_cases = []
    country = []

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.findAll('tr', attrs={'class': 'odd'}):
        cty = a.find('td')
        case = a.find('td', attrs={'class': 'sorting_1'})
        cases.append(case.text)
        country.append(cty.text)

    for a in soup.findAll('tr', attrs={'class': 'even'}):
        cty = a.find('td')
        case = a.find('td', attrs={'class': 'sorting_1'})
        cases.append(case.text)
        country.append(cty.text)

    for i in cases:
        s = i.replace(',', '')
        new_cases.append(int(s))


    covid = dict(zip(new_cases, country))

    for key, value in sorted(covid.items(), reverse=True):
        print(key, value)