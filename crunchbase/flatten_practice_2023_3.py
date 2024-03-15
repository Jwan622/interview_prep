def flatten(mapping):
    final = {}
    for key, value in mapping.items():
        flatten_helper(final, key, value)

    return final

def flatten_helper(final, key, value):
    if not isinstance(value, dict):
        final[key] = value
    else:
        for subkey, subvalue in value.items():
            new_key = "_".join([key, subkey])
            flatten_helper(final, new_key, subvalue)


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

