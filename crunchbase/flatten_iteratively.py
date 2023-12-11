def flatten_dict_iteratively(d, sep='_'):
    dict_flattened = {}

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
                print('in else')
                dict_flattened[sep.join((path + (k,)))] = v

    return dict_flattened

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
