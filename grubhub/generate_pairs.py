"""
pairs of values where the indicies are i and j. i < j but also elem[i] == elem[j]
"""

assert generate_pairs([1,1,2,2]) == 2 # [(0,1), (2,3)]
assert generate_pairs([1,1,2,3,2,3]) == 3 # [(0,1), (2,4), (3,5)]
assert generate_pairs([1,1,1,1]) == 6 # [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
