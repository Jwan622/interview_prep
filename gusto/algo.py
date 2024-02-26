import urllib.request

SMALL_FILE_URL = 'https://gist.githubusercontent.com/bss/6dbc7d4d6d2860c7ecded3d21098076a/raw/244045d24337e342e35b85ec1924bca8425fce2e/sample.small.log'

# logs = urllib.request.urlopen(SMALL_FILE_URL).readlines()
# for row in logs[0:10]:
#     log = row.decode('ascii')
#     print(log)

"""
These are patterns that we care about
GET /api/users/{user_id}/count_pending_messages
GET /api/users/{user_id}/get_messages
GET /api/users/{user_id}/get_friends_progress
GET /api/users/{user_id}/get_friends_score
POST /api/users/{user_id}
GET /api/users/{user_id}

These are logs that return from the api, a sample:
2014-01-09T06:16:53.748849+00:00 heroku[router]: at=info method=POST path=/api/online/platforms/facebook_canvas/users/100002266342173/add_ticket host=mygame.heroku.com fwd="94.66.255.106" dyno=web.12 connect=12ms service=21ms status=200 bytes=78
connect + service = response_time =  12 + 21 = 33. This will be the response_time

2014-01-09T06:16:53.742892+00:00 heroku[router]: at=info method=GET path=/api/users/100002266342173/count_pending_messages host=mygame.heroku.com fwd="94.66.255.106" dyno=web.8 connect=9ms service=9ms status=304 bytes=0

2014-01-09T06:16:53.742892+00:00 heroku[router]: at=info method=GET path=/api/users/456643646346/count_pending_messages host=mygame.heroku.com fwd="94.66.255.106" dyno=web.8 connect=9ms service=9ms status=304 bytes=0

2014-01-09T06:16:53.766841+00:00 heroku[router]: at=info method=POST path=/logs/save_personal_data host=mygame.heroku.com fwd="5.13.87.91" dyno=web.10 connect=1ms service=42ms status=200 bytes=16

2014-01-09T06:16:53.772938+00:00 heroku[router]: at=info method=POST path=/api/users/100002844291023 host=mygame.heroku.com fwd="46.195.178.244" dyno=web.6 connect=2ms service=43ms status=200 bytes=52

2014-01-09T06:16:53.765430+00:00 heroku[router]: at=info method=GET path=/api/users/100005936523817/get_friends_progress host=mygame.heroku.com fwd="5.13.87.91" dyno=web.11 connect=1ms service=47ms status=200 bytes=7498


We want to return some data like this:
[{
  "request_identifier": "GET /api/users/{user_id}/count_pending_messages",
  "called": 3,
  "response_time_mean": 40.0,
}]
do not aggergate at the user level, aggregate on the pattenr level like this pattern: path=/api/online/platforms/facebook_canvas/users/100002266342173/add_ticket
"""



'''
# steps
- get all the logs for each identifier
- once we have all logs in a list, we can run analysis
- iterate through each log and start building a data structure to keep track of metrics
- [{
    "<method + path>": [15,20,50,40,56....]}
  }]
'''
def analyze_logs():
    logs = urllib.request.urlopen(SMALL_FILE_URL).readlines()
    print('logs: ', logs)

    aggregate_data = build_aggregate_data(logs)
    return prepare(aggregate_data)


def anonymize_path(path):
    splitted = path.split('/')
    for index, part in enumerate(splitted):
        if part == 'users':
            splitted[index + 1] = '{user_id}'
    thing_to_return ='/'.join(splitted)
    return thing_to_return


def is_relevant_log(method, path):
    things_we_care_about = [
        "GET /api/users/{user_id}/count_pending_messages",
        "GET /api/users/{user_id}/get_messages",
        "GET /api/users/{user_id}/get_friends_progress",
        "GET /api/users/{user_id}/get_friends_score",
        "POST /api/users/{user_id}",
        "GET /api/users/{user_id}"
    ]
    splitted_things_we_care_about = [method_and_path.split() for method_and_path in things_we_care_about]
    print('method: ', method)
    print('path: ', path)
    print('splitted_couplet: ', splitted_things_we_care_about)
    match = any(splitted_couplet[0] == method and splitted_couplet[1] == path for splitted_couplet in splitted_things_we_care_about)
    print('match: ', match)
    return match


