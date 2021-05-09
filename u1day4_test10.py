#全球星巴克店铺的统计数据
#使用matplotlib呈现出店铺总数排名前十的国家
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
#准备数据 按照国家进行排序
df = df[df["Country"]=="CN"]
data1 = df.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:25]
print(data1)
_x = data1.index
_y = data1.values

#绘图
plt.figure(figsize=(20,8),dpi=80)

plt.bar(range(len(_x)),_y,width=0.3,color="orange")
#刻画x轴刻度
plt.xticks(range(len(_x)),_x,rotation=-45,fontproperties = my_font)
#刻画Y轴刻度
plt.yticks(range(min(_y),max(_y)+20,20))

plt.grid(alpha=0.3)
plt.show()
