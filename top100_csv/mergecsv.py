import pandas as pd
import glob

# 获取所有CSV文件的文件名
csv_files = glob.glob('covid19_twitter/dailies/top100_csv/*.csv')

# 创建一个空的DataFrame用于存储合并后的数据
merged_data = pd.DataFrame()

# 循环读取每个CSV文件并合并数据
for file in csv_files:
    # 读取CSV文件
    df = pd.read_csv(file)
    
    # 根据'gram'列进行合并，将相同的词语频率进行求和
    merged_data = pd.concat([merged_data, df], ignore_index=True)

# 根据'gram'列进行合并，将相同的词语频率进行求和
merged_data = merged_data.groupby('gram', as_index=False)['counts'].sum()

# 按照 'counts' 列的值进行降序排列
merged_data = merged_data.sort_values(by='counts', ascending=False)

# 将合并后的数据保存到新的CSV文件中
merged_data.to_csv('covid19_twitter/dailies/top100_csv/merged_data.csv', index=False)
