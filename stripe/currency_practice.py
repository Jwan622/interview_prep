import math
from collections import defaultdict
from decimal import Decimal

CONVERSION_RATES = "AUD:USD:0.75,USD:CAD:1.26,USD:JPY:109.28,GBP:JPY:150.15"
def conversion(from_curr, to_curr):
  split_conversions = CONVERSION_RATES.split(',')
  rate_lookups = defaultdict(dict)
  for conversion in split_conversions:
    left_curr, right_curr, rate = conversion.split(":")
    rate_lookups[left_curr][right_curr] = round(Decimal(rate), 2)
    rate_lookups[right_curr][left_curr] = round(1/Decimal(rate), 2)

  if from_curr in rate_lookups and to_curr in rate_lookups[from_curr]:
    return rate_lookups[from_curr][to_curr]
  else:
    for intermediate_curr, intermediate_rate in rate_lookups[from_curr].items():
      final_rate = rate_lookups[intermediate_curr].get(to_curr)
      if final_rate is not None:
        return intermediate_rate * final_rate

  raise ValueError(f"Conversion rate from {from_curr} to {to_curr} not found.")




assert math.isclose(conversion("AUD", "USD"), Decimal('0.75'))
assert math.isclose(conversion("USD", "CAD"), Decimal('1.26'))
assert math.isclose(conversion("USD", "AUD"), Decimal('1.33'))
assert math.isclose(conversion("AUD", "CAD"), Decimal('0.945'), rel_tol=1e-9), 'this fina ltest did not pass'
