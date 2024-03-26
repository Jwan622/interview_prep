import pandas as pd

# Lets find the stores with the max total sales average for stores after 2001.
# a = 20 + 30 + 10 + 20 = 80
# b = 20 + 80 + 20 = 120
# c = 30 + 15 + 45 = 90
# d = 90
# A couple ways:

# Load the CSV file into a DataFrame
df = pd.read_csv('pandas_data/store_data.csv')

df['Total Sales'] = df['Price'] * df['Quantity']
print('df with total sales \n', df)
# Sum total sales by product and sort in descending order
top_products = df.groupby('Product')['Total Sales'].sum().sort_values(ascending=False).head(3)
print('top products: \n', top_products)

#1. first way to find stores with the highest average sales
# Calculate average sales per store. if multiple rows match the max, this will return them
average_sales_per_store = df.groupby('Store')['Total Sales'].mean()
print('average_sales_per_store: \n', average_sales_per_store)
# Find the maximum average sales value
max_average_sales = average_sales_per_store.max()
print('max average sales:', max_average_sales)

# this eauivalence is weird yes. This line compares each element in the average_sales_per_store Series with the single value max_average_sales. The comparison is done element-wise, resulting in a Boolean Series. This Boolean Series will have True for stores whose average sales are equal to max_average_sales.
print('wierd equal \n', average_sales_per_store == max_average_sales)
# Get all stores with average sales equal to the max average sales This Series (average_sales_per_store) can be compared with a single number (like max_average_sales), which will perform an element-wise comparison and return a Boolean Series. In this Boolean Series, True indicates that the store's average sales equal the maximum average sales value.
stores_with_highest_sales = average_sales_per_store[average_sales_per_store == max_average_sales].index.tolist()
print('stores with highest sales: \n', stores_with_highest_sales)

# Filter the DataFrame for those stores
filtered_data = df[df['Store'].isin(stores_with_highest_sales)]
print('filetered_data', filtered_data)


# another way:
# Calculate average sales per store
average_sales_per_store = df.groupby('Store')['Total Sales'].mean()
# Find the store with the highest average sales
store_with_highest_sales = average_sales_per_store.idxmax()
print('weird equal again: \n',df['Store'] == store_with_highest_sales)
# Filter the DataFrame for the store with the highest average sales
filtered_data = df[df['Store'] == store_with_highest_sales]
print('filetered_data', filtered_data)
