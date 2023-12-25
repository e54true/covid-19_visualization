import os
import datetime
import csv
from googleapiclient.discovery import build
import matplotlib.pyplot as plt

# 第一個程式碼
API_KEY = 'AIzaSyB_FyOU0THJveCUNevPUeXh4LL99Gth1-c'
youtube = build('youtube', 'v3', developerKey=API_KEY)
search_query = 'covid-19 shot vaccine news usa'
max_results = 50
monthly_counts_youtube = {}
start_date_youtube = datetime.date(2020, 4, 1)
end_date_youtube = datetime.date(2022, 12, 31)  # 調整為結束日期
current_date_youtube = start_date_youtube

while current_date_youtube < end_date_youtube:
    date_start = current_date_youtube
    date_end = current_date_youtube + datetime.timedelta(days=30)
    search_response = youtube.search().list(
        q=search_query,
        part='snippet',
        type='video',
        order='relevance',
        maxResults=max_results,
        publishedAfter=date_start.isoformat() + 'T00:00:00Z',
        publishedBefore=date_end.isoformat() + 'T23:59:59Z',
        videoDuration='short',
        videoDimension='2d'
    ).execute()
    count = search_response['pageInfo']['totalResults']
    monthly_counts_youtube[current_date_youtube.strftime('%y-%m')] = count  # 修改此行
    current_date_youtube += datetime.timedelta(days=30)

months_youtube = list(monthly_counts_youtube.keys())
counts_youtube = list(monthly_counts_youtube.values())

# 第二個程式碼
covid19 = {}
for year in range(20, 23):
    if year == 20:
        for month in range(4, 13):
            filename = f'/Users/e54true/Desktop/coivd-19/covid19_twitter/dailies/specific_words_csv/data/{year:02d}-{month:02d}_specific_words.csv'
            with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    gram, counts = row
                    if gram == 'vaccine':
                        date = f"{year:02d}-{str(month).zfill(2)}"
                        covid19[date] = int(counts)
    elif year == 23:
        for month in range(1, 5):
            filename = f'/Users/e54true/Desktop/coivd-19/covid19_twitter/dailies/specific_words_csv/data/{year:02d}-{month:02d}_specific_words.csv'
            with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    gram, counts = row
                    if gram == 'vaccine':
                        date = f"{year:02d}-{str(month).zfill(2)}"
                        covid19[date] = int(counts)
    else:
         for month in range(1, 13):
            filename = f'/Users/e54true/Desktop/coivd-19/covid19_twitter/dailies/specific_words_csv/data/{year:02d}-{month:02d}_specific_words.csv'
            with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    gram, counts = row
                    if gram == 'vaccine':
                        date = f"{year:02d}-{str(month).zfill(2)}"
                        covid19[date] = int(counts)

x_covid19 = list(covid19.keys())
y_covid19 = list(covid19.values())

with open('youtube_vaccine_results.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Month', 'Video Count'])
    for month, count in zip(months_youtube, counts_youtube):
        csv_writer.writerow([month, count])

# 第二個程式碼
with open('twitter_vaccine_results.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Month', 'Mask Count'])
    for date, count in zip(x_covid19, y_covid19):
        csv_writer.writerow([date, count])

# 重疊兩個資料集的折線圖
plt.figure(figsize=(20, 12))

# 使用月份作為 x 軸
plt.plot(months_youtube, counts_youtube, marker='o', linestyle='-', label='Youtube mask frequency')
plt.plot(x_covid19, y_covid19, marker='o', linestyle='-', label='Twitter mask frequency')

plt.xticks(rotation=45)
plt.xlabel('Time (Month)')
plt.ylabel('Counts')
plt.title('Comparison of Youtube and Twitter vaccine frequency')
plt.legend()
plt.grid(True)

# 顯示圖形
plt.show()
