# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

CONVERSION_RATES = "AUD:USD:0.75,USD:CAD:1.26,USD:JPY:109.28,GBP:JPY:150.15"


def conversion(from_curr, to_curr):
    rate_lookups = {}
    split_rates = [rate for rate in CONVERSION_RATES.split(',')]
    for rate in split_rates:
        left_side, right_side, rate = rate.split(':')
        print('left side: ', left_side)
        if left_side in rate_lookups:
            rate_lookups[left_side].append([right_side, float(rate)]) # use another dict next time
        else:
            rate_lookups[left_side] = [[right_side, float(rate)]]

    print('rate lookups: ', rate_lookups)
    for key, val in rate_lookups.items():
        if key == from_curr:
            for rate_pair in val:
                first_rate = rate_pair[0]
                first_rate_val = rate_pair[1]
                if first_rate == to_curr:
                    return rate_pair[1]
                for subsequent_lookups in rate_lookups.get(first_rate, []):
                    if subsequent_lookups[0] == to_curr:
                        print('got in here for subsequent')
                        print('sbsequent lookup value: ', subsequent_lookups[1])
                        print('first_rate value: ', first_rate_val)
                        print('final value: ', subsequent_lookups[1] * first_rate_val)
                        return round(subsequent_lookups[1] * first_rate_val, 3)

    for key, val in rate_lookups.items():
        if key == to_curr:
            for rate_pair in val:
                if rate_pair[0] == from_curr:
                    print("1/rate_pair[1]", 1/rate_pair[1])
                    return round(1/rate_pair[1], 3)


assert conversion("AUD", "USD") == 0.75
assert conversion("USD", "CAD") == 1.26
assert conversion("USD", "AUD") == 1.333
assert math.isclose(conversion("USD", "AUD"), 1.333, rel_tol=0.002)
assert conversion("AUD", "CAD") == 0.945  # multiply both
