import pandas as pd

# def find_manager_employees(employee: pd.DataFrame) -> pd.DataFrame:
  # managers_employee_count_id = employee.groupby('managerId').agg({'id': 'count'}).reset_index()['managerId']
  # print('managers_employee_count\n' ,managers_employee_count_id)
  # relevant_employees = employee[employee['id'].isin(managers_employee_count_id)]
  # print('relevant_employees \n', relevant_employees)
  # return relevant_employees.name

def find_manager_employees(employee: pd.DataFrame) -> pd.DataFrame:
  # Group by 'managerId' and count the number of employees for each manager
  managers_employee_count = employee.groupby('managerId').agg({'id': 'count'}).rename(columns={'id': 'employee_count'})
  print('managers employee with count \n', managers_employee_count)
  # Find managers with more than 5 employees
  managers_with_more_than_five = managers_employee_count[managers_employee_count['employee_count'] >= 5]
  print('managers with more than 5\n', managers_with_more_than_five)

  # Join to get the names of the managers
  """
  Column or index level name(s) in the caller to join on the index in other, otherwise joins index-on-index.
  This joins the managers_with_more_than_five DataFrame with the modified employee DataFrame on the managerId column. The on parameter specifies the column in the calling DataFrame (managers_with_more_than_five) that should be aligned with the index of the DataFrame being joined (employee.set_index('id')).
  """
  relevant_employees = managers_with_more_than_five.join(employee.set_index('id'), on='managerId')
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
