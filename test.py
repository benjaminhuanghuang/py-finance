import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import datetime
import time
import yfinance as yf

SYMBOL = 'AAPL'
data = yf.download(SYMBOL, '2020-1-1', '2021-1-1')
print(data)