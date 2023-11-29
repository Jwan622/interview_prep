import json

# Opening JSON file
f = open('card-transaction-data.json')
data = json.load(f)
for i in data['cardTransactionList']:
    print(i)
f.close()
