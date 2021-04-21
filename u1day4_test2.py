#pandas读取外部数据
import pandas as pd
import string


#读取csv中的文件
df = pd.read_csv("./dogNames2.csv")

#读取mysql中的数据
# df1 = pd.read_sql(sql_sentence, connection)

#mongodb
