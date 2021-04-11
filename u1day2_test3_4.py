#在美国2004年人口普查发现有124million的人在离家相对较远的地方工作。
# 根据他们从家到上班地点所需的时间，通过抽样统计最后列出了下表的数据。
#区间
interval = [0,5,10,15,20,25,30,35,40,45,60,90]
#间距
width = [5,5,5,5,5,5,5,5,5,15,30,60]
#对应区间的数据
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

#设置图片大小
plt.figure(figsize=(20,8),dpi= 80)

plt.bar(range(len(quantity)),quantity,width = 1)

#设置x轴的刻度
_x = [i-0.5 for i in range(13)]
_xtick_labels = interval + [150]
plt.xticks(_x,_xtick_labels)


#绘制网格
plt.grid(alpha = 0.4)


#展示图片
plt.show()