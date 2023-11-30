import json
import datetime

# Opening JSON file
f = open('card-transaction-data.json')
data = json.load(f)


def account_sort_by_date(data, accountId):
    # filter all the transaction list for an account id
    # sort it on the transactionDate
    # relevant_transactions = []
    # for transaction in data['cardTransactionList']:
    #     if transaction['accountId'] == accountId:
    #         relevant_transactions.append(transaction)
    relevant_transactions = [
        transaction for transaction in data['cardTransactionList']
        if transaction['accountId'] == accountId
    ]

    relevant_transactions.sort(key=lambda x: x['transactionDate'], reverse=True)

    return relevant_transactions


assert account_sort_by_date(data, '534524') == [
    {'accountId': '534524', 'amount': 83.24, 'category': 'bar', 'transactionDate': '2021-08-31T12:56:32.850818',
     'transactionId': 'dae49e05-a37c-470b-a7cd-4e07b0db206e', 'vendorId': '1016', 'vendorName': 'Thirsty Step'},
    {'accountId': '534524', 'amount': 52.54, 'category': 'retail', 'transactionDate': '2021-08-27T12:56:32.850818',
     'transactionId': '2d2a4be7-d816-43ca-b4a8-92368a5f47a8', 'vendorId': '1004', 'vendorName': 'Morty Mart'},
    {'accountId': '534524', 'amount': 53.74, 'category': 'travel', 'transactionDate': '2021-08-26T12:56:32.850818',
     'transactionId': '0ef1d522-6272-42eb-bde3-e6d120079529', 'vendorId': '1008', 'vendorName': 'Titanic 2'},
    {'accountId': '534524', 'amount': 54.65, 'category': 'bar', 'transactionDate': '2021-08-25T12:56:32.850818',
     'transactionId': '018f36e3-11ab-4232-88a1-a4bfc8f122fa', 'vendorId': '1011', 'vendorName': 'Cogspot'},
    {'accountId': '534524', 'amount': 51.61, 'category': 'travel', 'transactionDate': '2021-08-25T12:56:32.850818',
     'transactionId': '0431b451-1fdf-4c32-81b1-ababe03ad1da', 'vendorId': '1013',
     'vendorName': 'Immortality Field Resort'},
    {'accountId': '534524', 'amount': 76.15, 'category': 'restaurant', 'transactionDate': '2021-08-24T12:56:32.850818',
     'transactionId': '17a65302-3066-4c41-bff4-afe12e538b5a', 'vendorId': '1003', 'vendorName': 'Blips and Chipz'},
    {'accountId': '534524', 'amount': 85.35, 'category': 'restaurant', 'transactionDate': '2021-08-22T12:56:32.850818',
     'transactionId': 'c32786c9-4d71-41ed-844a-b77dc681e93b', 'vendorId': '1009', 'vendorName': 'Furp Rock Plaza'},
    {'accountId': '534524', 'amount': 21.93, 'category': 'restaurant', 'transactionDate': '2021-08-22T12:56:32.850818',
     'transactionId': 'b7b70165-8604-450a-98bc-83efd5e7b125', 'vendorId': '1002', 'vendorName': "Lil' Bits"},
    {'accountId': '534524', 'amount': 72.41, 'category': 'travel', 'transactionDate': '2021-08-21T12:56:32.850818',
     'transactionId': 'b9946f7f-8711-4341-903a-5f6e1a9e0e4e', 'vendorId': '1008', 'vendorName': 'Titanic 2'},
    {'accountId': '534524', 'amount': 5.83, 'category': 'restaurant', 'transactionDate': '2021-08-19T12:56:32.850818',
     'transactionId': '16cf3237-010d-489a-99a1-196cd3924a53', 'vendorId': '1012', 'vendorName': 'Furp Rock Plaza'},
    {'accountId': '534524', 'amount': 57.83, 'category': 'travel', 'transactionDate': '2021-08-19T12:56:32.850818',
     'transactionId': '5aab564f-2dc6-4c50-909f-0e817982e104', 'vendorId': '1013',
     'vendorName': 'Immortality Field Resort'},
    {'accountId': '534524', 'amount': 92.75, 'category': 'travel', 'transactionDate': '2021-08-19T12:56:32.850818',
     'transactionId': '8b1208b5-c948-4338-8be4-732fe7ffa378', 'vendorId': '1013',
     'vendorName': 'Immortality Field Resort'},
    {'accountId': '534524', 'amount': 27.85, 'category': 'travel', 'transactionDate': '2021-08-17T12:56:32.850818',
     'transactionId': '53f7f221-7fa0-4653-a64f-f9fc65967d92', 'vendorId': '1013',
     'vendorName': 'Immortality Field Resort'},
    {'accountId': '534524', 'amount': 47.57, 'category': 'travel', 'transactionDate': '2021-08-16T12:56:32.850818',
     'transactionId': '25bc19ff-617e-4801-a960-517ba5ca2bec', 'vendorId': '1013',
     'vendorName': 'Immortality Field Resort'},
    {'accountId': '534524', 'amount': 88.77, 'category': 'retail', 'transactionDate': '2021-08-09T12:56:32.850818',
     'transactionId': 'be701b7d-7c68-4c31-8ec8-ddfd8ceb5627', 'vendorId': '1004', 'vendorName': 'Morty Mart'},
    {'accountId': '534524', 'amount': 0.96, 'category': 'travel', 'transactionDate': '2021-08-08T12:56:32.850818',
     'transactionId': '93dffed1-3695-4cd5-88a2-85501c9237dc', 'vendorId': '1001', 'vendorName': 'Anatomy Park'},
    {'accountId': '534524', 'amount': 77.91, 'category': 'travel', 'transactionDate': '2021-08-07T12:56:32.850818',
     'transactionId': '13cd28d4-7713-4cef-84b0-3c516303fcd9', 'vendorId': '1008', 'vendorName': 'Titanic 2'},
    {'accountId': '534524', 'amount': 17.24, 'category': 'restaurant', 'transactionDate': '2021-08-06T12:56:32.850818',
     'transactionId': '1256ee50-c42a-4f2d-8cfc-73e0a43601b9', 'vendorId': '1003', 'vendorName': 'Blips and Chipz'},
    {'accountId': '534524', 'amount': 95.14, 'category': 'retail', 'transactionDate': '2021-08-01T12:56:32.850818',
     'transactionId': '84689504-1f53-4e36-9f65-d3c8c9460f64', 'vendorId': '1007', 'vendorName': 'Curse Purge Plus!'},
    {'accountId': '534524', 'amount': 87.09, 'category': 'retail', 'transactionDate': '2021-07-30T12:56:32.850818',
     'transactionId': '252cc8a4-adaf-427d-985d-92384be06f8d', 'vendorId': '1005', 'vendorName': 'Needful Things'},
    {'accountId': '534524', 'amount': 17.12, 'category': 'travel', 'transactionDate': '2021-07-25T12:56:32.850818',
     'transactionId': '872e35a3-d7f3-443e-a9ab-071a9f6fd9ef', 'vendorId': '1001', 'vendorName': 'Anatomy Park'},
    {'accountId': '534524', 'amount': 18.8, 'category': 'entertainment',
     'transactionDate': '2021-07-23T12:56:32.850818', 'transactionId': '12b2dd1e-4423-4bcf-99c8-c8c8bd2ecd65',
     'vendorId': '1010', 'vendorName': 'Egan Cinema'},
    {'accountId': '534524', 'amount': 41.82, 'category': 'travel', 'transactionDate': '2021-07-23T12:56:32.850818',
     'transactionId': '3aca0bbb-c423-42fd-aa10-de632e85dd27', 'vendorId': '1008', 'vendorName': 'Titanic 2'},
    {'accountId': '534524', 'amount': 77.55, 'category': 'entertainment',
     'transactionDate': '2021-07-23T12:56:32.850818', 'transactionId': '1e56fbc3-43b8-4bcb-a410-ace3dc94e7e1',
     'vendorId': '1010', 'vendorName': 'Egan Cinema'},
    {'accountId': '534524', 'amount': 20.93, 'category': 'restaurant', 'transactionDate': '2021-07-22T12:56:32.850818',
     'transactionId': '50db51a0-1825-4035-abe3-381e8bcdeeee', 'vendorId': '1015', 'vendorName': "Shoney's"},
    {'accountId': '534524', 'amount': 49.22, 'category': 'travel', 'transactionDate': '2021-07-22T12:56:32.850818',
     'transactionId': 'aa2365a4-7142-4bfe-b356-17e403f91a2f', 'vendorId': '1008', 'vendorName': 'Titanic 2'},
    {'accountId': '534524', 'amount': 68.33, 'category': 'travel', 'transactionDate': '2021-07-21T12:56:32.850818',
     'transactionId': '4e486aef-9ed8-4fc1-9751-37026e3952f1', 'vendorId': '1014',
     'vendorName': 'Burningmanapaloozaflargabarg'},
    {'accountId': '534524', 'amount': 40.8, 'category': 'travel', 'transactionDate': '2021-07-20T12:56:32.850818',
     'transactionId': '87f213cb-b953-43d2-8a84-290188e4595a', 'vendorId': '1013',
     'vendorName': 'Immortality Field Resort'},
    {'accountId': '534524', 'amount': 69.32, 'category': 'bar', 'transactionDate': '2021-07-14T12:56:32.850818',
     'transactionId': '632c805d-75f0-47c8-8039-abf264d8f321', 'vendorId': '1011', 'vendorName': 'Cogspot'},
    {'accountId': '534524', 'amount': 72.39, 'category': 'bar', 'transactionDate': '2021-07-13T12:56:32.850818',
     'transactionId': 'd9620e7b-2fc6-4fbd-926b-d5702185728f', 'vendorId': '1016', 'vendorName': 'Thirsty Step'},
    {'accountId': '534524', 'amount': 66.22, 'category': 'travel', 'transactionDate': '2021-07-10T12:56:32.850818',
     'transactionId': '084ecafb-520f-4168-a7b8-8b6bd7c648e7', 'vendorId': '1001', 'vendorName': 'Anatomy Park'},
    {'accountId': '534524', 'amount': 68.39, 'category': 'retail', 'transactionDate': '2021-07-09T12:56:32.850818',
     'transactionId': 'd39505d0-9fa8-484f-9948-058fcede7981', 'vendorId': '1005', 'vendorName': 'Needful Things'},
    {'accountId': '534524', 'amount': 16.73, 'category': 'retail', 'transactionDate': '2021-07-08T12:56:32.850818',
     'transactionId': '409b465e-5697-4757-bb90-1822c8b4f338', 'vendorId': '1007', 'vendorName': 'Curse Purge Plus!'},
    {'accountId': '534524', 'amount': 94.73, 'category': 'bar', 'transactionDate': '2021-07-06T12:56:32.850818',
     'transactionId': '86cebc26-fec4-44b8-ae11-2a95ddbcbcc8', 'vendorId': '1016', 'vendorName': 'Thirsty Step'},
    {'accountId': '534524', 'amount': 26.66, 'category': 'retail', 'transactionDate': '2021-07-01T12:56:32.850818',
     'transactionId': 'b3dd4d69-e966-47c9-a601-182f6ba07eed', 'vendorId': '1005', 'vendorName': 'Needful Things'},
    {'accountId': '534524', 'amount': 78.72, 'category': 'retail', 'transactionDate': '2021-06-30T12:56:32.850818',
     'transactionId': 'be35ebac-5f4d-4d2b-834a-c543cfd0c8ba', 'vendorId': '1004', 'vendorName': 'Morty Mart'},
    {'accountId': '534524', 'amount': 68.53, 'category': 'entertainment',
     'transactionDate': '2021-06-30T12:56:32.850818', 'transactionId': '5434a538-ab11-429e-bae9-29691da1def4',
     'vendorId': '1010', 'vendorName': 'Egan Cinema'},
    {'accountId': '534524', 'amount': 50.68, 'category': 'restaurant', 'transactionDate': '2021-06-29T12:56:32.850818',
     'transactionId': '9b0ca8fe-0543-46e5-9018-2e3f558588c9', 'vendorId': '1015', 'vendorName': "Shoney's"},
    {'accountId': '534524', 'amount': 65.49, 'category': 'restaurant', 'transactionDate': '2021-06-29T12:56:32.850818',
     'transactionId': 'ea55ef44-9998-409e-8b55-6eb4ad0b7b40', 'vendorId': '1012', 'vendorName': 'Furp Rock Plaza'},
    {'accountId': '534524', 'amount': 35.83, 'category': 'restaurant', 'transactionDate': '2021-06-25T12:56:32.850818',
     'transactionId': '7c8d02e3-e0a5-4c38-8b34-257d85aa1646', 'vendorId': '1003', 'vendorName': 'Blips and Chipz'},
    {'accountId': '534524', 'amount': 27.2, 'category': 'restaurant', 'transactionDate': '2021-06-23T12:56:32.850818',
     'transactionId': '0856aed5-a8c2-4263-8082-fbca6cfc9a10', 'vendorId': '1002', 'vendorName': "Lil' Bits"},
    {'accountId': '534524', 'amount': 80.92, 'category': 'travel', 'transactionDate': '2021-06-22T12:56:32.850818',
     'transactionId': 'a9e63252-5927-4696-9956-727adee2175f', 'vendorId': '1014',
     'vendorName': 'Burningmanapaloozaflargabarg'},
    {'accountId': '534524', 'amount': 95.22, 'category': 'travel', 'transactionDate': '2021-06-20T12:56:32.850818',
     'transactionId': '6073f608-1737-40a2-beee-751d454d26d8', 'vendorId': '1001', 'vendorName': 'Anatomy Park'},
    {'accountId': '534524', 'amount': 3.66, 'category': 'restaurant', 'transactionDate': '2021-06-20T12:56:32.850818',
     'transactionId': '1d8c6eec-4f73-44c5-8144-08654eca0217', 'vendorId': '1002', 'vendorName': "Lil' Bits"},
    {'accountId': '534524', 'amount': 70.77, 'category': 'retail', 'transactionDate': '2021-06-19T12:56:32.850818',
     'transactionId': 'd8181603-04ca-4b35-bc01-6a34419fe594', 'vendorId': '1006', 'vendorName': 'Pawn Shop Planet'}]


