#numpy更多好用的方法
import numpy as np
#创建一个全为0的数组
t1 = np.zeros((3,4))
print(t1)
print("*t1"*50)

#创建一个全为1的数组
t2 = np.ones((3,4))
print(t2)
print("*t2"*50)

#创建一个对角线为1的正方形数组（方阵）
t3 = np.eye(4)
print(t3)
print("*t3"*50)

#获取最大值和最小值的位置
t5 = np.arange(12,24).reshape(3,4)
print(t5)
print("*t5"*50)

t6 = np.argmax(t5,axis=0)   #返回每一列中最大值所在的行下标
t7 = np.argmin(t5,axis=1)   #返回每一行中最小值所在的列下标
print(t6)
print("*t6"*50)
print(t7)
print("*t7"*50)

#numpy.random方法生成随机数组

#np.random.rand(d0,d1,...,dn) 创建d0*d1*...*dn维的均匀分布的随机数组，浮点数，范围0-1
t8 = np.random.rand(2,3,4)
print(t8)
print("*t8"*50)

#np.random.randn(d0,d1,...,dn) 创建d0-dn维的标准正态分布的随机数组，浮点数，平均数为0，标准差为1
t9 = np.random.randn(2,3)
print(t9)
print("*t9"*50)

#np.random.randint(low,high,(shape))    从给定上下限范围选取随机整数，范围：low到high-1，形状为shape
t10 = np.random.randint(10,20,(2,3))
print(t10)
print("*t10"*50)

#np.random.seed(s)  随机种子数，s是给定的种子数。

np.random.seed(10)  #此时每次刷新后，生成的随机数都不会改变
t11 =  np.random.randint(10,20,(2,3))
print(t11)
print("*t11"*50)



