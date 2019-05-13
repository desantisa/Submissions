import quandl
import pandas as pd

def get_key(path = './quandl_key.conf'):
    with open(path, 'r') as f:
        key = f.readline()

    return key


def historical_data(zipcode):
    key = get_key()
    indicator = 'ZILLOW/Z' + str(zipcode) + '_MLPAH'
    quandl.ApiConfig.api_key = key
    try:
        df = pd.DataFrame(quandl.get(indicator))
    except:
        df = ''
    return df
