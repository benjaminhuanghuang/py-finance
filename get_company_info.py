'''
    From https://github.com/victorgau/PyConTW2017
'''

import pandas as pd

def get_companies_pd(ex = "NASDAQ"):
    template = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange={}&render=download"
    url = template.format(ex)
    return pd.read_csv(url)

data = get_companies_pd("NYSE")
data.head()
data[data['MarketCap'] < 1e8].head()




