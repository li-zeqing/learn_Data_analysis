#numpy中数值的修改
import numpy as np
import random
t2 = np.array([random.random() for i in range(64)]).reshape(8,8)
print(t2)
print("*"*100)

#where()为三元运算符， 将小于等于0.1的替换成0.1，其他的替换成0.2
t3=np.where(t2<=0.1,0.1,0.2)
print(t3)

#np.clip 裁剪
t4 = t2.clip(0.1,0.2)   #小于0.1的替换为0.1，大于0.2的替换为0.2 但是nan不能被提换




