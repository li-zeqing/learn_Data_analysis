import numpy as np

#现在希望把之前案例中两个国家的数据放到一起研究分析，同时保留国家的信息(每条数据的国家来源)
#方法：在每条数据最后加上一列 用0表示us，用1表示uk
#读取本地数据
us_data = "./US_video_data_numbers.csv"
uk_data = "./GB_video_data_numbers.csv"

#加载国家数据
us_data = np.loadtxt(us_data,delimiter=",",dtype=int)
uk_data = np.loadtxt(uk_data,delimiter=",",dtype=int)

#添加国家信息
#在每条数据最后加上一列 用0表示us，用1表示uk   shape[0]表示行， shape[1]表示列
zeros_data = np.zeros((us_data.shape[0],1)).astype(int)
ones_data = np.ones((uk_data.shape[0],1)).astype(int)
print(zeros_data)
print(ones_data)
#水平拼接
us_data = np.hstack((us_data,zeros_data))
uk_data = np.hstack((uk_data,ones_data))

#拼接两行数据
#竖直拼接
final_data = np.vstack((us_data,uk_data))

print(final_data)
