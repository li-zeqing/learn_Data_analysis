#numpy库  快速生成数组
import random

import numpy as np
t1 = np.array([1,2,3])
print(t1)

t2 = np.array(range(1,6))
print(t2)

t3 = np.arange(12)
print(t3)
print(type(t3))
print(t3.dtype)

#numpy中的数据类型 dtype参数可以指定数据类型
t4 = np.array(range(1,4),dtype="i1")
print(t4)
print(t4.dtype)

#numpy中的bool类型
t5 = np.array([2,0,1,0,0,1],dtype=bool)
print(t5)
print(t5.dtype)

#调整数据类型
t6 = t5.astype("int8")
print(t6)
print(t6.dtype)

#numpy中的小数
#random.random(参数1,参数2) 参数1和参数2需为整数，结果返回参数1和参数2之间的任意整数
print(random.randint(1,5))

#random.random()用于生成一个0到1的随机小数  0<= n <1.0
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

#取小数
t8 = np.round(t7,2)
print(t8)
print(t8.dtype)
