import pandas as pd

# Set display options
pd.set_option('display.max_columns', None)  # No column limit
pd.set_option('display.max_rows', None)  # No row limit
pd.set_option('display.width', None)  # Auto-detect the display width

df = pd.read_json('sample_data.json', lines=True)
print("original data frame:\n", df)
'''
Practice Questions
Find the top 3 cities with the highest population.
Calculate the average car ownership rate for all cities.
Identify the city with the highest elevation and report its name, country, and elevation.


Methods:
df['timestamp'] = pd.to_datetime(df['timestamp']) to convert string to datetime
df.sort_values + head(3)
df = df[df['founded'] < pd.Timestamp('1800-01-01')]  to make new dataframe with only rows where founded is before 1800

to groupby and sort and take top 5:
new_df = df.groupby(by=df['ProductID'], as_index=False)['Total_Rev'].sum()
top_products = new_df.sort_values(by='Total_Rev', ascending=False).head(5)

- to convert to timestamp periods
def convert(date):
    year, month, day = [int(date_piece) for date_piece in date.split('T')[0].split('-')]
    return pd.Period(year=year, month=month, day=day, freq='D')

data['founded'] = data['founded'].apply(convert)
before_1900 = data[data['founded'].dt.year < 1900]

- drop dupes
If you want to remove duplicates based on specific columns, you can pass the column names as a list to the subset parameter:
df = df.drop_duplicates(subset=['column1', 'column2'])
Additionally, you can control which duplicates to keep:
first: (default) Drop duplicates except for the first occurrence.
last: Drop duplicates except for the last occurrence.
False: Drop all duplicates.
Here’s an example of keeping only the last occurrence:
df = df.drop_duplicates(subset=['column1', 'column2'], keep='last')
After removing duplicates, the DataFrame's index may be disordered or have gaps, you can reset the index if necessary:
df = df.reset_index(drop=True)

- filter last 30 days of data
past_30_days = activity[activity.activity_date > pd.to_datetime('2019-08-16', format='%Y-%m-%d') - pd.to_timedelta("30day")]

'''

# 1. Find the top 3 cities with the highest population.
top_3_populated_cities_df = df.sort_values(by='population', ascending=False).head(3)
print("Top 3 cities with the highest population:\n", top_3_populated_cities_df[['name', 'population']])

# 2. Calculate the average car ownership rate for all cities.
average_car_ownership_rate = df['car_ownership_rate'].round(3).mean()
print(f"Average car ownership rate for all cities: {average_car_ownership_rate}")

# 3. Identify the city with the highest elevation and report its name, country, and elevation.
print(f"index of city with highest elevation:", df['elevation'].idxmax())
highest_elevation_city = df.loc[df['elevation'].idxmax(), ['name', 'elevation', 'country']]
print("City with the highest elevation:")
print(f"Name: {highest_elevation_city['name']}, Country: {highest_elevation_city['country']}, Elevation: {highest_elevation_city['elevation']}")

#4. identify country with longest name
country_with_longest_name = df['country']
print(f"country with longest_name", country_with_longest_name.max())

#5. shortest car ownership
lowest_car_ownership_country = df.loc[df['car_ownership_rate'].idxmin(), 'country']
print(f"Country with the lowest car ownership rate: {lowest_car_ownership_country}")

#6. average population of all cities
avg_pop_all_cities = df['population'].mean()
print(f"avg_pop_all_cities: {avg_pop_all_cities}")

#7. How many cities founded before 1500
df['founded_year'] = df['founded'].str.slice(0,4).astype(int)
print('df for founded_year', df['founded_year'])
# Count how many cities were founded before the year 1500
'''The shape attribute of a pandas DataFrame returns a tuple representing its dimensions, specifically the number of rows and columns.
For example, if you have a DataFrame named df, df.shape will return a tuple (n_rows, n_columns), where n_rows is the number of rows and n_columns is the number of columns in the DataFrame.
In your case, df.shape returning (11, 12) indicates that your DataFrame has 11 rows and 12 columns. This means you have 11 records (or observations) and 12 features (or variables) in your dataset.
'''
cities_founded_before_1500 = df[df['founded_year'] < 1500].shape[0]
print(f"Cities founded before the year 1500: {cities_founded_before_1500}")

#8. correlation between population size and ownership rate
correlation = df['population'].corr(df['car_ownership_rate'])
print(f"Correlation between population size and car ownership rate: {correlation}")

# 9. transform each element in gps coordinates to 3 precision
def round_coordinates(coord):
    print("coord", coord)
    return [round(c, 3) for c in coord]

df['gps_coordinates'] = df['gps_coordinates'].apply(round_coordinates)
print(f"rounded to 3 decimal places: {df['gps_coordinates']}")

# 10. find city name and country with highest average temperate
city_with_highest_temp = df.loc[df['average_temperature'].idxmax()]
print('city with highest temp: ', city_with_highest_temp['name'], city_with_highest_temp['country'])

#11. find city name and country with lowest transit tripcs per capita
city_with_lowest_transit_trips = df.loc[df['transit_trips_per_capita'].idxmin()]
print(f"city with lowest transit trips", city_with_lowest_transit_trips['name'], city_with_lowest_transit_trips['country'], city_with_lowest_transit_trips['transit_trips_per_capita'])

#12. highest car ownership rate but in percentage format

# # 13. how many cities were founded after 1800?
# df['founded'] = df['founded'].apply(lambda x: x if '1677' <= x <= '2262' else pd.NaT)
# # Convert 'founded' column to datetime format
# df['founded'] = pd.to_datetime(df['founded'])
#
# # Extract year and month
# df['year'] = df['founded'].dt.year
# df['month'] = df['founded'].dt.month
#
# # Filter the DataFrame for cities founded after 1800
# filtered_df = df[df['year'] > 1800]
# print(f"cities_founded_after_1800: {filtered_df['name'].shape[0]}")

# 14. how many cities were founded before 1800? This is interesting because pands can't handle certain rows before 1677 should be 14 cities
df['founded'] = pd.to_datetime(df['founded'], errors='coerce')
# Filter cities founded before 1800
print('df founded using errors coerce', df['founded'])

# the outer df will only return rows that are True
# the inner comparison:
# The expression df['founded'] < pd.Timestamp('1800-01-01') is performing a comparison between each value in the "founded" column of your DataFrame (df['founded']) and the specified timestamp pd.Timestamp('1800-01-01').
# Each comparison evaluates whether the date in the "founded" column is before January 1, 1800. The result is a boolean Series where True indicates that the date is before 1800, and False indicates that it is not.
# In your output, True values indicate that the date in the corresponding row is before January 1, 1800, while False values indicate that it is not. It appears that only one row (index 17) has a date before 1800 in your DataFrame.
# If you want to retrieve the entire row(s) where the condition df['founded'] < pd.Timestamp('1800-01-01') evaluates to True, you can use boolean indexing. That's what the outer df is doing
cities_before_1800 = df[df['founded'] < pd.Timestamp('1800-01-01')]
print('cities before 1800', cities_before_1800)

# Filter cities with NaT values (i.e., invalid datetime strings)
na_values = df['founded'].isna()
print("na_values", na_values.sum())
# Count the number of cities founded before 1800
num_cities_before_1800 = len(cities_before_1800) + na_values.sum()

print("Number of cities founded before 1800:", num_cities_before_1800)


# when you use the sum() function on a boolean series in pandas, it counts the number of True values, treating True as 1 and False as 0. So, it effectively counts the number of occurrences where the condition is True.
# 15. How many cities have an area under 1000?

area_under_1000 = df['area'] < 1000
print("area udner 1000", area_under_1000.sum())


