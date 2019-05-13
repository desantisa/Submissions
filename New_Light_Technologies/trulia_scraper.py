import os
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
import time
import numpy as np
import pandas as pd
from uszipcode import SearchEngine


def URL_generator(zipcode):
    zipcode = str(zipcode)

    search = SearchEngine(simple_zipcode=True)
    zipcode_data = search.by_zipcode(zipcode)
    zip_dict = zipcode_data.to_dict()
    city_state = zip_dict['post_office_city'].split(', ')
    city_state[0] = city_state[0].replace(' ', '_')

    url = 'https://www.trulia.com/{}/{}/{}/'.format(city_state[1], city_state[0], zipcode)
    return url


def driver_generator(path = './', driver_type = 'Firefox'):
    driver_path = os.path.expanduser(path)
    sys.path.append(driver_path)

    if (driver_type == 'Firefox'):
        option = webdriver.FirefoxOptions()
        option.headless = True
        driver = webdriver.Firefox(driver_path, options=option)

    if (driver_type == 'Chrome'):
        option = webdriver.ChromeOptions()
        option.headless = True
        driver = webdriver.Chrome(driver_path, options=option)

    return driver

def house_data(url, driver, pages=20):
    df = pd.DataFrame(columns=['address', 'city', 'state', 'area', 'bedrooms', 'bathrooms', 'price'])
    price_list = []
    bed_list = []
    bath_list = []
    sqft_list = []
    address_list = []
    city_list = []
    state_list = []

    driver.get(url)

    for i in range(pages):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        listings = soup.find_all('div', class_='ptm cardContainer positionRelative clickable')
        for row in listings:
            price = row.find('span', class_='cardPrice h5 man pan typeEmphasize noWrap typeTruncate').text
            ul = row.find('ul', class_='listInline typeTruncate mvn')
            obj_bed = ul.find('li', {'data-auto-test': 'beds'})
            obj_bath = ul.find('li', {'data-auto-test': 'baths'})
            obj_sqft = ul.find('li', {'data-auto-test': 'sqft'})
            if ('Contact' not in price) and (obj_bed != None) and (obj_bath != None) and (obj_sqft != None):
                price  = float(price.strip('$+ ').replace(',',''))
                try:
                    nbed = int(obj_bed.text[0])
                except:
                    nbed = obj_bed.text
                nbath = int(obj_bath.text[0])
                sqft = float(obj_sqft.text.split(' ')[0].replace(',', ''))
                address = row.find('div', class_='h6 typeWeightNormal typeTruncate typeLowlight mvn').text
                city_state = row.find('div', class_='typeTruncate typeLowlight').text.split(', ')
                if (len(city_state) > 2):
                    city_state = city_state[1:]
                city = city_state[0]
                state = city_state[1]

                price_list.append(price)
                bed_list.append(nbed)
                bath_list.append(nbath)
                sqft_list.append(sqft)
                address_list.append(address)
                city_list.append(city)
                state_list.append(state)

        time.sleep(np.random.lognormal(0,1))
        next_button = soup.find('a', {'aria-label': 'Next page'})
        if (next_button != None):
            driver.get(next_button['href'])
        else:
            break

    df['address'] = address_list
    df['city'] = city_list
    df['state'] = state_list
    df['area'] = sqft_list
    df['bedrooms'] = bed_list
    df['bathrooms'] = bath_list
    df['price'] = price_list

    driver.quit()

    return df


def trulia_data(zipcode):
    url = URL_generator(zipcode)
    driver = driver_generator()
    df = house_data(url, driver)
    return df
