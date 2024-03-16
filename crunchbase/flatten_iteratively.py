# I like my other solution in the other file better
def flatten_dict_iteratively(d, sep='_'):
    final = {}

    # Stack for keeping track of iteration through nested dictionaries
    stack = [((), d)]

    while stack:
        print('stack: ', stack)
        path, current = stack.pop()
        print('path: ', path)
        print('current: ', current)
        for k, v in current.items():
            print('k: ', k)
            print('v: ', v)
            if isinstance(v, dict):
                print('v is a dict instance: ', v)
                stack.append((path + (k,), v))
            else:
                print('in else and this is what the sep.join looks like', sep.join((path + (k,))))
                final[sep.join((path + (k,)))] = v

    return final

# Example dictionary
data = {
    "a": "b",
    "c": {
        "d": "e",
        "f": "g",
        "h": {
            "i": "j"
        }
    }
}

# Flattening the dictionary iteratively
flattened_data = flatten_dict_iteratively(data)
print(flattened_data)
