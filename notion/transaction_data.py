import pandas as pd
'''
Which company has the most revenue overall?
Which are the top 2 grossing revenue companies in each country?
'''

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

df = pd.read_csv('pandas_data/transaction_data.csv')
print('df, ', df)


grouped_by_country_and_company = df.groupby(['country', 'company'])['amount'].sum()
print('grouped_by_country_and_company: ', grouped_by_country_and_company)

# top 2 companies in each country

sorted = grouped_by_country_and_company.reset_index().sort_values(['country', 'amount'], ascending=[True, False])
print('sorted : \n', sorted)
top_companies = sorted.groupby('country').head(2)
print('toip_companies: \n', top_companies)
