import os
import pandas as pd
import glob

# 主目录路径
main_directory = 'covid19_twitter/dailies'

# 获取主目录下的所有子目录
subdirectories = [f.path for f in os.scandir(main_directory) if f.is_dir()]

# 创建一个空的DataFrame用于存储合并后的数据
merged_data = pd.DataFrame()

# 循环遍历每个子目录
for subdirectory in subdirectories:
    # 获取子目录下的所有CSV文件
    csv_files = glob.glob(os.path.join(subdirectory, '*.csv'))

    # 循环读取每个CSV文件并合并数据
    for csv_file in csv_files:
        # 读取CSV文件，并显式指定 'counts' 列为数字类型，将 NaN 转为 0
        df = pd.read_csv(csv_file, header=None, names=['gram', 'counts'])
        df['counts'] = pd.to_numeric(df['counts'], errors='coerce').fillna(0).astype(int)

        # 根据 'gram' 列进行合并，将相同的词语频率进行求和
        merged_data = pd.concat([merged_data, df], ignore_index=True)

# 根据 'gram' 列进行合并，将相同的词语频率进行求和
merged_data = merged_data.groupby('gram', as_index=False)['counts'].sum()

# 按照 'counts' 列的值进行降序排列
merged_data = merged_data.sort_values(by='counts', ascending=False)

# 将合并后的数据保存到新的CSV文件中
merged_data.to_csv('covid19_twitter/dailies/merged_data.csv', index=False)
