#对于这一组电影数据，如果我们想Rating, Runtime的分布情况，应该如何呈现数据？
import pandas as pd
from matplotlib import pyplot as plt
file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
print(df.head(1))
print(df.info())

#Runtime分布情况
#选择直方图
#准备数据

runtime_data = df["Runtime (Minutes)"].values
print(runtime_data)
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

#计算组距
print(max_runtime-min_runtime)
num_bin = (max_runtime-min_runtime)//5

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

#绘制直方图
plt.hist(runtime_data,num_bin)

#刻画x轴
plt.xticks(range(min_runtime,max_runtime+5,5))

#绘制网格
plt.grid(alpha=0.5)

#展示图片
plt.show()

