def clean_string(input, chars_to_remove):
    for chars_unit in chars_to_remove:
        chars_to_remove = [s for s in chars_unit]
    print(chars_to_remove)
    for remove in chars_to_remove:
        input = input.replace(remove, "")
    print(input)
    return input


assert clean_string('hel-----lo worl---d', ['-']) == 'hello world', 'this test 1 did not pass'
assert clean_string('hel**$$lo worl**$$d', ['*$']) == 'hello world', 'this test 2 did not pass'



def remove_one_element_from_list(list, element_to_remove):
    list.remove(element_to_remove)
    return list
    # index_to_remove = list.index(element_to_remove)
    # del list[index_to_remove]
    # return list


assert remove_one_element_from_list(['a', 'a', 'b', 'c'], 'a') == ['a', 'b', 'c']
assert remove_one_element_from_list(['a', 'a', 'a', 'b', 'c'], 'a') == ['a', 'a', 'b', 'c']
assert remove_one_element_from_list(['a', 'b', 'c'], 'a') == ['b', 'c']


def remove_one_element_from_string(str, element_to_remove):
    # return str.replace(element_to_remove, '', 1)
    str_list = list(str)
    for index, c in enumerate(str_list):
        if c == element_to_remove:
            return str[:index] + str[index + 1:]

    return str



assert remove_one_element_from_string('hello', 'l') == 'helo'
assert remove_one_element_from_string('helllo', 'l') == 'hello'
assert remove_one_element_from_string('back', 'k') == 'bac'
assert remove_one_element_from_string('back', 'l') == 'back'
