import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open('covid19_twitter/dailies/top100_csv/merged_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  
    your_list = '\t'.join([row[0] for row in reader])

#wordcloud = WordCloud().generate(your_list)
wordcloud = WordCloud(width=1600, height=900).generate(your_list)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()