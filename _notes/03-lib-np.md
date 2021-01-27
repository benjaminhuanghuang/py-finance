# Numpy
  array, ndarray 方便数组处理, 线性代数运算 a.T
```
  pip install numpy
```
 

Create N random
```
  import random

  a = [random.uniform(100.0, 200) for i in range(50)]
  
  np.array(a)
```

Create np array
```
  np.zeros(10)               # 0s array
  np.ones(10)                # 1s array
  np.empty(10)               # 

  np.arange(start, end, step)

  np.linspace(start, end, how-many-numbers)

  np.eye(10)                 # 单位矩阵


  np.arange(15).reshape(3, 5)
```

array vs number + - * // **  > <
```
  a = np.array(a)
  a * x

  a > 5
```

array vs array: + / ** % ==
```
```

赋值 
```
  b = a[5:8]             # 浅copy
  b = a[5:8].copy()      # 深copy
```

bool index 可用作 filter
```
  b = a[a>0]      # a[a[True, False, False, True]]    
  b = a[(a>5) & (a%2==0)]     # 此处不能用and    
```

- statistics
```
sum()  

min() max()  argmin() argmin()

std() var()

```