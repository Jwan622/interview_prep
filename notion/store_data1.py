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

# When you use .agg({'Total_Revenue': 'sum'}), it explicitly instructs pandas to apply the sum function to the 'Total_Revenue' column, resulting in a DataFrame where 'Total_Revenue' is the sum of revenues for each 'Store' and 'Product' group. This keeps the 'Store' and 'Product' columns in the resulting DataFrame, which allows for further sorting and grouping operations.
# USE agg instead of sum
# On the other hand, when you directly use .sum() on a grouped DataFrame, it will compute the sum of all numeric columns for each group. If 'Store' and 'Product' are the grouping variables, they will not be columns in the resulting DataFrame but instead will be part of the index, which changes how you need to handle the resulting DataFrame.
# When you use .sum() directly after grouping, the result is a Series, not a DataFrame. In your case, grouped_df becomes a Series with a MultiIndex consisting of 'Store' and 'Product', and the values are the summed 'Total_Revenue'. This Series structure is why you encounter the error when trying to use sort_values with the by argument, which is not applicable to Series objects.
#
# Here's the difference:
#
# With agg(), the result is a DataFrame, which can have multiple columns and allows sorting with the by argument in sort_values().
# With sum(), the result is a Series with a MultiIndex, and sort_values() on a Series does not require the by argument because there's only one column of data to sort.
# If you need to sort by 'Store' and then by 'Total_Revenue', you should ensure grouped_df remains a DataFrame. You could maintain the DataFrame structure by using .agg() or by resetting the index after summing:
# grouped_df = df_over_2000.groupby(by=['Store', 'Product']).sum().reset_index()
# sorted_df = grouped_df.sort_values(by=['Store', 'Total_Revenue'], ascending=[True, False])
# In this version, after summing, reset_index() is used to convert the MultiIndex into regular columns, allowing for sorting by multiple columns in sorted_df.
grouped_df = df_over_2000.groupby(by=['Store', 'Product']).agg({'Total_Revenue': 'sum'})
print('grouped_df: \n', grouped_df)
print('type of grouped_df', type(grouped_df))
sorted_df = grouped_df.sort_values(by=['Store', 'Total_Revenue'], ascending=[True, False])
print('sorted_df: \n', sorted_df)

# top revenue widget per store
top_revenue_per_store = sorted_df.groupby('Store').head(1)
print('top revenue per store: \n', top_revenue_per_store)
