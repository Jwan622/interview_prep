def flatten(mapping):
    final = {}
    stack = [(
        list(mapping.keys()), list(mapping.values())
    )]  # Initialize stack with keys and values, this is one big tuple if you look closely. god python syntax sucks sometimes
    print('intial stack: ', stack)
    while stack:
        keys, values = stack.pop()
        print('keys: ', keys)
        print('values: ', values)
        for key, value in zip(keys, values):
            if isinstance(value, dict):
                # If value is a dict, push its items onto the stack
                new_keys = ["_".join([key, k]) for k in value.keys()]
                stack.append((new_keys, list(value.values())))
            else:
                final[key] = value

    return final


start_data = {
    "a": "b",
    "c": {
        "d": "e",
        "f": "g"
    }
}
expected = {
    "a": "b",
    "c_d": "e",
    "c_f": "g"
}
assert flatten(start_data) == expected


start_data = {
    "a": "b",
    "c": {
        "d": "e",
        "f": "g",
        "h": {
            "i": "j"
        }
    }
}
expected = {
    "a": "b",
    "c_d": "e",
    "c_f": "g",
    "c_h_i": "j"
}
assert flatten(start_data) == expected
