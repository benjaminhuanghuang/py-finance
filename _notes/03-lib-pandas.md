# Pandas
based on numpy, DataFrame, Series, DateTime serices
```
  pip install pandas
```

## Series(array + dict)
- Create
```
  pd.Series([1,2,3,4], index=['a','b','c','d'])

  pd.Series({'a':1, 'b':2})
  
  pd.Series(0, index=['a','b','c','d'])
```

sr[10]          # 10 is tag

sr.iloc(index)  # 10 is index      
sr.loc(tag)     # 10 is tag  


- Series 运算
```
  sr1 = pd.Series([1,2,3], index=['c','a','d'])
  sr2 = pd.Series([6,8,7], index=['d','c','a'])
```
sr1 + sr1 会按照 tag进行操作， 缺失的数据结果为NaN

填充缺失值
```
  sr1.add(sr1, fill_value=0)
```

## DataFrame
- Create
```
  pd.DataFrame({'one':[1,2,3], 'two':[4,5,6]})
  pd.DataFrame({'one':pd.Series([1,2,3], index=['c','a','d']), 
                'two':pd.Series([1,2,3], index=['c','a','d'])})
```
read/write csv
```
  df.read_csv('a.csv', index_col='date', parse_dates=['date'])

  # when there is no col header in csv
  df.read_csv('a.csv', index_col='date', header=None, names=['col1','col2'])

  df.to_csv(sep="", na_rep="", )
```

read_table
```
  spe

```

- Access value
```
  df.loc['a', :]
```

- Handle NaN
```
  dropna()

  finllna()

  innull()

  notnull()
```

- Statistics
```
  df.mean()            # mean by col
  df.mean(asix=1)      # mean by row

  df.sort_values(by='two', ascending=False)

  df.describ()
```

## datetime
```
  import dateutil

  datetuil.parse.parse('2011-JAN-01')

  pd.to_datetime(['2011-JAN-01', '2011-DEC-01'])

  pd.date_range('2011-JAN-01', '2011-DEC-01') # start to end
  pd.date_range('2011-JAN-01',  periods=60)              # 60 days
  pd.date_range('2011-JAN-01',  periods=60, freq='H')    # 60 days * hours
  pd.date_range('2011-JAN-01',  periods=60, freq='1h20min')    # 60 days 1h20ms
  pd.date_range('2011-JAN-01',  periods=60, freq='W-MON')    # 60 days every monday
  pd.date_range('2011-JAN-01',  periods=60, freq='B')    # 60 days business days

```
- Statistics
```
  sr.resamle('W').mean()            # every week
  sr.resamle('M').mean()            # every month

  sr.truncate(before='2011-JAN-01')
```
