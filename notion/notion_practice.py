"""
Read and preprocess the data, ensuring timestamp is appropriately handled as a datetime object.
Perform the analysis as specified in the problem statement, using pandas to manipulate and analyze the data.
Provide insights and summaries based on the analysis.

Your task is to analyze the document interactions to identify the most engaged users and the popularity of documents based on user actions. Specifically, you need to:

Calculate the total number of actions each user has performed and identify the top 5 most active users.
For each type of action (created, viewed, edited, shared), find the top 3 most frequently interacted documents.
Determine the hour of the day when users are most active on the platform. Assume the timestamp is in the local time zone of the users.
"""

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option("display.max_rows", None)
pd.set_option('display.width', None)

df = pd.read_csv("pandas_data/notion_practice.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

#1.  number of actions user has performed
grouped_by = df.groupby(['user_id']).agg(action_count=("action", 'count'))
print('grouped_by \n', grouped_by)
print('grouped_by type', type(grouped_by))
top_5_active_users = grouped_by.sort_values(by="action_count", ascending=False).head(5)
print('top_5_active_users \n', top_5_active_users)

#2 for each type action, find top 3 more frequently interacted documents
just_viewed_actions = df[df['action'] == 'viewed']
print('just viewed \n', len(just_viewed_actions))
doc_grouped_by = df.groupby(['action', 'document_id']).agg(document_count=('document_id', 'count'))
print('doc_grouped_by', doc_grouped_by)
doc_sorted_by = doc_grouped_by.sort_values(by=['action', 'document_count'], ascending=[True, False])
print('doc sorted by\n', doc_sorted_by)
top_documents = doc_sorted_by.groupby('action').head(3)
print('top_documents \n', top_documents)
