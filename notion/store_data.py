import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('store_data.csv')

df['Total Sales'] = df['Price'] * df['Quantity']
# Sum total sales by product and sort in descending order
top_products = df.groupby('Product')['Total Sales'].sum().sort_values(ascending=False).head(3)
print('top products: \n', top_products)

# Calculate average sales per store
average_sales_per_store = df.groupby('Store')['Total Sales'].mean()
print('average_sales_per_store: ', average_sales_per_store)
# Find the maximum average sales value
max_average_sales = average_sales_per_store.max()
print('max average sales:', max_average_sales)

# Get all stores with average sales equal to the max average sales
stores_with_highest_sales = average_sales_per_store[average_sales_per_store == max_average_sales]   #.index.tolist()
print('stores with highest sales: ', stores_with_highest_sales)

# Filter the DataFrame for those stores
filtered_data = df[df['Store'].isin(stores_with_highest_sales)]
print('filetered_data', filtered_data)


# Calculate average sales per store
average_sales_per_store = df.groupby('Store')['Total Sales'].mean()
# Find the store with the highest average sales
store_with_highest_sales = average_sales_per_store.idxmax()

# Filter the DataFrame for the store with the highest average sales
filtered_data = df[df['Store'] == store_with_highest_sales]
