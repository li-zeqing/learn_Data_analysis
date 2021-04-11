from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

#四部电影某月的14,15,16日的当日实时票房
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]
#组距
bar_width = 0.3

x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]
#设置图片大小
plt.figure(figsize=(20,15),dpi=80)

#绘制条形图
plt.barh(x_14,b_14,height=bar_width,color="orange",label= "14日票房")
plt.barh(x_15,b_15,height=bar_width,color="blue",label= "15日票房")
plt.barh(x_16,b_16,height=bar_width,color="red",label= "16日票房")
#添加图例
plt.legend(loc="upper right",prop=my_font)

#设置字符串到Y轴
plt.yticks(x_15,a,fontproperties=my_font)

#绘制网格
plt.grid(alpha=0.3)

#添加描述信息
plt.xlabel("票房(单位/元)",fontproperties=my_font)
plt.title("实时票房对比",fontproperties=my_font)
#展示图片
plt.show()