def percent_cash_back_per_user(data, accountId, percent):
    relevant_transactions = account_sort_by_date(data, accountId)
    # aggregate the amount
    cashback_sum = sum([transaction['amount'] for transaction in relevant_transactions], 0)

    return round(cashback_sum * percent, 2)


assert percent_cash_back_per_user(data, '534524', 0.01) == 24.77, 'The two values are not equal: %s vs %s' % (percent_cash_back_per_user(data, '534524', 0.01), 24.76)


def calculate_percent_back(amount, percent):
    return round(amount * percent, 2)


promotion_lookup = {
    "1": "travel",
    "2": "restaurant",
    "3": "retail",
    "4": "entertainment",
    "5": "bar",
    "6": "travel",
    "7": "restaurant",
    "8": "retail",
    "9": "entertainment",
    "10": "bar",
    "11": "restaurant",
    "12": "retail",
}


def month_promotion_cashback(data, accountId):
    # figure out transaction month
    # if the month and the type
    total_cashback = 0
    relevant_transactions = account_sort_by_date(data, accountId)
    for transaction in relevant_transactions:
        month = str(datetime.datetime.strptime(transaction['transactionDate'], '%Y-%m-%dT%H:%M:%S.%f').month)
        if promotion_lookup[month] == transaction['category']:
            total_cashback += calculate_percent_back(transaction['amount'], 0.05)
        else:
            total_cashback += calculate_percent_back(transaction['amount'], 0.01)

    return total_cashback


