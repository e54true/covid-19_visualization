
import pandas as pd
import matplotlib.pyplot as plt

# Reading CSV files
df1 = pd.read_csv('twitter_vaccine_results.csv')
df2 = pd.read_csv('monthly_covid_cases_2020_2022.csv')

# Merging data frames on 'Month'
merged_df = pd.merge(df1, df2, on='Month')

# Creating a figure and a set of subplots
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting Mask Count on the first y-axis
ax1.set_xlabel('Month')
ax1.set_ylabel('Vaccine Count', color='tab:blue')
ax1.plot(merged_df['Month'], merged_df['Vaccine Count'], color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Rotating x-axis labels to reduce overlapping
plt.xticks(rotation=45)

# Creating a second y-axis for Cases Count
ax2 = ax1.twinx()  
ax2.set_ylabel('Cases Count', color='tab:red')  
ax2.plot(merged_df['Month'], merged_df['counts'], color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Adding title and showing the plot
plt.title('Trend Comparison with vaccine and case')
plt.show()

# Calculating correlation coefficient (optional)
correlation = merged_df['Vaccine Count'].corr(merged_df['counts'])
print(f'Correlation between Mask Count and Cases Count: {correlation}')
