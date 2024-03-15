import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

data = pd.read_json('sample_data.json', lines=True)
print('data', data)


# 1. get rows that were founded before 1900

# def func(x):
#     try:
#         return dt.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
#     except:
#         return pd.NaT
#
# df['founded'].apply(func)

# also data['founded_year'] = data['founded'].apply(lambda x: int(x.split('-')[0]))

def convert(date):
    year, month, day = [int(date_piece) for date_piece in date.split('T')[0].split('-')]
    return pd.Period(year=year, month=month, day=day, freq='D')

data['founded'] = data['founded'].apply(convert)
before_1900 = data[data['founded'].dt.year < 1900]
# Calculate the average temperature for these rows
average_temperature_before_1900 = before_1900['average_temperature'].mean()
print('average temperature before 1900', average_temperature_before_1900)



# 2. transform area by a factor of 10, for no reason
data['area_x10'] = data['area'].apply(lambda area: int(area) * 10)
print('data transformed x10: \n', data)


#3 max transit trips per capita
max = data['transit_trips_per_capita'].max()
print('max transit trips: ', max)
