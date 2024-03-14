import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_csv('sales_data.csv')
print('original df \n', df)

# 1. monthly revenue
df['Date'] = pd.to_datetime(df['Date'])
df['Total_Rev'] = df['UnitPrice'] * df['Quantity']
new_df = df.groupby(by=df['Date'].dt.month)['Total_Rev'].sum()
print('grouped and summed df \n', new_df)

# 1.5

# Assuming df is already loaded
df.set_index('Date', inplace=True)  # Set the datetime column as the index

# Use resample to sum monthly revenue
monthly_revenue = df['Total_Rev'].resample('M').sum().sort_values(ascending=False)
print('Monthly Revenue with Resample:\n', monthly_revenue)


# 2. top grossing products
new_df = df.groupby(by=df['ProductID'])['Total_Rev'].sum()

# Sort the revenues in descending order and get the top 5
top_products = new_df.sort_values(ascending=False).head(5)

print('Top Grossing Products:\n', top_products)


