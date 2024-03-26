import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_json('pandas_data/books_2.json', lines=True)


# how many books are in the database
grouped_df = df.groupby('bookID').agg(title_count=('title', 'sum'))
sorted_df = grouped_df.sort_values(['bookID'], ascending=True)
print('sorted_df \n', sorted_df)

# count size or sum?
title_counts = df.groupby('bookID').size()
print(title_counts)

## now that we verified that each title only appears once?
unique = df['bookID'].nunique()
print('unique titles \n', unique)

## how many boooks did each author release evry year
# what row is that 6?
df['publication_date'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year
df['authors'] = df['authors'].str.split('/')
df = df.explode('authors')
print('is the authors split? : \n', df.head(10))

grouped_df = df.groupby(['publication_date', 'authors']).agg(book_count=('bookID', 'count'))
print('grouped_df \n', grouped_df)


# which author is the max
author_counts = df.groupby('authors').size()
print('max_count of books', author_counts)
max_count = author_counts.max()
print('max count: ', max_count)
max_authors = author_counts[author_counts == max_count]
print('most_books_authors \n', max_authors)


