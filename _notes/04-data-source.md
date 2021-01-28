

## Tushare
free, opensoure for A  
```
  pip install Tushare
  pip install Tushare --upgrade

  df = ts.get_k_data('601318', start='1980-01-01')
```


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

