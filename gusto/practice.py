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

2014-01-09T06:16:53.742892+00:00 heroku[router]: at=info method=GET path=/api/users/100002266342173/count_pending_messages host=mygame.heroku.com fwd="94.66.255.106" dyno=web.8 connect=9ms service=9ms status=304 bytes=0

2014-01-09T06:16:53.742892+00:00 heroku[router]: at=info method=GET path=/api/users/456643646346/count_pending_messages host=mygame.heroku.com fwd="94.66.255.106" dyno=web.8 connect=9ms service=9ms status=304 bytes=0

2014-01-09T06:16:53.766841+00:00 heroku[router]: at=info method=POST path=/logs/save_personal_data host=mygame.heroku.com fwd="5.13.87.91" dyno=web.10 connect=1ms service=42ms status=200 bytes=16

2014-01-09T06:16:53.772938+00:00 heroku[router]: at=info method=POST path=/api/users/100002844291023 host=mygame.heroku.com fwd="46.195.178.244" dyno=web.6 connect=2ms service=43ms status=200 bytes=52

2014-01-09T06:16:53.765430+00:00 heroku[router]: at=info method=GET path=/api/users/100005936523817/get_friends_progress host=mygame.heroku.com fwd="5.13.87.91" dyno=web.11 connect=1ms service=47ms status=200 bytes=7498

Note that connect + service = response_time =  12 + 21 = 33. This will be the response_time

We want to return some data like this:
[{
  "request_identifier": "GET /api/users/{user_id}/count_pending_messages",
  "called": 3,
  "response_time_mean": 40.0,
}]
do not aggregate at the user level, aggregate on the pattern level like this pattern: path=/api/online/platforms/facebook_canvas/users/100002266342173/add_ticket
"""

import urllib.request
import re
from collections import defaultdict

SMALL_FILE_URL = 'https://gist.githubusercontent.com/bss/6dbc7d4d6d2860c7ecded3d21098076a/raw/244045d24337e342e35b85ec1924bca8425fce2e/sample.small.log'


def create_metrics():
    data = urllib.request.urlopen(SMALL_FILE_URL).read()
    file = data.decode('ascii')
    split_content = file.splitlines()
    process(split_content)

WE_CARE = [
    "GET /api/users/{user_id}/count_pending_messages",
    "GET /api/users/{user_id}/get_messages",
    "GET /api/users/{user_id}/get_friends_progress",
    "GET /api/users/{user_id}/get_friends_score",
    "POST /api/users/{user_id}",
    "GET /api/users/{user_id}"
]

def anonymize(path):
    return re.sub('/users/\d+', '/users/{user_id}', path)

def process(split_content):
    temp_holder = defaultdict(lambda: {'count': 0, 'times': 0})
    for log in split_content:
        timestamp, router, at, method, path, host, fwd, dyno, connect, service, status, byte = log.split(' ')
        method_and_path = anonymize(method.split('=')[1] + ' ' + path.split('=')[1])
        print('method_and_path after sub', method_and_path)
        connect_and_service = int(connect.split('=')[1].replace('ms', '')) + int(service.split('=')[1].replace('ms', ''))
        print('method and path', method_and_path)

        if any(care == method_and_path for care in WE_CARE):
            temp_holder[method_and_path]['count'] += 1
            temp_holder[method_and_path]['times'] += connect_and_service

    final = []
    for key, val in temp_holder.items():
        final.append(
            {
                "request_identifier": key,
                "called": val['count'],
                "response_time_mean": val['times'] / val['count']
            }
        )

    return final


test_data = [
    '2014-01-09T06:16:53.748849+00:00 heroku[router]: at=info method=POST path=/api/online/platforms/facebook_canvas/users/100002266342173/add_ticket host=mygame.heroku.com fwd="94.66.255.106" dyno=web.12 connect=12ms service=21ms status=200 bytes=78',
    '2014-01-09T06:16:53.742892+00:00 heroku[router]: at=info method=GET path=/api/users/100002266342173/count_pending_messages host=mygame.heroku.com fwd="94.66.255.106" dyno=web.8 connect=9ms service=9ms status=304 bytes=0',
    '2014-01-09T06:16:53.766841+00:00 heroku[router]: at=info method=POST path=/logs/save_personal_data host=mygame.heroku.com fwd="5.13.87.91" dyno=web.10 connect=1ms service=42ms status=200 bytes=16',
    '2014-01-09T06:16:53.772938+00:00 heroku[router]: at=info method=POST path=/api/users/100002844291023 host=mygame.heroku.com fwd="46.195.178.244" dyno=web.6 connect=2ms service=43ms status=200 bytes=52',
    '2014-01-09T06:16:53.765430+00:00 heroku[router]: at=info method=GET path=/api/users/100005936523817/get_friends_progress host=mygame.heroku.com fwd="5.13.87.91" dyno=web.11 connect=1ms service=47ms status=200 bytes=7498',
    '2014-01-09T06:16:53.760472+00:00 heroku[router]: at=info method=POST path=/api/users/1770684197 host=mygame.heroku.com fwd="74.139.217.81" dyno=web.5 connect=1ms service=17ms status=200 bytes=681',
    '2014-01-09T06:15:15.893505+00:00 heroku[router]: at=info method=GET path=/api/users/1686318645/get_friends_progress host=mygame.heroku.com fwd="1.125.42.139" dyno=web.3 connect=8ms service=90ms status=200 bytes=7534'
]
expected = process(test_data)

assert expected == [
    {'request_identifier': 'GET /api/users/{user_id}/count_pending_messages', 'called': 1, 'response_time_mean': 18.0},
    {'request_identifier': 'POST /api/users/{user_id}', 'called': 2, 'response_time_mean': 31.5},
    {'request_identifier': 'GET /api/users/{user_id}/get_friends_progress', 'called': 2,
     'response_time_mean': 73.0}
]


