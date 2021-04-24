import pandas as pd

file_path = "IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

#查看文件描述信息
# print(df.info())

#获取电影的平均评分
print(df["Rating"].mean())

#获取导演人数
print(len(set(df["Director"].tolist())))

print(len(df["Director"].unique())) #unique()唯一的意思

#获取演员人数
temp_actors_list = df["Actors"].str.split(", ").tolist()
print(temp_actors_list)

actors_list = [i for j in temp_actors_list for i in j]
print(actors_list)
actors_num = len(set(actors_list))
print(actors_num)
