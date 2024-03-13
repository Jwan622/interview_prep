import pandas as pd

# Set display options
pd.set_option('display.max_columns', None)  # No column limit
pd.set_option('display.max_rows', None)  # No row limit
pd.set_option('display.width', None)  # Auto-detect the display width

df = pd.read_json('sample_data.json', lines=True)

print(df)

'''
Practice Questions
Find the top 3 cities with the highest population.
Calculate the average car ownership rate for all cities.
Identify the city with the highest elevation and report its name, country, and elevation.
'''

# 1. Find the top 3 cities with the highest population.
top_3_populated_cities = df.sort_values(by='population', ascending=False).head(3)
print("Top 3 cities with the highest population:")
print(top_3_populated_cities[['name', 'population']])

# 2. Calculate the average car ownership rate for all cities.
average_car_ownership_rate = df['car_ownership_rate'].mean()
print(f"Average car ownership rate for all cities: {average_car_ownership_rate:.2f}")

# 3. Identify the city with the highest elevation and report its name, country, and elevation.
highest_elevation_city = df.loc[df['elevation'].idxmax()]
print("City with the highest elevation:")
print(f"index of city with highest elevation:", df['elevation'].idxmax())
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

# Define a function to round each coordinate to 3 decimal points
def round_coordinates(coord):
    print("coord", coord)
    return [round(c, 3) for c in coord]

df['gps_coordinates'] = df['gps_coordinates'].apply(round_coordinates)
print(f"rounded to 3 decimal places: {df['gps_coordinates']}")
