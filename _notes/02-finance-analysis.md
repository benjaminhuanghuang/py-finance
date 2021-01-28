## 基本面
### 增长率
### 市值
### 市盈率 PE
市盈率（PE）用来评估股价水平是否合理的指标之一，由股价除以年度每股盈余（EPS）得出.
PE = Price per share / Earnings per Share

PE标示几年回本
投资越快回本越好，那么就应该买PE低的股票呢？长期投资，买便宜（PE低）的股票，但最低的也不一定好，可能太不活跃或太大盘，盈利能力不强

1、同行业PE 排名
2、同支股票的历史PE走势
### 净资产收益率 ROE

### 现金流
计算未来现金流的现值， R是折现率，n是周期数
```
PV = FV / (1+R)^n
```
### 永久年金
 指为了每隔一段时间有等额的现金支付, R是周期折现率，C是每个周期的定额支付
```
 PV(永久年金) = C/R
```
增长型永久年金, g是每周期增长率
```
 PV(永久年金) = C/(R-g)
```

## 技术面
- K线: 最高，最低，收盘，开盘，颜色

- MA(Moving Average)

每个交易日可以计算出前N天的移动平均值，这些移动平均值构成N日移动平均线

MA 通常有 5D， 10D， 30D， 60D， 120D，240D

短期均线上穿长期均线 为买入信号

短期均线下穿长期均线 为卖出信号

- KDJ 随机指标

- MACD 指数平滑移动平均线

## 选股策略


- Bollinger Band

  中间线 20日均线

  Up = 20 日均线 + N * SD(20日收盘价)
  
  Down = 20 日均线 - N * SD(20日收盘价)
  
  股价突破up  卖， 股价突破down  买

```
  N = 2
  sr = get_history(20 days)['close']
  ma = sr.mean()
  up = ma + N * sr.std()
  down = ma - N * sr.std()

  price = get_current_data()['open']

  if p < down and no_hold
    ## BUY
  elif p > up and hold
    ## SELL
```

- 市盈率 PE
PE = Price(股价) / EPS (Earnings per Share 每股收益) = 市值 / 净收益

G（收益增长率）= （EPS2 - EPS1）/ EPS1

PEG = PE /(G * 100)

选 PEG 最小的 股票， 过滤收益增长率为负的股票
```
  df = df[(df['pe']>0) & (df['inc_net_profit_yearly']>0)]
  df['peg'] = df['pe'] / df['inc_net_profit_yearly'] / 100
  df = df.sort(coloums='peg')

  tohold = df['code'][:N].value   # 选 PEG 最小的 股票

```