import pandas as pd
import numpy as np
import string
#Series 为带标签的一维数组  由键index和值values组成 键->值
t1=pd.Series(np.arange(10))
print(t1)


#用index来指定标签（索引）的值，但个数须和数组个数相同
t2=pd.Series(np.arange(10),index= list(string.ascii_uppercase[:10]))
print(t2)
print(type(t2))

#通过字典创建一个Series数组
temp_dict = {"name":"xiaohong","age":30,"tel":10086}
t3 = pd.Series(temp_dict)
print(t3)

#string.ascii_uppercase表示取ABC..
a = {string.ascii_uppercase[i]:i for i in range(10)}
t4=pd.Series(a)
print(t4)
print(a)

t5 = pd.Series(a,index=list(string.ascii_uppercase[5:15]))
print(t5)


#Series 切片和索引

print(t3["age"])
print(t3[1])

#取连续的多行
print(t3[:2])
#取不连续的多行
print(t3[["age","tel"]])


print(t1[t1>5])

#获取索引 t.index
print(t3.index)
print(list(t3.index)[:2])
print(type(t3.index))
#获取具体的值 t.values
print(t3.values)
print(list(t3.values)[1:])
print(type(t3.values))
