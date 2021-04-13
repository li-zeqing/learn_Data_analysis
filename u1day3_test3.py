#numpy 切片和索引
import numpy as np
import random
t2 = np.array([random.random() for i in range(64)]).reshape(8,8)
print(t2)
print("*"*100)

#取行
# print(t2[2])

# print(t2[2,:])

#取连续多行
# print(t2[2:])

# print(t2[2:,:])

#取不连续多行
# print(t2[[2,5,7]])

# print(t2[[2,5,7],:])


#取列
# print(t2[:,1])

#取连续的多列
# print(t2[:,2:])

#取不连续的多列
# print(t2[:,[0,2]])

#取行和列
# print(t2[2,3]) #取第3行第4列

#取多行多列 取交叉点的数
print(t2[2:5,3:4])  #取第3行到第5行，第4列

#取多个不相邻的点
# print(t2[[0,2,2],[0,1,3]]) #取的是(1,1),(3,2),(3,4)这三个点