# print(account_sort_by_date(data, '534524'))
# print(one_percent_cash_back_per_user(data, '534524'))
# print(month_promotion_cashback(data, '534524'))


def monthly_cashback_cap_at_10(data, accountId):
    relevant_transactions = account_sort_by_date(data, accountId)
    running_monthly_cashbacks = {}
    total_cashback = 0
    monthly_limit = 10.00

    for transaction in relevant_transactions:
        month = str(datetime.datetime.strptime(transaction['transactionDate'], '%Y-%m-%dT%H:%M:%S.%f').month)

        if month not in running_monthly_cashbacks:
            running_monthly_cashbacks[month] = {
                'five_percent_cashback': 0.00,
                'one_percent_cashback': 0.00,
            }

        if promotion_lookup[month] == transaction['category']:
            if (
                    running_monthly_cashbacks[month]['five_percent_cashback'] +
                    calculate_percent_back(transaction['amount'], 0.05) <= monthly_limit
            ):
                running_monthly_cashbacks[month]['five_percent_cashback'] += calculate_percent_back(
                    transaction['amount'], 0.05
                )
            else:
                amount_left_up_to_10 = 10.00 - running_monthly_cashbacks[month]['five_percent_cashback']
                amount_to_deduct_from_transaction_amount = amount_left_up_to_10 * 20
                transaction['amount'] = transaction['amount'] - amount_to_deduct_from_transaction_amount
                running_monthly_cashbacks[month]['five_percent_cashback'] = 10.00
                running_monthly_cashbacks[month]['one_percent_cashback'] += calculate_percent_back(
                    transaction['amount'], 0.01)
        else:
            running_monthly_cashbacks[month]['one_percent_cashback'] += calculate_percent_back(
                transaction['amount'], 0.01)

    for monthly_cashbacks_both_categories in running_monthly_cashbacks.values():
        for cashback in monthly_cashbacks_both_categories.values():
            total_cashback += cashback

    return total_cashback


assert monthly_cashback_cap_at_10(data, '534524') == 40.67999999999999
