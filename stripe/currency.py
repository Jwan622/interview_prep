# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from decimal import Decimal

CONVERSION_RATES = "AUD:USD:0.75,USD:CAD:1.26,USD:JPY:109.28,GBP:JPY:150.15"

def conversion(from_curr, to_curr):
  rate_lookups = {}
  split_rates = CONVERSION_RATES.split(',')

  for rate_string in split_rates:
    left_rate, right_rate, rate = rate_string.split(":")
    if left_rate in rate_lookups:
      rate_lookups[left_rate][right_rate] = Decimal(rate)
    else:
      rate_lookups[left_rate] = {right_rate: Decimal(rate)}

  print('rate_lookups', rate_lookups)

  for key, value in rate_lookups.items():
    if key == from_curr:
      for key in value.keys():
        if key == to_curr:
          return rate_lookups[from_curr][to_curr]

      other_keys = value.keys()
      for key in other_keys:
        if key in rate_lookups:
          return rate_lookups[from_curr][key] * rate_lookups[key][to_curr]

  for key, value in rate_lookups.items():
    if key == to_curr:
      for key in value.keys():
        if key == from_curr:
          return 1 / rate_lookups[to_curr][from_curr]




assert math.isclose(conversion("AUD", "USD"), Decimal('0.75'))
assert math.isclose(conversion("USD", "CAD"), Decimal('1.26'))
assert math.isclose(conversion("USD", "AUD"), Decimal('1.33333333333'), rel_tol=1e-9)
assert math.isclose(conversion("AUD", "CAD"), Decimal('0.945'), rel_tol=1e-9)


# from collections import defaultdict
# def conversion(from_curr, to_curr):
#     split_lookup = CONVERSION_RATES.split(',')
#     rate_lookups = defaultdict(dict)
#     for rate_trio in split_lookup:
#         left_curr, right_curr, rate = rate_trio.split(":")
#         rate_lookups[left_curr][right_curr] = float(rate)
#         rate_lookups[right_curr][left_curr] = round(1/float(rate),3)
#
#     if rate_lookups[from_curr].get(to_curr):
#         return rate_lookups[from_curr][to_curr]
#     else:
#         for first_rate_key in rate_lookups[from_curr].keys():
#             for indirect_rate_key in rate_lookups[first_rate_key].keys():
#                 if indirect_rate_key == to_curr:
#                     print('indirect rate key', indirect_rate_key)
#                     print('first rate key', first_rate_key)
#                     return round(rate_lookups[first_rate_key][indirect_rate_key] * rate_lookups[from_curr][first_rate_key], 3)
#
#         return True
