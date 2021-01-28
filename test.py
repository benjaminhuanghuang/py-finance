import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import datetime
import time
import yfinance as yf

import requests
from bs4 import BeautifulSoup as bs


WEB_URL = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

response = requests.get(WEB_URL)
content = response.content

soup = bs(content, "html.parser")
table = soup.find('table', id='constituents')

body_rows = table.find_all('tr')[1:]

for table_row in body_rows:
  data_row = []
  for td in table_row.find_all('td'):
      if td.a:
        print(td.a.text)
      else:
        data_row.append(td.text.strip())

