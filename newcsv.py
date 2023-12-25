import os
import pandas as pd

# 设置目录路径
directory = "/Users/e54true/Desktop/coivd-19/covid19_twitter/dailies/23-04"

# 初始化一个空的字典用于合并特定词汇的计数
word_counts = {}

# 要保留的特定词汇列表
desired_words = ['mask', 'vaccine', 'covid']  # 替换为您想要保留的特定词汇列表

# 循环遍历目录下的每个文件夹
for subdir, _, files in os.walk(directory):
    for file in files:
        # 确保文件是CSV文件
        if file.endswith(".csv"):
            file_path = os.path.join(subdir, file)
            # 读取CSV文件，指定列的位置
            if os.path.getsize(file_path) == 0:
                continue
            data = pd.read_csv(file_path, header=None, usecols=[0, 1])
            # 检查数据框中是否存在数据
            if not data.empty:
                # 将第一列和第二列重命名为 'gram' 和 'counts'
                data.columns = ['gram', 'counts']
                # 将 'counts' 列转换为数值类型
                data['counts'] = pd.to_numeric(data['counts'], errors='coerce')
                data['counts'] = data['counts'].replace([float('inf'), -float('inf'), float('nan')], 0)
                data['counts'] = data['counts'].astype(int)
                # 仅保留特定词汇
                data = data[data['gram'].isin(desired_words)]
                
                # 合并特定词汇的计数
                for index, row in data.iterrows():
                    word = row['gram']
                    count = row['counts']
                    if word in word_counts:
                        word_counts[word] += count
                    else:
                        word_counts[word] = count

# 创建新的DataFrame来存储合并后的数据
merged_data = pd.DataFrame(list(word_counts.items()), columns=['gram', 'counts'])

# 根据 'counts' 列降序排序
merged_data = merged_data.sort_values(by='counts', ascending=False)

# 将合并后的数据保存为一个新的CSV文件
merged_data.to_csv("specific_words_combined.csv", index=False)
