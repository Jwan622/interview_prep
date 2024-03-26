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

data = pd.read_json('pandas_data/sample_data.json', lines=True)
print('data', data)
```


3. modify using loc
Use loc to modify the original DataFrame directly, if that's what you intend. This makes it clear that you are modifying the original DataFrame:
```
df.loc[df['Column'] > value, 'NewColumn'] = some_value
```


4. top 5 users by action sorted
```python3
grouped_by = df.groupby(['user_id']).agg(action_count=("action", 'count'))
print('grouped_by \n', grouped_by)

top_5_active_users = grouped_by.sort_values(by="action_count", ascending=False).head(5)
print('top_5_active_users \n', top_5_active_users)
```

5. ignoring erros in a column and just getting the numeric values:

```python3
df['amounts'] = pd.to_numeric(df['amounts'], errors='coerce')
sum = df['amounts'].sum()
```

6. fill in missing values with NaN then 0
```python3
# Problem 1: Filling missing 'amount' with 0 after converting a column to numeric
# Replace non-numeric values with NaN, then fill NaN with 0
df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0)
```

6.5. Fill in missing values with median of that year.

```python3
df.fillna({'Year' : df['Year'].median()}, inplace=True)
```

7. drop rows where value is missing

```python3
# Problem 2: Dropping rows where 'country' is missing
df_cleaned = df.dropna(subset=['country'])
```

8. drop row where 2 values are missing with thres

how: Determines if a row or column is dropped when there are missing values.
how='any' (default): Drop the row/column if any value is NaN.
how='all': Drop the row/column only if all values are NaN.
thresh: Specifies a minimum number of non-missing values required to keep a row/column. For example, thresh=3 means a row/column needs at least three non-missing values to be retained.
subset: Allows you to specify a subset of columns or rows to consider when dropping. For instance, dropna(subset=['col1', 'col2']) will only consider col1 and col2 when determining which rows to drop.

```python3
df_dropped = df.dropna(thresh=2)
```

9. convert a column of mix types to numeric and then int

```python3
df['Year'] = pd.to_numeric(df['Year']).astype(int)
```
