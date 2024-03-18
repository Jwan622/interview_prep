import pandas as pd
import matplotlib.pyplot as plt
'''
Calculate the total box office revenue for each genre.
Find the year with the highest average box office revenue.
(Bonus) Plot the total box office revenue for each genre in a bar chart.
'''
pd.set_option('display.max_columns', None)  # No column limit
pd.set_option('display.max_rows', None)  # No row limit
pd.set_option('display.width', None)  # Auto-detect the display width

df = pd.read_json('movies.json', lines=True)
print('df: ', df)

group_by_genre_df = df.groupby('genre')['box_office'].sum()
print('group_by_genre_df: ', group_by_genre_df)

group_by_year = df.groupby('release_year')['box_office'].mean()
max_year = group_by_year.loc[group_by_year.idxmax()]
print('max_year: ', max_year)
print('group_by_year: ', group_by_year)

# now do some plotting
print('plotting....')
group_by_genre_df.plot.bar(x='genre', y='box_office', rot=0)
plt.show()
