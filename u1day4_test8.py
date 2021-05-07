#现在我们有一组关于全球星巴克店铺的统计数据，如果我想知道美国的星巴克数量和中国的哪个多，
# 或者我想知道中国每个省份星巴克的数量的情况，那么怎么办？
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#设置中文显示
import matplotlib
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")
file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
print(df.head(3))
print(df.info())
#分组聚合
# groupe = df.groupby(by="columns name")
# groupe是一个DataFrameGroupBy的对象，是可迭代的
# groupe中的每一个元素是一个元组 元组里面是（索引（分组的值），分组之后的DataFrame）
grouped = df.groupby(by="Country")
print(grouped)
#DataFrameGroupBy
#可以进行遍历
for i,j in grouped:
    print(i)
    print("_"*50)
    print(j)
    print("*"*50)

# df[df["Country"]=="US"]
#调用聚合方法
country_count = grouped["Brand"].count()
print(country_count)
#US和CN的Brand数量
print(country_count["US"])
print(country_count["CN"])

#统计中国每个省份星巴克店铺的数量
China_data = df[df["Country"]=="CN"]
China_grouped = China_data.groupby(by="State/Province").count()["Brand"]
print(China_grouped)

#数据按照多个条件进行分组，返回Series
grouped_more = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
print(grouped_more)
#此时索引就有多个【复合索引】

#数据按照多个条件进行分组，方括号嵌套方括号，返回DataFrame
grouped_more1 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
grouped_more2 = df.groupby(by=[df["Country"],df["State/Province"]])[["Brand"]].count()
grouped_more3 = df.groupby(by=[df["Country"],df["State/Province"]]).count()[["Brand"]]
print(grouped_more1,type(grouped_more1))
print("1"*50)
print(grouped_more2,type(grouped_more2))
print("2"*50)
print(grouped_more3,type(grouped_more3))
print("3"*50)

#索引的方法和属性
print(grouped_more1.index)
#获取index：df.index
#指定(修改)index:df.index = ['X','Y']
#与df.index不同，重新设置index，新索引的值全为Nan :df.reindex(list("abcf"))
#指定某一列作为索引:df.set_index("Country",drop=False)   #drop默认为True，既为删去改列 drop为False时保留该列为列索引
#返回index的唯一值：df.set_index("Country").index.unique()  #侧面声明index横索引可以是相同值

#假设a为一个DataFrame，那么当a.set_index(["c","d"])即设置两个索引的时候是怎么的结果
a = pd.DataFrame({'a':range(7),'b':range(7,0,-1),'c':['one','one','one','two','two','two','two'],'d':list("hjklmno")})
print(a)

#交换复合索引中的横索引 a.swaplevel()

