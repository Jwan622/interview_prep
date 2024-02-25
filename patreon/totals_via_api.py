# A third party vendor has given us access to financial transactions (credit/debits) that they have processed for us.  We can access these transactions via an HTTP API.  See the section on API documentation below.

# We want you to write code that will:
# 1. Pull down this data
# 2. For each user: calculate the total amount of all their transactions (credits - debits).

# For instance, if a user "Keanu Reeves" with a user_id=10 has a debit txn of $10.00 and a credit txn of $40.00.  You should return a data structure that includes the following data:
# - Name: Keanu Reeves
# - User Id: 10
# - Amount Total: 30

# NOTE: YOUR CODE IS TO ANSWER AN AD-HOC ANALYTICS QUESTION. Your code is not intended for use in a production service.  Please choose your language and coding choices accordingly. There will be time later to discuss how we would code this in a formal service.

# API Documentation
# Transaction records are available via HTTP GET to https://jsonmock.hackerrank.com/api/transactions/search

# The following parameters can be added to the URL to alter the response:
# - txnType : Either "debit" or "credit" to only pull transactions of that type.
# - page : An integer to pull the page number of the response.  The response is paginated starting with page 1.

# For example, a GET request to:
# https://jsonmock.hackerrank.com/api/transactions/search?page=2
# Will pull the second page of the response for all transactions (both credits and debits).


# SAMPLE JSON

# {
#   "page": 2,
#   "per_page": 10,
#   "total": 300,
#   "total_pages": 30,
#   "data": [
#     {
#       "id": 11,
#       "userId": 1,
#       "userName": "John Oliver",
#       "timestamp": 1547112098173,
#       "txnType": "debit",
#       "amount": "$1,100.59",
#       "location": {
#         "id": 9,
#         "address": "961, Neptide, Elliott Walk",
#         "city": "Bourg",
#         "zipCode": 68602
#       },
#       "ip": "142.216.23.1"
#     },
#     {
#       "id": 12,
#       "userId": 1,
#       "userName": "John Oliver",
#       "timestamp": 1553870734435,
#       "txnType": "debit",
#       "amount": "$892.10",
#       "location": {
#         "id": 8,
#         "address": "389, Everest, Barwell Terrace",
#         "city": "Murillo",
#         "zipCode": 66061
#       },
#       "ip": "181.191.153.61"
#     },
#     {
#       "id": 13,
#       "userId": 1,
#       "userName": "John Oliver",
#       "timestamp": 1547039521086,
#       "txnType": "credit",
#       "amount": "$820.28",
#       "location": {
#         "id": 8,
#         "address": "389, Everest, Barwell Terrace",
#         "city": "Murillo",
#         "zipCode": 66061
#       },
#       "ip": "35.151.1.82"
#     },
#     {
#       "id": 14,
#       "userId": 1,
#       "userName": "John Oliver",
#       "timestamp": 1552146846090,
#       "txnType": "credit",
#       "amount": "$2,984.25",
#       "location": {
#         "id": 1,
#         "address": "948, Entroflex, Franklin Avenue",
#         "city": "Ilchester",
#         "zipCode": 84181
#       },
#       "ip": "5.116.1.11"
#     },
#     {
#       "id": 15,
#       "userId": 3,
#       "userName": "Helena Fernandez",
#       "timestamp": 1551421711822,
#       "txnType": "credit",
#       "amount": "$1,248.68",
#       "location": {
#         "id": 9,
#         "address": "961, Neptide, Elliott Walk",
#         "city": "Bourg",
#         "zipCode": 68602
#       },
#       "ip": "35.151.1.82"
#     },
#     {
#       "id": 16,
#       "userId": 4,
#       "userName": "Francesco De Mello",
#       "timestamp": 1551533186809,
#       "txnType": "credit",
#       "amount": "$1,233.56",
#       "location": {
#         "id": 9,
#         "address": "961, Neptide, Elliott Walk",
#         "city": "Bourg",
#         "zipCode": 68602
#       },
#       "ip": "212.215.115.165"
#     },
#     {
#       "id": 17,
#       "userId": 4,
#       "userName": "Francesco De Mello",
#       "timestamp": 1551693726293,
#       "txnType": "credit",
#       "amount": "$1,806.13",
#       "location": {
#         "id": 6,
#         "address": "206, Portaline, Brooklyn Avenue",
#         "city": "Brownlee",
#         "zipCode": 80358
#       },
#       "ip": "181.191.153.61"
#     },
#     {
#       "id": 18,
#       "userId": 2,
#       "userName": "Bob Martin",
#       "timestamp": 1550143522252,
#       "txnType": "debit",
#       "amount": "$2,235.13",
#       "location": {
#         "id": 1,
#         "address": "948, Entroflex, Franklin Avenue",
#         "city": "Ilchester",
#         "zipCode": 84181
#       },
#       "ip": "111.83.155.103"
#     },
#     {
#       "id": 19,
#       "userId": 2,
#       "userName": "Bob Martin",
#       "timestamp": 1552070436910,
#       "txnType": "credit",
#       "amount": "$2,659.47",
#       "location": {
#         "id": 6,
#         "address": "206, Portaline, Brooklyn Avenue",
#         "city": "Brownlee",
#         "zipCode": 80358
#       },
#       "ip": "212.215.115.165"
#     },
#     {
#       "id": 20,
#       "userId": 2,
#       "userName": "Bob Martin",
#       "timestamp": 1546523118910,
#       "txnType": "debit",
#       "amount": "$1,543.25",
#       "location": {
#         "id": 9,
#         "address": "961, Neptide, Elliott Walk",
#         "city": "Bourg",
#         "zipCode": 68602
#       },
#       "ip": "142.216.23.1"
#     }
#   ]
# }

