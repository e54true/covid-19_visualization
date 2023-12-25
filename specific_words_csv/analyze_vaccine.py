import pandas as pd
import matplotlib.pyplot as plt

# 讀取CSV檔案
df1 = pd.read_csv('twitter_vaccine_results.csv')
df2 = pd.read_csv('youtube_vaccine_results.csv')

# 合併資料框
merged_df = pd.merge(df1, df2, on='Month')

# 視覺化趨勢
plt.figure(figsize=(10, 6))
plt.plot(merged_df['Month'], merged_df['Vaccine Count'], label='Vaccine Count')
plt.plot(merged_df['Month'], merged_df['Vaccine Video Count'], label='Vaccine Video Count')
plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Trend Comparison')
plt.legend()
plt.show()

# 計算相關係數
correlation = merged_df['Vaccine Count'].corr(merged_df['Vaccine Video Count'])
print(f'Correlation between Vaccine Count and Vaccine Video Count: {correlation}')
