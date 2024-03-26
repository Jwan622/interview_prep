import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

df = pd.read_json('pandas_data/books_2.json', lines=True)


#1. how many books are in the database

# first check to see if there are any dupes:
unique_book_ids_count = df['bookID'].nunique()
total_title_count = df['title'].nunique()
print('total title count: :', total_title_count)
print('unqieu book ids count: ', unique_book_ids_count)
total_books = len(df)
print('total_books: ', total_books)

#curious, title count is less. why?
duplicate_titles = df[df.duplicated('title', keep=False)]
# Sort by title to make inspection easier
sorted_duplicate_titles = duplicate_titles.sort_values(by='title')
print('Duplicate Titles:\n', sorted_duplicate_titles.head(30))

# ah so there are duplicate book titles from different publishers.!

# any Nans in titles which is why it's less?
nan_bookIDs = df[df['bookID'].isna()]
nan_titles = df[df['title'].isna()]

print('Rows with NaN Book IDs:\n', nan_bookIDs)
print('Rows with NaN Titles:\n', nan_titles)

# nope it's just that there are duplicated titles

# count size or sum?
'''
 using size() gives you the total number of entries, including those with NaN authors, while count() gives you the number of non-null entries in each column for each group of authors.
'''
title_counts = df.groupby('bookID').agg(book_id_counts=('bookID', 'count')).sort_values(by=['book_id_counts'], ascending=False)
# so bookID is not duped.
print(title_counts.head(6))

#2. how many books did each author release every year
# what row is that 6?
df['publication_date'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year
# let's see the row
nat_rows = df[df['publication_date'].isna()]
print('nat rows: \n', nat_rows)

# now let's explode the authors since they are seperated by a / and so we want to explode that out into 2 rows.
df['authors'] = df['authors'].str.split('/')
df = df.explode('authors')
print('is the authors split? : \n', df.head(10))

grouped_df = df.groupby(['publication_date', 'authors']).agg(book_count=('bookID', 'count'))
print('grouped_df for pub date and authors \n', grouped_df.head(10))
# find specific year?
print('find specific year: \n', grouped_df.loc[1913.0])


#3.  which author has the max amount of books, not grouped by year
author_counts = df.groupby('authors').size()
print('max_count of books \n', author_counts.head(10))
max_count = author_counts.max() # max is called on a group by
print('max count: ', max_count)
max_authors = author_counts[author_counts == max_count] # this is boolean indexing
print('most_books_authors \n', max_authors.head(5))


