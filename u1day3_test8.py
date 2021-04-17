#numpy中的nan和inf

import numpy as np
#nan:not a number表示不是一个数字
#inf:infinity,inf表示正无穷, -inf表示负无穷

#nan和inf都是float型
a = np.nan
print(type(a))
b = np.inf
print(type(b))

#两个nan不相等
print(np.nan == np.nan)
#np.nan!=np.nan

#判断数组中nan的个数
t1 = np.array([1.,2.,np.nan])
print(np.count_nonzero(t1!=t1))
#np.isnan() 可以用来判断哪些地方等于nan
print(np.isnan(t1))

#np.isnan(t1)  等价于 t1!=t1
print(np.count_nonzero(np.isnan(t1)))  #同样可以判断数组中有多少个nan

#nan与任何值计算都为nan
print(np.sum(t1))

#np.sum(t,axis=0)或 np.sum(t,axis=1)  其中axis指定按照哪个轴计算
t2 = np.arange(12).reshape((3,4))
print(t2)
print(np.sum(t2,axis=0))
print(np.sum(t2,axis=1))

#numpy中常用统计函数
t3 = np.array([[0.,3.,3.,3.,3.,3.],
               [0.,3.,3.,3.,10.,11.],
               [0.,13.,14.,15.,16.,17.],
               [0.,19.,20.,np.nan,20.,20.]])
#求和：t.sum(axis = None)
print(t3.sum(axis=0))
print(t3.sum(axis=1))

#求均值：t.mean(a , axis  = None)
print(t3.mean(axis=0))
print(t3.mean(axis=1))

#求中值：np.median(t , axis = None)
print(np.median(t3,axis=0))

#求最大值： t.max(axis = None)
#求最小值： t.min(axis = None)
#求极值： np.ptp(t , axis = None)  既最大值和最小值的差
#求标准差：t.std(axis = None)