import pandas as pd

# merge takes 2 dataframes and takes a strategy/how
def price_at_given_date():
  # Given data
    data = {
      'product_id': [1, 2, 1, 1, 2, 3],
      'new_price': [20, 50, 30, 35, 65, 20],
      'change_date': ['2019-08-14', '2019-08-14', '2019-08-15', '2019-08-16', '2019-08-17', '2019-08-18']
    }
  # Create DataFrame
    products = pd.DataFrame(data)

    products['change_date'] = pd.to_datetime(products.change_date)
    target_date = pd.to_datetime('2019-08-16')
    products_before_target = products[products['change_date'] <= target_date]
    products_before_target_sorted = products_before_target.sort_values(by=['product_id', 'change_date'], ascending=[True, False])
    print('products_before_target_sorted \n', products_before_target_sorted)
    # only keep the latest one
    # products_deduped = products_before_target_sorted.drop_duplicates(subset='product_id')
    # or
    idx = products_before_target_sorted.groupby('product_id')['change_date'].idxmax()
    print('idx: \n', idx)
    # Use 'loc' to select the rows with the index found
    products_deduped = products.loc[idx]
    # get all the product ids from the left side
    all_product_ids = pd.DataFrame({'product_id': products['product_id'].unique()})
    # use merge, it's a left merge so all products on the left show up, fill in nulls with 10
    final_prices = all_product_ids.merge(products_deduped[['product_id', 'new_price']], on='product_id', how='left').fillna(10)
    final_prices.rename(columns={'new_price': 'price'}, inplace=True)
    return final_prices
