1. convert string datetime to usable datetime
```
data      name    country  population  area  elevation timezone                            gps_coordinates  average_temperature  transit_trips_per_capita  car_ownership_rate              founded
0   CityA   Country1     1000000   500        100    UTC+1                            [52.52, 13.405]            10.000000                       100            0.500000  1806-01-01T00:00:00
1   CityB   Country2     2000000   600        200    UTC+2                          [48.8566, 2.3522]            12.000000                       110            0.600000  1330-01-01T00:00:00
2   CityC   Country3     3000000   700        300    UTC+3                         [40.7128, -74.006]            14.000000                       120            0.700000  1961-01-01T00:00:00
3   CityD   Country4     4000000   800        400    UTC-1                         [51.5074, -0.1278]            16.000000                       130            0.800000  1657-01-01T00:00:00
```

and pandas code:

```python3
def convert(date):
    year, month, day = [int(date_piece) for date_piece in date.split('T')[0].split('-')]
    return pd.Period(year=year, month=month, day=day, freq='D')

data['founded'] = data['founded'].apply(convert)
before_1900 = data[data['founded'].dt.year < 1900]
```

2. import json

```python3
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

data = pd.read_json('sample_data.json', lines=True)
print('data', data)
```
