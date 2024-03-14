import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

df = pd.read_csv('sales_data.csv')
print('original df \n', df)

# 1. monthly revenue
df['Date'] = pd.to_datetime(df['Date'])
df['Total_Rev'] = df['UnitPrice'] * df['Quantity']
df['Month'] = df['Date'].dt.month
new_df = df.groupby('Month')['Total_Rev'].sum()
print('grouped and summed df \n', new_df)

# 1.5

# Assuming df is already loaded
'''
. When you use set_index('Date') to set the 'Date' column as the index and then apply the resample method on this datetime-indexed DataFrame, Pandas handles the time series data in chronological order. Here's why the line graph appears in order:

Datetime Index: Setting 'Date' as the index of your DataFrame and ensuring it's in datetime format means that Pandas recognizes the index as time series data. This datetime index allows Pandas to utilize time-based indexing and slicing, as well as specialized time series functionalities like resample.

Resampling: The resample method is specifically designed for time series data. When you resample the data by month (using 'M' or 'ME' for month end in resample('ME')), Pandas groups the data into time periods based on the datetime index. It then aggregates the data (with .sum() in this case) for each of these time periods.
'''
new_df = df.set_index('Date')  # Set the datetime column as the index
# Use resample to sum monthly revenue
monthly_revenue = new_df['Total_Rev'].resample('MS').sum()
print('Monthly Revenue with Resample:\n', monthly_revenue)
print('plotting: \n')
monthly_revenue.plot(kind='line', figsize=(10, 6))
plt.title('Monthly Revenue')
plt.ylabel('Revenue')
plt.xlabel('Month')
plt.show()

# 2. top grossing products
new_df = df.groupby(by=df['ProductID'], as_index=False)['Total_Rev'].sum()

# Sort the revenues in descending order and get the top 5
top_products = new_df.sort_values(by='Total_Rev', ascending=False).head(5)

print('Top Grossing Products:\n', top_products)

'''
Sorting Values Issue: The line final = grouped.sort_values(by=[df['Date'].dt.month, 'Total_Rev'], ascending=[True, False]) attempts to use df['Date'].dt.month in the sort_values method, which is incorrect. The by parameter of sort_values expects column names from the DataFrame on which it's called. Since df['Date'].dt.month is not a column name in grouped, this will cause an error. Instead, you should sort by the column names that exist in grouped after the groupby operation.
'''
# 3. max product each month

df['Month'] = df['Date'].dt.month
grouped = df.groupby(by=['Month', 'ProductID'])['Total_Rev'].sum().reset_index()
# now sort
sorted = grouped.sort_values(by=['Month', 'Total_Rev'], ascending=[True, False])
# Keep only the max product for each month
max_product_per_month = sorted.drop_duplicates(subset=['Month'], keep='first')
print('max_product_per_month: \n', max_product_per_month[['ProductID', 'Total_Rev']])

# 3. customer segmentation
new_df = df.groupby(['CustomerID'])['Total_Rev'].sum()
print('customer segmented revenue \n', new_df)
thresholds = new_df.quantile(q=[0.33, 0.66], interpolation='linear').tolist()
print('thresholds: \n', thresholds)
# Segment customers
customer_segments = pd.cut(new_df, bins=[-float('inf'), thresholds[0], thresholds[1], float('inf')], labels=['Low', 'Medium', 'High'])
print('customer segments: \n', customer_segments)
# Add customer segment to the original DataFrame
'''
The map function associates each CustomerID in the original DataFrame df with the spending segment determined earlier. This adds a new column to df that categorizes each transaction by the customer's spending segment.
'''
df['CustomerSegment'] = df['CustomerID'].map(customer_segments)
print('df with customer sgments', df)



# 4. highest category each month. For each category, find the month with the highest sales volume and the highest revenue.
# for each category suggest we're grouping by category

new_df = df.groupby(['Category', 'Month']).agg({'Quantity': 'sum', 'Total_Rev': 'sum'}).sort_values('Category', ascending=False)
print('new_df \n', new_df)

# Find the month with the highest sales volume and revenue for each category
highest_volume = new_df.loc[new_df.groupby('Category')['Quantity'].idxmax()]
highest_revenue = new_df.loc[new_df.groupby('Category')['Total_Rev'].idxmax()]

print("Month with Highest Sales Volume by Category:\n", highest_volume)
print("\nMonth with Highest Revenue by Category:\n", highest_revenue)
