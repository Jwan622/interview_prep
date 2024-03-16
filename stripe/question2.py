from functools import reduce
'''
Tech screen was 3 parts
First was to parse a string of letters from input that represent a binary status of something being open or closed and calculate a count.
Second and third were follow up questions to build on that solutions

string manipulation problem. give me some string maniupation methods.
'''

# chat gpt prompt
'''
Here's a practice problem for string manipulation, focusing on parsing a string to interpret binary statuses, similar to what you might encounter in a tech screen for a company like Stripe. Additionally, I'll include some common string manipulation methods that could be useful for solving these types of problems.

Practice Problem
You're given a string representing the daily status of a series of switches, where '1' indicates the switch is on (open) and '0' indicates the switch is off (closed). Your task is to parse this string and perform the following operations:

Basic Parsing and Counting:
Calculate and return the total count of days when all switches were on (all '1's in the string).

Consecutive Segments:
Find the longest consecutive sequence of days with all switches on (the longest substring of '1's).

Switch Flipping:
Determine the minimum number of days you need to flip the switches (change from '0' to '1' or vice versa) to make all switches on for the maximum consecutive days. This essentially means finding the shortest sequence of '0's that, if flipped, would result in the longest consecutive sequence of '1's.

Example Input
makefile
Copy code
input_string = "110011011110000111"
Example Output for Each Part
Total count of days with all switches on: 2 (assuming '11' means all switches are on for this context)
Longest consecutive sequence of days with all switches on: 5 ('11111')
Minimum flips to achieve longest consecutive on period: 2 (flipping the two '0's in '0000111' to get '1111111')
String Manipulation Methods
len(string): Returns the length of the string.
string.count(substring): Counts how many times a substring occurs in string.
string.find(substring): Returns the lowest index in string where substring is found.
string.replace(old, new): Returns a string where all occurrences of old have been replaced by new.
string.split(separator): Returns a list of the words in the string, using separator as the delimiter string.
string.strip(chars): Returns a trimmed version of the string where all characters in chars are removed from the beginning and the end of the string.
Regular expressions (via the re module) for complex pattern matching and manipulation.
Would you like to dive into the code solution for this practice problem, or do you need more explanation on the string manipulation methods?
'''

def count_switches(input_string):
    ones_count = 0
    longest_consec = 0
    current_longest = 0
    switch_split = list(input_string)
    print('switch split: ', switch_split)
    for switch in switch_split:
        if switch == '1':
            ones_count += 1
            current_longest += 1
            if current_longest > longest_consec:
                longest_consec += 1
        else:
             current_longest = 0

    return [ones_count, longest_consec]

test_string = "110011011110000111"
expected = [11, 4]
assert count_switches(test_string) == expected, f'actual: {count_switches(test_string)}'
