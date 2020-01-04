
## 绘制多个子图
matplotlib下, 一个 Figure 对象可以包含多个子图(Axes), 可以使用 subplot() 快速绘制, 其调用形式如下 :
subplot(numRows, numCols, plotNum)

图表的整个绘图区域被分成 numRows 行和 numCols 列
然后按照从左到右，从上到下的顺序对每个子区域进行编号，左上的子区域的编号为1
