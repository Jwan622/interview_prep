def some_function(account):
    final_accounts = {}

    for key in account.keys():
        print('key: ', key)
        value = account[key]

        if value is None:
            final_accounts[key] = key

        while value:
            print('value in while: ', value)
            final_accounts[key] = value
            value = account[value]
            print('value after reassign: ', value)

    print('final_accounts: ', final_accounts)
    return final_accounts



# def some_function_recursive(account):
#     # Helper function to recursively find the final value
#     def find_final_value(key):
#         print('key: ', key)
#         print('account: ', account)
#         if account[key] is None:
#             return key
#         return find_final_value(account[key])
#
#     # Resolve each entry in the account dictionary
#     # you can just do this:
#     # resolved = {key: find_final_value(value) if value is not None else find_final_value(key) for key, value in account.items()}
#     resolved = {}
#     for key, value in account.items():
#         print('key in loop: ', key)
#         print('value in loop: ', value)
#         if value is not None:
#             resolved[key] = find_final_value(value)
#         elif value is None:
#             resolved[key] = find_final_value(key)
#
#     return resolved


# account = {'a':'b',
#            'c':'d',
#            'b':'d',
#            'd': None,
#            'e':'f',
#            'f':None,
#            'g':None,
#            'h':'b',
#            'i':'d'}
# assert some_function(account) == {'a': 'd', 'c': 'd', 'b': 'd', 'd': 'd', 'e': 'f', 'f': 'f', 'g': 'g', 'h': 'd', 'i': 'd'}

# account1 = {'a':'b',
#            'b': None}
# assert some_function(account1) == {'a': 'b', 'b': 'b'}

account2 = {'a':'b',
           'b': 'd',
            'd': None
            }
assert some_function(account2) == {'a': 'd', 'b': 'd', 'd': 'd'}
