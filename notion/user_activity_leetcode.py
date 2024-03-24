import pandas as pd


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
  print('activity\n', activity)
  activity['activity_date'] = pd.to_datetime(activity['activity_date'])
  past_30_days = activity[
    (activity.activity_date > pd.to_datetime('2019-07-27') - pd.to_timedelta('30days')) &
    (activity.activity_date <= pd.to_datetime('2019-07-27'))
  ]
  print('past_30_days\n', past_30_days)
  '''
  This code snippet returns a DataFrame. When you use .agg() and pass a dictionary, pandas always returns a DataFrame because it assumes that you might be aggregating multiple columns with potentially different functions. Each key in the dictionary will become a column in the resulting DataFrame. Even if you aggregate only a single column, the result will still be a DataFrame, and the column names will be preserved or will be set according to the keys you've provided in the dictionary.
  '''
  grouped_df = past_30_days.groupby('activity_date').agg({'user_id': pd.Series.nunique})
  '''
  If you only need the result as a Series and you are doing a single aggregation operation, you can call the aggregation function directly (like .nunique()). If later you need it as a DataFrame, you can call .reset_index() to convert the Series to a DataFrame.
  '''
  print('grouped_df\n', grouped_df)
  '''
  The grouped_df DataFrame will have activity_date as the index and a single column containing the count of unique user IDs. To turn activity_date back into a regular column and to be able to rename the columns, you will indeed need to use .reset_index(), like so
  '''
  activity_users_per_day = grouped_df.reset_index()
  activity_users_per_day.columns = ['day', 'active_users']
  return activity_users_per_day
  # past_30_days = activity[
  #   (activity.activity_date <= pd.to_datetime('2019-07-27', format='%Y-%m-%d')) &
  #   (activity.activity_date > pd.to_datetime('2019-07-27', format='%Y-%m-%d') - pd.to_timedelta("30day"))
  # ]
  # print('past_30_days \n', past_30_days)
  # grouped_df = past_30_days.groupby('activity_date')['user_id'].nunique()
  # print('grouped_df \n', grouped_df)
  # # Reset the index so activity_date is a column, not the index
  # active_users_per_day = grouped_df.reset_index()
  # # Rename columns to match expected output
  # active_users_per_day.columns = ['day', 'active_users']
  # return active_users_per_day


test_data = {
    'user_id': [1, 1, 1, 2, 2, 2],
    'session_id': [1, 1, 1, 4, 4, 4],
    'activity_date': [
        '2019-07-20', '2019-07-20', '2019-07-20',
        '2019-07-20', '2019-07-21', '2019-07-21'
    ],
    'activity_type': [
        'open_session', 'scroll_down', 'end_session',
        'open_session', 'send_message', 'end_session'
    ]
}
user_activity(pd.DataFrame(test_data))