def build_aggregate_data(logs):
    print(logs)
    aggregate_data = {}

    for log in logs:
        splitted = log.split()
        print('splitted: ', splitted)
        path = splitted[4].split('=')[1]
        path = anonymize_path(path)
        method = splitted[3].split('=')[1]
        if is_relevant_log(method, path) is False:
            print('insdie is relevant log: ', path)
            continue
        unique_key = method + ' ' + path

        connect = int(splitted[8].split('=')[1].replace('ms', ''))
        service = int(splitted[9].split('=')[1].replace('ms', ''))
        summed_up_time = connect + service
        print('path: ', path)
        print('method: ', method)
        print('unique key', unique_key)
        print('connect: ', connect)
        print('service: ', service)

        if unique_key in aggregate_data:
            aggregate_data[unique_key].append(summed_up_time)
        else:
            aggregate_data[unique_key] = [summed_up_time]


    return aggregate_data

def prepare(unprepared_data):
    prepared_data = []
    for key, value in unprepared_data.items():
        prepared_data.append({
            "request_identifier": key,
            "called": len(value),
             "response_time_mean": sum(value) / len(value)
        })

    return prepared_data


test_logs = [
    "2014-01-09T06:16:53.748849+00:00 heroku[router]: at=info method=POST path=/api/online/platforms/facebook_canvas/users/100002266342173/add_ticket host=mygame.heroku.com fwd='94.66.255.106' dyno=web.12 connect=12ms service=21ms status=200 bytes=78",
    "2014-01-09T06:16:53.742892+00:00 heroku[router]: at=info method=GET path=/api/users/100002266342173/count_pending_messages host=mygame.heroku.com fwd='94.66.255.106' dyno=web.8 connect=10ms service=20ms status=304 bytes=0",
    "2014-01-09T06:16:53.742892+00:00 heroku[router]: at=info method=GET path=/api/users/456643646346/count_pending_messages host=mygame.heroku.com fwd='94.66.255.106' dyno=web.8 connect=20ms service=30ms status=304 bytes=0",
    "2014-01-09T06:16:53.742892+00:00 heroku[router]: at=info method=GET path=/api/users/456643646346/count_pending_messages host=mygame.heroku.com fwd='94.66.255.106' dyno=web.8 connect=2ms service=20ms status=304 bytes=0",
    "2014-01-09T06:16:53.765430+00:00 heroku[router]: at=info method=GET path=/api/users/100005936523817/get_friends_progress host=mygame.heroku.com fwd='5.13.87.91' dyno=web.11 connect=4ms service=0ms status=200 bytes=7498"
    ]
assert build_aggregate_data(test_logs) == {
        "GET /api/users/{user_id}/count_pending_messages": [30, 50, 22],
        "GET /api/users/{user_id}/get_friends_progress": [4]
}, 'test 1 does not pass'

test_path_2 = '/api/online/platforms/facebook_canvas/users/100002266342173/add_ticket'
assert anonymize_path(test_path_2) == '/api/online/platforms/facebook_canvas/users/{user_id}/add_ticket'

test_path_3 = '/api/users/456643646346/count_pending_messages'
assert anonymize_path(test_path_3) == '/api/users/{user_id}/count_pending_messages'

test_path_4 = '/api/users/{user_id}/count_pending_messages'
assert is_relevant_log('GET', test_path_4) is True

test_path_5 = '/api/users/{user_id}/count_pending_messagessadfsdafasdfds'
assert is_relevant_log('POST', test_path_5) is False

unprepared_data = {
        "GET /api/users/{user_id}/count_pending_messages": [30, 50, 22],
        "GET /api/users/{user_id}/get_friends_progress": [4]
}
assert prepare(unprepared_data) == [
    {"request_identifier": "GET /api/users/{user_id}/count_pending_messages", "called": 3, "response_time_mean": 34},
    {"request_identifier": "GET /api/users/{user_id}/get_friends_progress", "called": 1, "response_time_mean": 4}
]
