# Matplotlib
```
  pip install matplotlib

  import matplotlib.pyplot as plt
```

## 折线
```
  plt.title()
  plt.xlable()    plt.ylable()
  plt.xlim()      plt.ylim()
  plt.xticks()    plt.yticks()
  plt.legend()

  plt.plot([1,2,3][3,2,1], color='black', marker="o-", label="y=x^2")
```


# work with pandas
```
  df.plot()  # use dateindex as x
  plt.show()
```


## 绘制多个子图
matplotlib下, 一个 Figure 对象可以包含多个子图(Axes), 可以使用 subplot() 
```
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)   ## 2 row, 2 col, ax1 is the first subplot
ax1.plot([1,2,3], [4,5,6])
ax2 = fig.add_subplot(2,2,2)   ## 2 row, 2 col
ax2.plot([1,2,3], [4,5,6])

fig.show()
```


```
subplot(numRows, numCols, plotNum)

```
图表的整个绘图区域被分成 numRows 行和 numCols 列
然后按照从左到右，从上到下的顺序对每个子区域进行编号，左上的子区域的编号为1

