import pandas as pd
import matplotlib.pyplot as plt

# 创建一个空的数据框来存储所有数据
all_data = pd.DataFrame()

# 循环读取每个 CSV 文件并将其合并到 all_data 中
for year in range(20, 23):
    if year == 20:
        for month in range(3, 13):
            filename = f'/Users/e54true/Desktop/coivd-19/covid19_twitter/dailies/top100_csv/{year:02d}-{month:02d}_top100.csv'
            data = pd.read_csv(filename)
            all_data = pd.concat([all_data, data])
    elif year == 23:
        for month in range(1, 5):
            filename = f'/Users/e54true/Desktop/coivd-19/covid19_twitter/dailies/top100_csv/{year:02d}-{month:02d}_top100.csv'
            data = pd.read_csv(filename)
            all_data = pd.concat([all_data, data])
    else:
         for month in range(1, 13):
            filename = f'/Users/e54true/Desktop/coivd-19/covid19_twitter/dailies/top100_csv/{year:02d}-{month:02d}_top100.csv'
            data = pd.read_csv(filename)
            all_data = pd.concat([all_data, data])