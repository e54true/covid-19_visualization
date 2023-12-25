import csv
import matplotlib.pyplot as plt


covid19 = {}

for year in range(20, 23):
    if year == 20:
        for month in range(3, 13):
            filename = f'/Users/e54true/Desktop/coivd-19/covid19_twitter/dailies/top100_csv/{year:02d}-{month:02d}_top100.csv'
            with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    gram, counts = row
                    if gram == 'mask':
                        date = f"{year}-{str(month).zfill(2)}"
                        covid19[date] = int(counts)
    elif year == 23:
        for month in range(1, 5):
            filename = f'/Users/e54true/Desktop/coivd-19/covid19_twitter/dailies/top100_csv/{year:02d}-{month:02d}_top100.csv'
            with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    gram, counts = row
                    if gram == 'mask':
                        date = f"{year}-{str(month).zfill(2)}"
                        covid19[date] = int(counts)
    else:
         for month in range(1, 13):
            filename = f'/Users/e54true/Desktop/coivd-19/covid19_twitter/dailies/specific_words_csv/{year:02d}-{month:02d}_specific_words.csv'
            with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    gram, counts = row
                    if gram == 'mask':
                        date = f"{year}-{str(month).zfill(2)}"
                        covid19[date] = int(counts)
x = list(covid19.keys())
y = list(covid19.values())

plt.plot(x, y, marker='o', linestyle='-')

plt.xlabel('Year-Month')
plt.ylabel('counts')
plt.title('mask frequency')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()