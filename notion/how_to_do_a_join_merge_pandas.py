import pandas as pd

# def find_manager_employees(employee: pd.DataFrame) -> pd.DataFrame:
  # managers_employee_count_id = employee.groupby('managerId').agg({'id': 'count'}).reset_index()['managerId']
  # print('managers_employee_count\n' ,managers_employee_count_id)
  # relevant_employees = employee[employee['id'].isin(managers_employee_count_id)]
  # print('relevant_employees \n', relevant_employees)
  # return relevant_employees.name


"""
In pandas, using single brackets [] when selecting columns from a DataFrame will return a pandas Series, while double brackets [[]] will return a DataFrame. Here's a quick explanation:

Single Bracket ([]):

When you use single brackets with a single column label, pandas returns a Series representing that column.
For example: df['column_name'] returns a Series.
Double Brackets ([[]]):

When you use double brackets, you're passing a list of column labels, and pandas returns a DataFrame that contains just the specified columns.
Even if the list contains a single column label, you get a DataFrame: df[['column_name']] returns a DataFrame.
"""
def find_manager_employees(employee: pd.DataFrame) -> pd.DataFrame:
  # Group by 'managerId' and count the number of employees for each manager
  managers_employee_count = employee.groupby('managerId').agg({'id': 'count'}).rename(columns={'id': 'employee_count'})
  print('managers employee with count \n', managers_employee_count)
  # Find managers with more than 5 employees using boolean indexing
  managers_with_more_than_five = managers_employee_count[managers_employee_count['employee_count'] >= 5]
  print('managers with more than 5\n', managers_with_more_than_five)

  # Join to get the names of the managers
  """
  Column or index level name(s) in the caller to join on the index in other, otherwise joins index-on-index.
  This joins the managers_with_more_than_five DataFrame with the modified employee DataFrame on the managerId column. The on parameter specifies the column in the calling DataFrame (managers_with_more_than_five) that should be aligned with the index of the DataFrame being joined (employee.set_index('id')).
  """
  relevant_employees = managers_with_more_than_five.merge(employee, left_on='managerId', right_on='id', how='inner')
  # relevant_employees = managers_with_more_than_five.join(employee.set_index('id'), on='managerId', how='inner')
  print('relevant employees \n', relevant_employees)

  # Return the names of the relevant managers
  return relevant_employees['name']


employee_data = {
    "id": [101, 102, 103, 104, 105, 106],
    "name": ["John", "Dan", "James", "Amy", "Anne", "Ron"],
    "department": ["A", "A", "A", "A", "A", "B"],
    "managerId": [None, 101, 101, 101, 101, 101]
}
print(find_manager_employees(pd.DataFrame(employee_data)))

employee_data = {
    "id": [101, 102, 103, 104, 105, 106],
    "name": ["John", "Dan", "James", "Amy", "Anne", "Ron"],
    "department": ["A", "A", "A", "A", "A", "B"],
    "managerId": [None, 100, 100, 100, 100, 100] # no matching manager, so should return empty
}
print(find_manager_employees(pd.DataFrame(employee_data)))
