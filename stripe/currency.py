# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

CONVERSION_RATES = "AUD:USD:0.75,USD:CAD:1.26,USD:JPY:109.28,GBP:JPY:150.15"


# def conversion(from_curr, to_curr):
#     rate_lookups = {}
#     split_rates = [rate for rate in CONVERSION_RATES.split(',')]
#     for rate in split_rates:
#         left_side, right_side, rate = rate.split(':')
#         print('left side: ', left_side)
#         if left_side in rate_lookups:
#             rate_lookups[left_side].append({right_side: float(rate)}) # use another dict next time
#         else:
#             rate_lookups[left_side] = [{right_side: float(rate)}]
#
#     print('rate lookups: ', rate_lookups)
#     for key, val in rate_lookups.items():
#         if key == from_curr:
#             for rate_dct in val:
#                 for rate_key, rate_val in rate_dct.items():
#                     if rate_key == to_curr:
#                         return rate_val
#                     for subsequent_lookups in rate_lookups.get(rate_key, []):
#                         for rate_key1, rate_val1 in subsequent_lookups.items():
#                             if rate_key1 == to_curr:
#                                 print('got in here for subsequent')
#                                 print('sbsequent lookup value: ', rate_val1)
#                                 print('first_rate value: ', rate_key1)
#                                 print('final value: ', rate_val1 * rate_val1)
#                                 return round(rate_val1 * rate_val, 3)
#
#     for key, val in rate_lookups.items():
#         if key == to_curr:
#             for rate_dct in val:
#                 for rate_key, rate_val in rate_dct.items():
#                     if rate_key == from_curr:
#                         print("1/rate_pair[1]", 1/rate_val)
#                         return round(1/rate_val, 3)


from collections import defaultdict
def conversion(from_curr, to_curr):
    split_lookup = CONVERSION_RATES.split(',')
    rate_lookups = defaultdict(dict)
    for rate_trio in split_lookup:
        left_curr, right_curr, rate = rate_trio.split(":")
        rate_lookups[left_curr][right_curr] = float(rate)
        rate_lookups[right_curr][left_curr] = round(1/float(rate),3)

    if rate_lookups[from_curr].get(to_curr):
        return rate_lookups[from_curr][to_curr]
    else:
        for first_rate_key in rate_lookups[from_curr].keys():
            for nested_rate_key in rate_lookups[first_rate_key].keys():
                if nested_rate_key == to_curr:
                    print('nested rate key', nested_rate_key)
                    print('first rate key', first_rate_key)
                    return round(rate_lookups[first_rate_key][nested_rate_key] * rate_lookups[from_curr][first_rate_key], 3)

        return True


assert conversion("AUD", "USD") == 0.75
assert conversion("USD", "CAD") == 1.26
assert conversion("USD", "AUD") == 1.333
assert math.isclose(conversion("USD", "AUD"), 1.333, rel_tol=0.002)
assert conversion("AUD", "CAD") == 0.945  # multiply both
