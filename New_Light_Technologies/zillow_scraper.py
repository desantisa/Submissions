import os
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
import time
import numpy as np
import pandas as pd
import zillow


def get_key(path = './zillow_key.conf'):
    with open(path, 'r') as f:
        key = f.readline()

    return key


def URL_generator(zipcode):
    zipcode = str(zipcode)
    url = 'https://www.zillow.com/homes/for_sale/' + zipcode + '_rb/'
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


def get_zpids(url, driver, pages=20):
    zpid_data = []
    driver.get(url)
    time.sleep(5)
    for i in range(pages):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        listings = soup.find_all('a', class_='zsg-photo-card-overlay-link')
        zpid = [row['href'].split('/')[-2].split('_')[0] for row in listings if 'AuthRequired' not in row['href']]
        zpid_data.extend(zpid)
        time.sleep(np.random.lognormal(0, 1))
        next_button = soup.find('a', class_='off')
        if (next_button != None):
            next_button_link = 'https://www.zillow.com' + next_button['href']
            driver.get(next_button_link)
        else:
            break

    driver.quit()

    return zpid_data


def house_data(key, api, zpid_list):
    df = pd.DataFrame(columns=['zpid', 'address', 'city', 'state', 'latitude', 'longitude', 'price'])
    valid_zpids = []
    address_list = []
    city_list = []
    state_list = []
    latitude_list = []
    longitude_list = []
    price_list = []

    for zpid in zpid_list:
        try:
            data = api.GetZEstimate(key, zpid)
            data_dict = data.get_dict()
            valid_zpids.append(zpid)
            address_list.append(data_dict['full_address']['street'])
            city_list.append(data_dict['full_address']['city'].capitalize())
            state_list.append(data_dict['full_address']['state'])
            latitude_list.append(float(data_dict['full_address']['latitude']))
            longitude_list.append(float(data_dict['full_address']['longitude']))
            price_list.append(data_dict['zestimate']['amount'])
        except:
            pass

    df['zpid'] = valid_zpids
    df['address'] = address_list
    df['city'] = city_list
    df['state'] = state_list
    df['latitude'] = latitude_list
    df['longitude'] = longitude_list
    df['price'] = price_list

    return df


def zillow_data(zipcode):
    key = get_key()
    url = URL_generator(zipcode)
    driver = driver_generator()
    zpids = get_zpids(url, driver)
    api = zillow.ValuationApi()
    df = house_data(key, api, zpids)
    return df
