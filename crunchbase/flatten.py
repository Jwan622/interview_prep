"""
{
    "a": "b",
    "c": {
        "d": "e",
        "f": "g"
        }
}

to

{
    "a": "b",
    "c_d": "e",
    "c_f": "g"
} dammit just got it
"""

def do_the_magic(flattened_list, value_could_be_string_or_dict, built_key):
    if not isinstance(value_could_be_string_or_dict, dict): # base case
        flattened_list[built_key] = value_could_be_string_or_dict
    else:
        for nested_key, nested_value in value_could_be_string_or_dict.items():
            new_key = [built_key]
            new_key.append(nested_key)
            new_key_delimited = "_".join(new_key)
            print('new_key_delimited: ', new_key_delimited)
            do_the_magic(flattened_list, nested_value, new_key_delimited) # this helper is called at end. we need to pass the return value that is being built on, and the new segment of the value that needs to be evaluated for base cases or a new list. the new_key needs to be passed too which is being built up.


def flatten(input) -> dict:
    # this is the iterative approach, but we found a recursive approach
    # if input is None:
    #     return None
    # flattened_list = {}

    # for key, value in input.items():
    #     if not isinstance(value, dict):
    #         flattened_list[key] = value
    #     else:
    #         for nested_key, nested_value in value.items():
    #             new_key = [key]
    #             new_key.append(nested_key)
    #             new_key_delimited = "_".join(new_key)
    #             print('new_key_delimited: ', new_key_delimited)
    #             flattened_list[new_key_delimited] = nested_value

    if input is None:
        return None
    flattened_list = {}

    for key, value in input.items():  # this iteration still needs to be outside the flatten because think of a flat nested input
        do_the_magic(flattened_list, value, key)


    return flattened_list






# run some tests
assert flatten({"a": "b"}) == {"a": "b"}, "test_naive_case did not pass"
assert flatten({"a": "b", "c": {"d": "e"}}) == {"a": "b", "c_d": "e"}, "tests_2 did not pass"
assert flatten({"a": "b", "c": {"d": "e", "f": "g"}}) == {"a": "b", "c_d": "e", "c_f": "g"}, "tests_3 did not pass"
assert flatten({}) == {}, "tests_4 did not pass"
assert flatten(None) == None, "tests_5 did not pass"

actual = flatten(
    {"a": "b",
    "c": {
        "d": "e",
        "f": "g",
        "h": {
                "i": "j",
                "k": "l"
            }
        }
    })
assert actual == {"a": "b", "c_d": "e", "c_f": "g", "c_h_i": "j", "c_h_k": "l"}, f"tests_6 did not pass: {actual}"
print("ALL TESTS PASS")
