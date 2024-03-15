import pandas as pd

# Creating a DataFrame with a column containing non-numeric values
# data = {'amounts': ['0.123', 0.456, 'text'], 'items': ['apple', 'banana', 'orange']}
# df = pd.DataFrame(data)

# 1 sum up the amounts
# Convert 'column_name' to numeric, handling errors with 'coerce'. the sum() function in pandas will skip NaN (Not a Number) values by default. When you use pd.to_numeric with errors='coerce', it converts non-numeric values to NaN. When you call sum() on a column containing NaN values, it will compute the sum of only the numeric values, excluding the NaNs.
# df['amounts'] = pd.to_numeric(df['amounts'], errors='coerce')
# sum = df['amounts'].sum()
# print('sum: ', sum)
# print(f'sum percentage: {sum:.2%}')


# 2 find the highest priced fruit: should be banana
# highest_priced_fruit = df.loc[df['amounts'].idxmax()]
# print(f'highest_priced_fruit', highest_priced_fruit['items'])


# Creating a DataFrame
# data = {'column_name': [0.123, 0.456, 0.789]}
# df = pd.DataFrame(data)

# Incorrect usage, resulting in an AttributeError
# df = df.map('{:.2%}'.format)  # This line will raise an error

# Correct usage: Select the column and apply the .map method
# df['column_name'] = df['column_name'].map('{:.2%}'.format)
#
#
# # 3. show sums for each fruit
# data = {'amounts': ['60.50', 80.50, 'text', 100, 100, 200, 1], 'fruits': ['apple', 'apple', 'orange', 'banana', 'orange', 'strawberry', 'strawberry']}
# df = pd.DataFrame(data)
#
# df['amounts'] = pd.to_numeric(df['amounts'], errors='coerce')
# print('df amounts coerced', df['amounts'])
# new_df = df.groupby('fruits').sum()
# new_df = new_df.sort_values(by='amounts', ascending=False)
# print(new_df)
#
# 4. show sums for each user and product
# data = {'user': [1,1,1,1,1,2,2,2], 'product_id': [456, 87, 788, 456, 87, 456, 788, 456], 'amount': [1,1,3,5,2,1,3,5], 'some_other_column': [3,3,3,4,3,3,3,3]}
# df = pd.DataFrame(data)
'''
What reset_index Does: The reset_index function is used to reset the index of the DataFrame. When you specify level=0, it resets the first level of the index (user in this case) back to a column in the DataFrame, leaving any remaining levels (in this case, just product_id) as the index.

Effect on the DataFrame: By calling reset_index(level=0), you effectively move the user level of the index back into the DataFrame as a standard column. This operation leaves product_id as the index, changing the DataFrame's structure. Now, each row is uniquely identified by product_id, and user appears as a regular column alongside amount.

Without reset_index: The DataFrame maintains its hierarchical index, with both user and product_id serving as row identifiers.
With reset_index(level=0): The user field is "demoted" from being part of the index to being a regular column, leaving product_id as the sole index.

If you want to sort the grouped data by both user and amount, you should ensure that the result of the groupby operation is a DataFrame, which allows specifying columns in sort_values. You can achieve this by not selecting a single column (['amount']) to sum, thus keeping the result as a DataFrame with multiple columns. Here's how you can adjust your code:

as_index=False in the groupby method call ensures that the grouping keys (user, product_id) are not set as the index, which keeps the result as a DataFrame. you can also use reset_index which also eliminates teh index
'''
# new_df = df.groupby(['user', 'product_id'], as_index=False).sum()
# new_df = df.groupby(['user', 'product_id']).sum().reset_index()
# new_df = df.groupby(['user', 'product_id']).sum() // this is without reset -index
# print('new_df with new index and reset index \n', new_df)
# new_df = new_df.sort_values(by=['user', 'amount'], ascending=[True, False])
# print('newdf \n', new_df[['user', 'amount']])



# 5. top 3 companies in each country by amount sold
data = {
    'companies': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D'],
    'countries': ['US', 'China', 'Spain', 'US', 'China', 'Spain', 'France', 'Canada', 'US', 'US', 'China', 'France', 'Canada', 'US', 'US', 'China'],
    'amount': [1,1,3,5,2,1,3,5,1,1,3,5,2,1,3,5]
}

df = pd.DataFrame(data)
grouped_df = df.groupby(['countries', 'companies']).sum()
print('grouped df \n', grouped_df)

# Sort each group within each country by the summed amount in descending order
'''
After the initial grouping and summation, you have a DataFrame (grouped_df) indexed by two levels: countries and companies. The goal is to sort companies within each country by their summed amount. To achieve this, we need to "act" on each country's subset individually so we need to group again. By grouping by countries again, we instruct Pandas to apply the subsequent operation (apply) within each country's subset independently, allowing for per-country sorting.

In summary, the reason for the additional groupby is to achieve a sort operation within each country's group while maintaining the structure of your DataFrame, especially its hierarchical index. This approach allows for a fine-grained sorting operation that respects your data's hierarchical nature, providing sorted lists of companies within each country based on their summed amount.

apply can be used on both Series and DataFrame objects. When used on a DataFrame, apply allows you to apply a function along an axis of the DataFrame (rows or columns). It does not inherently add an additional index; instead, the changes to the index depend on the function you apply and how you're applying it.
'''
# sorted_df = grouped_df.groupby('countries', as_index=False).apply(lambda x: x.sort_values(by='amount', ascending=False))
# print('sorted_df \n', sorted_df)
# final = sorted_df.groupby('countries').head(3)
# print('final \n', final)

# or this... which I think actually makes more sense to me:
sorted_df = grouped_df.reset_index().sort_values(by=['countries', 'amount'], ascending=[True, False])
print('sorted_df \n', sorted_df)
top_companies = sorted_df.groupby('countries').head(3)
print('top companies \n', top_companies)
# If you only want to show the countries and companies in the final DataFrame
final_df = top_companies[['countries', 'companies']]
print('final df:\n', final_df)
