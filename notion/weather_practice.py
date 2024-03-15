import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


data = pd.read_csv('weather.csv')
print('data', data)

# 1. max rainfall each date
data['Year'] = data['Date'].apply(lambda x: int(x.split('-')[0]))
data['Month'] = data['Date'].apply(lambda x: int(x.split('-')[1]))
data['Day'] = data['Date'].apply(lambda x: int(x.split('-')[2]))

print('data', data)
new_data = data.groupby(['Year', 'Month', 'Day'])['Rainfall'].max()
print('new_data max \n', new_data)

# 2. max rainfall each station
new_data = data.groupby('StationID')['Rainfall'].max()
print('new data station max: ', new_data)

# 3. average rainfall
avg_rainfall = data['Rainfall'].mean().round(3)
print('avg rainfall: ', avg_rainfall)

# 4. lowest humidity before or on jan 2
# filtered_data = data.query('Month == 1 and Day <= 2')
filtered_data = data[(data['Month'] == 1) & (data['Day'] <= 2)]
print('filtered data: ', filtered_data)
min = filtered_data['Humidity'].min()
print('min: ', min)

#5. which day did each statino record teh highest temp
max_temps = data.loc[data.groupby('StationID')['Temperature'].idxmax(), ['StationID', 'Date', 'Temperature']]
print('max temps\n ', max_temps)


# 6 means for all columns and group by station
averages = data.groupby('StationID')[['WindSpeed', 'Rainfall']].mean().round(3)
print('all averages', averages)
