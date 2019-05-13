import pandas as pd


def clean_zip(x):
    x = x.split('.')[0]
    x = x.zfill(5)
    return x


def realtor_data(zipcode):
    url = 'https://s3-us-west-2.amazonaws.com/econresearch/Reports/Core/RDC_InventoryCoreMetrics_Zip.csv'
    data = pd.read_csv(url)
    data['ZipCode'] = data['ZipCode'].astype('str')
    data['ZipCode'] = data['ZipCode'].map(clean_zip)
    df = data[data['ZipCode'] == zipcode]
    return df
