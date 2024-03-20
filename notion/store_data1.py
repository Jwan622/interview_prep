import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

df = pd.read_csv('store_data.csv')
df['Total_Revenue'] = df['Price'] * df['Quantity']
df['Date'] = pd.to_datetime(df['Date'])
print('df should have date', df)
df_over_2000 = df[df['Date'].dt.year > 2000]
print('df over 2000 \n', df_over_2000)


grouped_df = df_over_2000.groupby(by=['Store', 'Product']).agg({'Total_Revenue': 'sum'})
print('grouped_df: \n', grouped_df)
sorted_df = grouped_df.sort_values(by=['Store', 'Total_Revenue'], ascending=[True, False])
print('sorted_df: \n', sorted_df)

# top revenue widget per store
top_revenue_per_store = sorted_df.groupby('Store').head(1)
print('top revenue per store: \n', top_revenue_per_store)
