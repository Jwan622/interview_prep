import pandas as pd

# Sample DataFrame with temperatures in Celsius
df = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Temperature_C': [22, 28, 16]
})

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(x):
    return x * 9/5 + 32

df['Temperature_C'] = df['Temperature_C'].apply(celsius_to_fahrenheit)
print('df: \n', df)



# usage of apply and axis=1
df = pd.DataFrame({
    'Item': ['Book', 'Pen', 'Pencil'],
    'Quantity': [3, 10, 5],
    'Unit_Price': [15, 1.5, 0.8]
})

# Function to calculate total price
df['Total_Price'] = df.apply(lambda x: x['Quantity'] * x['Unit_Price'], axis=1)


print('total price \n', df['Total_Price'])
