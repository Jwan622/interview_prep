"""
.Check if One String Swap can make strings Equal

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:
Input: s1 = “grubhub”, s2 = “brughub”
Output: true
Explanation: For example, swap the first character with the 4th character of s2 to make “grubhub”.
Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
"""


assert can_swap("grubhub", "brughub") == True
assert can_swap("attack", "defend") == False
assert can_swap("attack", "attack") == True
assert can_swap("toe", "toe") == False
