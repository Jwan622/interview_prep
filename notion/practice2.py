import pandas as pd

# 1. only for orders before 2000, apply coupon discounts to prices, and only for vege and fruit. sum up the cart.
# Creating a sample DataFrame
data = {
    'Product': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'Type': ['Fruit', 'Fruit', 'Fruit', 'Vege', 'Vege', 'Meat', 'Meat'],
    'Price': [1500.25, 2300.50, 1800.75, 1000.00, 2000.00, 3000.00, 10],
    'Discount': [0.05, 0.10, 0.15, 0.10, 0.5, 0.25, 0.25],
    'timestamp': ['1999-01-01T00:00:00', '1867-01-01T00:00:00', '1998-01-01T00:00:00', '1997-01-01T00:00:00', '1988-01-01T00:00:00', '2001-01-01T00:00:00', '1999-01-01T00:00:00']
}

df = pd.DataFrame(data)
print("Original DataFrame:", df)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df[df['timestamp'].dt.year < 2000]


df['discounted_dollars'] = df.apply(lambda x: x['Price'] * x['Discount'] if x['Type'] in ['Fruit', 'Vege'] else 0, axis=1).round(2)
df['discounted_price'] = df['Price'] - df['discounted_dollars'].round(2)
total_cart = df['discounted_price'].sum()
print("new df \n", df)
print("Total cart:", total_cart)
