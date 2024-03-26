import pandas as pd
import numpy as np

data = {
    'Title': ['To Kill a Mockingbird', '1984', None, 'The Great Gatsby', 'The Catcher in the Rye', 'Pride and Prejudice', 'Wuthering Heights', 'The Hobbit', None, 'Fahrenheit 451', 'three body problem'],
    'Author': ['Harper Lee', 'George Orwell', 'Aldous Huxley', 'F. Scott Fitzgerald', 'J.D. Salinger', 'Jane Austen', 'Emily Brontë', None, 'Ray Bradbury', 'Ray Bradbury', 'some asian guy'],
    'Year': [1960, 1949, 1932, 1925, 1951, 1813, 1847, 1937, 1953, None, '2021'],
    'Genre': ['Southern Gothic', 'Dystopian', 'Dystopian', None, 'Coming-of-age', 'Classic Romance', 'Gothic', 'Fantasy', 'Dystopian', 'Science Fiction', 'Science Fiction']
}

df = pd.DataFrame(data)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

# count is null in a column
print('missing years should be 1: ', df['Year'].isna().sum())
print('missing Author should be 1: ', df['Author'].isna().sum())
print('missing in all columns should be 2,1,1,1 \n: ', df.isna().sum())


# fill in year with median year
print('year median: ', df['Year'].median())
df.fillna({'Year' : df['Year'].median()}, inplace=True)
print('df with filled in year: \n', df)

# remove rows where title or author is missing since those are critical piece of info
df.dropna(subset=['Title', 'Author'], inplace=True)
print('df with droppedrows, only 7 left: \n', df)

# convert all to numerica
df['Year'] = pd.to_numeric(df['Year']).astype(int)
print('df with cleaned years: ', df)

# avg publication year for each genre.
print('mean of each genre year: \n', df.groupby('Genre').agg({'Year': 'mean'}).astype(int))

# how many books are in each genre
print('how many books are in each genre: \n', df.groupby('Genre').agg({'Title': 'count'}).astype(int))

# title length
df['Title_Length'] = df['Title'].apply(lambda x: len(x))
print('added title length: \n', df)


# hmmm let's see what this does first
# dates = pd.date_range('1/1/2001', periods=12, freq="MS")
# print('dates: ', dates)
# df = pd.DataFrame({"jA": 5*np.arange(len(dates))+2}, index=dates)
# print('df head: \n', df.head())
# group the books by decade of publication

# anyway let's group by decade for our original dataframe now and count number of books in each decade
df['Decade'] = df['Year'] // 10 * 10
print('df with decade: \n', df)
grouped_by = df.groupby('Decade').agg({'Title': 'count'})
print('titles per decade: \n', grouped_by)


# Which titles contain the word The?
the_series = df['Title'].str.contains('The', na=False)
print('the series: \n', the_series)
