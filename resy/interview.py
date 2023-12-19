import re

TEST_STRINGS = [
    ('fdsa1???9', True) # 1 + 9
    , ('1?sad?qw!?9', True) # 1 + 9
    , ('1?sad?qw!?8?', False) # 1 + 9
    , ('1?5???5', True) # 5 + 5
    , ('1???9???7', False) # 1 + 9 && 9 + 7
    , ('3??7???5', False) # 7 + 5
    ,('5???57???3', True) # 5 + 5 && 7 + 3
    ,('1??9???1', True) # 1 + 9 && 9 + 7
    ,('1???9???1', True) # 1 + 9 && 9 + 7
]

def check(s):
    '''Function that accepts a string and verifies that for each pair of digits separated by exactly 3 question marks that the sum of those digits is 10
    '''
    first_letter_pointer = 0

    while first_letter_pointer < len(s) - 1:
        print('first_letter_pointer', first_letter_pointer)
        if s[first_letter_pointer].isdigit():
            second_letter_pointer = first_letter_pointer + 1
            while second_letter_pointer < len(s):
                print('second_letter_pointer', second_letter_pointer)
                if s[second_letter_pointer].isdigit():
                    if int(s[first_letter_pointer]) + int(s[second_letter_pointer]) == 10 and second_letter_pointer != len(s) - 1:
                        first_letter_pointer = second_letter_pointer + 1
                        break
                    if int(s[first_letter_pointer]) + int(s[second_letter_pointer]) != 10 and s[first_letter_pointer:second_letter_pointer + 1].count('?') == 3:
                        return False
                second_letter_pointer = second_letter_pointer + 1
        first_letter_pointer = first_letter_pointer + 1
    return True



for to_check, expected in TEST_STRINGS:
    if check(to_check) != expected:
        print(f'Failed on {to_check}')
print('done')
