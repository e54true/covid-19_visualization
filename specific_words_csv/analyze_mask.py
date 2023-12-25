import pandas as pd
import matplotlib.pyplot as plt

# 讀取CSV檔案
df1 = pd.read_csv('/Users/e54true/Desktop/coivd-19/covid19_twitter/dailies/specific_words_csv/twitter_mask_tmp.csv')
df2 = pd.read_csv('/Users/e54true/Desktop/coivd-19/covid19_twitter/dailies/specific_words_csv/youtube_mask_tmp.csv')

# 合併資料框
merged_df = pd.merge(df1, df2, on='Month')

# 視覺化趨勢
plt.figure(figsize=(10, 6))
plt.plot(merged_df['Month'], merged_df['Mask Count'], label='Mask Count')
plt.plot(merged_df['Month'], merged_df['Mask Video Count'], label='Mask Video Count')
plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Trend Comparison')
plt.legend()
plt.show()

# 計算相關係數
correlation = merged_df['Mask Count'].corr(merged_df['Mask Video Count'])
print(f'Correlation between Mask Count and Mask Video Count: {correlation}')
