'''
    read stock data from csv
'''
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 


df = pd.read_csv('data/tsla.csv', parse_dates = True, index_col = 0)
# df.plot()
df['Close'].plot()
plt.show()