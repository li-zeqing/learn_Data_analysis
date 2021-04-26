#对于这一组电影数据，如果我们想Rating, Runtime的分布情况，应该如何呈现数据？
import pandas as pd
from matplotlib import pyplot as plt
#设置中文显示
import matplotlib
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")
file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)


#Rating的分布情况
#准备数据
rating_data = df["Rating"].values

max_rating = rating_data.max()
min_rating = rating_data.min()

#计算组距
print(max_rating,min_rating)

#设置不等宽的组距，hist方法中取到的会是一个左闭右开的区间[1.9,3.5)
num_bin_list = [1.9,3.5]
i = 3.5
while i<max_rating:
    i +=0.5
    num_bin_list.append(i)

print(num_bin_list)

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

#绘制直方图
plt.hist(rating_data,num_bin_list)

#刻画x轴
plt.xticks(num_bin_list)

#添加描述信息
plt.xlabel("电影评分",fontproperties=my_font)
plt.ylabel("电影时长 单位(min)",fontproperties=my_font)
plt.title("电影评分Rating和时长Runtimr的分布情况",fontproperties=my_font)

#绘制网格
plt.grid(alpha=0.5)

#展示图片
plt.show()