import requests

URL = 'https://jsonmock.hackerrank.com/api/transactions/search'


# def some_function():
#     response = requests.get(URL).json()
#     total_pages = response['total_pages']
#     total_data = []
#     for page_number in range(total_pages):
#         response = requests.get(URL + '?' + f"page={page_number + 1}").json()
#         total_data += response['data']
#
#     final_ledger = {}
#
#     # aggregate credits and ebits
#     for data in total_data:
#         print(data)
#         is_credit = data['txnType'] == 'credit'
#         credit_amount = float(data['amount'].replace('$', '').replace(',', '')) if is_credit else 0
#         debit_amount = float(data['amount'].replace('$', '').replace(',', '')) if not is_credit else 0
#
#         username = data['userName']
#         if username not in final_ledger:
#             final_ledger[username] = (data['userId'], credit_amount, debit_amount)
#         else:
#             final_ledger[username] = (final_ledger[username][0], final_ledger[username][1] + credit_amount,
#                                       final_ledger[username][2] + debit_amount)
#
#     print('final_ledger', final_ledger)
#
#     thing_to_return = []
#     # clean data structure
#     for key, value in final_ledger.items():
#         thing_to_return.append({
#             'user_name': key,
#             'total': value[1] - value[2],
#             'id': value[0]
#         })
#
#     print(thing_to_return)


# assert some_function()['Helena Fernandez'] == '$1,248.68', 'simple test case 1 one credit should pass'
# assert some_function()['Francesco De Mello'] == '$1,248.68', 'simple test case 2 two credids should pass'

# https://jsonmock.hackerrank.com/api/transactions/search?page=110
from decimal import Decimal
URL = 'https://jsonmock.hackerrank.com/api/transactions/search'
def some_function():
    response = requests.get(URL).json()
    final_records = {}
    for page_number in range(response['total_pages']):
        page_data = requests.get(URL + '?' + f"page={page_number + 1}").json()['data']
        calculate_individual_totals(final_records, page_data)

    return final_records.values()


def calculate_individual_totals(accumulator, page_data):
    for transaction in page_data:
        total_amount = 0
        unique_key = transaction['userName'] + str(transaction['userId'])
        user_id = transaction['userId']
        name = transaction['userName']
        cleaned_amount = Decimal(transaction['amount'].replace('$', '').replace(',', ''))
        if transaction['txnType'] == 'debit':
            total_amount -= cleaned_amount
        else:
            total_amount += cleaned_amount

        if unique_key in accumulator:
            accumulator[unique_key]['total_amount'] += total_amount
        else:
            accumulator[unique_key] = {'total_amount': total_amount, 'userId': user_id, 'name': name}

    return accumulator



page_data = [{'id': 1, 'userId': 1, 'userName': 'John Oliver', 'timestamp': 1549536882071, 'txnType': 'debit', 'amount': '$100', 'location': {'id': 7, 'address': '770, Deepends, Stockton Street', 'city': 'Ripley', 'zipCode': 44139}, 'ip': '212.215.115.165'}, {'id': 2, 'userId': 2, 'userName': 'Bob Martin', 'timestamp': 1549260902604, 'txnType': 'debit', 'amount': '$200', 'location': {'id': 8, 'address': '389, Everest, Barwell Terrace', 'city': 'Murillo', 'zipCode': 66061}, 'ip': '212.215.115.165'}, {'id': 3, 'userId': 2, 'userName': 'Bob Martin', 'timestamp': 1549530365037, 'txnType': 'credit', 'amount': '$2', 'location': {'id': 1, 'address': '948, Entroflex, Franklin Avenue', 'city': 'Ilchester', 'zipCode': 84181}, 'ip': '142.216.23.1'}, {'id': 4, 'userId': 1, 'userName': 'John Oliver', 'timestamp': 1549272069586, 'txnType': 'credit', 'amount': '$0.50', 'location': {'id': 8, 'address': '389, Everest, Barwell Terrace', 'city': 'Murillo', 'zipCode': 66061}, 'ip': '119.162.205.226'}]
assert calculate_individual_totals({}, page_data) == {'John Oliver1': {'name': 'John Oliver', 'total_amount': -99.50, 'userId': 1}, 'Bob Martin2': {"name": 'Bob Martin', 'userId': 2, 'total_amount': -198}}









