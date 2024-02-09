# You're given a log file of web server data in the format "UserID, Timestamp, Action". Write a function that parses this log file and returns the number of unique users who performed a specific action.
#
# Example Input:
#
# makefile
# Copy code
# logs = [
#     "123, 2021-03-01 14:20:00, LOGIN",
#     "124, 2021-03-01 14:35:00, LOGIN",
#     "123, 2021-03-01 15:00:00, LOGOUT",
#     "125, 2021-03-01 15:15:00, LOGIN",
#     "124, 2021-03-01 15:15:00, LOGOUT",
#     "123, 2021-03-01 15:20:00, LOGIN"
# ]
# action = "LOGIN"
# Example Output:
#
# Copy code
# 3

def parse_logs(logs, action):
    unique_users = []
    for log in logs:
        user_id, timestamp, parsed_action = log.split(',')
        if parsed_action.lstrip() == action:
            if user_id not in unique_users:
                unique_users.append(user_id)

    return len(unique_users)



logs = [
    "123, 2021-03-01 14:20:00, LOGIN", # notice the white space on the left here
    "124, 2021-03-01 14:35:00, LOGIN",
    "123, 2021-03-01 15:00:00, LOGOUT",
    "125, 2021-03-01 15:15:00, LOGIN",
    "124, 2021-03-01 15:15:00, LOGOUT",
    "123, 2021-03-01 15:20:00, LOGIN"
]
action = "LOGIN"
assert parse_logs(logs, action) == 3, "simple test 1 did not pass"


logs1 = [
    "123, 2021-03-01 14:20:00, LOGIN", # notice the white space on the left here
    "124, 2021-03-01 14:35:00, LOGIN",
    "123, 2021-03-01 15:00:00, LOGOUT",
    "125, 2021-03-01 15:15:00, LOGIN",
    "124, 2021-03-01 15:15:00, LOGOUT",
    "123, 2021-03-01 15:20:00, LOGIN"
]
action1 = "LOGOUT"
assert parse_logs(logs1, action1) == 2, "simple test 2 did not pass"



