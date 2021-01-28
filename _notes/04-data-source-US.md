##
https://www.quandl.com/tools/python

s

##  yahoo finance
数据很有限
```
  import yfinance as yf

  data = yf.download('AAPL', '2020-1-1', '2021-1-1')
```
return 
```
                  Open        High         Low       Close   Adj Close     Volume
Date                                                                             
2020-01-02   74.059998   75.150002   73.797501   75.087502   74.444603  135480400
```

```
   # Fetch the data
  import yfinance as yf
  tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']
  data = yf.download(tickers_list,'2015-1-1')['Adj Close']

  print(data.head())
```
return
```
                 AAPL        AXP          BA         IBM         MU        WMT
Date                                                                          
2015-01-02  24.898552  84.234779  112.786011  124.083694  34.750000  74.167084
2015-01-05  24.197117  82.007118  112.004875  122.131233  33.779999  73.951225
2015-01-06  24.199400  80.259384  110.685638  119.497353  32.869999  74.521065
2015-01-07  24.538729  82.012276  112.404106  118.716354  32.099998  76.498276
2015-01-08  25.481558  83.174782  114.391670  121.296631  33.669998  78.112862
```