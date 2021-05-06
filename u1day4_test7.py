#对于一组电影数据，如果我们想统计电影分类（genre）的情况，应该如何处理数据
#思路：重新构造一个全为0的数组，列名为分类，如果某一条数据中分类出现过，让0变为1
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#设置中文显示
import matplotlib
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")
file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
print(df.head(1))
print(df["Genre"])
#统计分类的列表
temp_list = df["Genre"].str.split(",").tolist()     #[[],[],...,[]]
print(temp_list)
genre_list = list(set([i for j in temp_list for i in j]))
#构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
print(zeros_df)
#给每个电影出现分类的位置赋值1
for i in range(df.shape[0]):
    zeros_df.loc[i,temp_list[i]] = 1
print(zeros_df.head(3))
#统计每个分类的电影的数量和
genre_count = zeros_df.sum(axis=0)
print(genre_count)
#排序
genre_count = genre_count.sort_values()

#画图
plt.figure(figsize=(20,8),dpi=80)
_x = genre_count.index
_y = genre_count.values
print(_y)
#绘制条形图
plt.bar(range(len(_x)),_y,width=0.3,color="green")
#刻画X轴
plt.xticks(range(len(_x)),_x)
#刻画Y轴刻度
plt.yticks(range(min(_y).astype(int),max(_y).astype(int)+20,20))
#添加描述信息
plt.xlabel("电影分类",fontproperties=my_font)
plt.ylabel("各类电影 数量(部)",fontproperties=my_font)
plt.title("统计电影分类（genre）的情况",fontproperties=my_font)
#绘制网格
plt.grid(alpha=0.5)
#展示图片
plt.show()

