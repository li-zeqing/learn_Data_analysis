#pandas之DataFrame
#DataFrame为二维数组
import pandas as pd
import string
import numpy as np

t1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(t1)

#DataFrame既有行索引既有列索引
#行索引 index，0轴，axis=0
#列索引 columns 1轴，axis=1

t2 = pd.DataFrame(np.arange(12).reshape((3,4)),index=list("abc"),columns=list("ABCD"))
print(t2)

t3 = pd.DataFrame(np.arange(12).reshape((3,4)),index=list(string.ascii_lowercase[:3]),columns=list(string.ascii_uppercase[:4]))
print(t3)

#DataFrame传入字典
d1 = {"name":["xiaohong","xiaoming","xiaoli"],"age":[20,21,22],"tel":[10086,10010,10025]}
t4 = pd.DataFrame(d1)
print(t4)

d2 = [{"name":"xiaohong","age":20,"tel":10086},{"name":"xiaoming","tel":"10010"},{"name":"xiaoli","age":22}]
t5 = pd.DataFrame(d2)
print(t5)

