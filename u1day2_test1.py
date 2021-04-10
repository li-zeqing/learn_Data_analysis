# 假设大家在30岁的时候，根据自己的实际情况，统计出来你和你同桌各自从11岁到30岁每年交的女（男）朋友
# 的数量如列表a和b，请在一个图形中绘制出该数据的折线图，以便比较自己和同桌20年间的差异，同时分析每年
# 交女（男）朋友的数量走势
from matplotlib import pyplot as plt
import random

#设置中文显示
import matplotlib
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")
y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]

x = range(11,31)
#设置图片大小
plt.figure(figsize=(12,6),dpi=80)
#绘制折线图
plt.plot(x,y_1,label="自己",color="orange",linestyle='--',linewidth=2)
plt.plot(x,y_2,label="同桌",color="cyan",linestyle='-.',linewidth=2)

#添加图例 !!只能用prop来接收中文字体，loc来接收图例位置,plt.plot()中需用label来接收图例
plt.legend(prop=my_font,loc="upper left")


#调整x轴的刻度
_xtick_labels = ["{}岁".format(i) for i in x]

#取步长,只有列表才能取步长,rotation旋转度数
plt.xticks(x,_xtick_labels,rotation=-45,fontproperties=my_font)

#调整y轴刻度
plt.yticks(range(0,9))

#添加描述信息
plt.xlabel("年龄",fontproperties=my_font)
plt.ylabel("交女朋友 数量(个)",fontproperties=my_font)
plt.title("我与同桌11到30岁交友变化情况",fontproperties=my_font)

#绘制网格 alpha为透明度参数
plt.grid(alpha=0.4)

plt.show()