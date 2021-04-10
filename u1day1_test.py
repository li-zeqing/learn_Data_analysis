#如果列表a表示10点到12点的每一分钟的气温，如何绘制折线图观察每分钟气温的变化情况？
# a = [random.randint(20,35) for i in range(120)]
from matplotlib import pyplot as plt
import random

#设置中文显示
import matplotlib
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")


x = range(0,120)
y = [random.randint(20,35) for i in range(120)]
plt.figure(figsize=(50,6),dpi = 80)
plt.plot(x,y,color="orange",linestyle='--',linewidth=2)
#调整x轴的刻度
_x = list(x)
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i-60) for i in range(60,120)]
#取步长 #只有列表才能取步长 #rotation旋转度数 #fontproperties接收中文字体
plt.xticks(_x[::3],_xtick_labels[::3],rotation=-45,fontproperties=my_font)
#_x[::3]和_xtick_labels[::3]点数要一致

#添加描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位(℃)",fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)

#绘制网格
plt.grid(alpha=0.4)
#alpha 为透明度参数

plt.show()
