# say cart has 20, 30, 50. Say we have a 10% coupon for the 50. so cart = 100. We can add it up and then subtract the discounts of 10% to the 50 so 100-5 = 95
# Or add up 20 + 30 + 90%50 = 95. What's easier?
# 20 + 30 + 50 - (50 * 0.05) = 95
# 20 + 30 + ((1 - 0.05) * 50) = 20 + 30 + 50 - (50 * 0.05) so same thing.


def calculate_totals(cart, coupons):
    initial_total = sum(item['price'] for item in cart)

    total_discounts = apply_coupons(cart, coupons)

    return initial_total - total_discounts

def apply_coupons(cart, coupons):
    coupons = [coupons] if isinstance(coupons, dict) else coupons
    total_discount = 0
    for coupon in coupons:
        possible_discounts = []
        coupon_categories = [coupon['category']] if isinstance(coupon['category'], str) else coupon['category']
        for category in coupon_categories:
            discount = 0
            applicable_items = [item for item in cart if item['category'] == category]
            applicable_items_length = len(applicable_items)
            applicable_items_amount = sum(item['price'] for item in applicable_items)

            if (coupon['minimum_num_items_required'] is None or coupon['minimum_num_items_required'] <= applicable_items_length) and (coupon['minimum_amount_required'] is None or coupon['minimum_amount_required'] <= applicable_items_amount):
                if coupon['percent_discount']:
                    discount += applicable_items_amount * coupon['percent_discount'] * 0.01
                else:
                    discount += coupon['amount_discount']

            possible_discounts.append(discount)
        total_discount += max(possible_discounts)
    return total_discount



# integration tests
coupon_test_1 = {'category': 'fruit',
                  'percent_discount': 10,
                  'amount_discount': None,
                  'minimum_num_items_required': 2,
                  'minimum_amount_required': 10.00
                }
# Example Cart
cart_test_1 = [{'price': 100.00, 'category': 'fruit'},
               {'price': 20.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert calculate_totals(cart_test_1, coupon_test_1) == 295, 'simple test 1 case does not pass'


# unit tests
coupon_test_2 = {'category': 'fruit',
                  'percent_discount': 10,
                  'amount_discount': None,
                  'minimum_num_items_required': 2,
                  'minimum_amount_required': 10.00
                }
# Example Cart
cart_test_2 = [{'price': 100.00, 'category': 'fruit'},
               {'price': 20.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert apply_coupons(cart_test_2, coupon_test_2) == 30


coupon_test_3 = {'category': 'fruit',
                  'percent_discount': None,
                  'amount_discount': 10,
                  'minimum_num_items_required': 2,
                  'minimum_amount_required': 10.00
                }
# Example Cart
cart_test_3 = [{'price': 100.00, 'category': 'fruit'},
               {'price': 20.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert apply_coupons(cart_test_3, coupon_test_3) == 10

# another coupon category
coupon_test_4 = {'category': 'toy',
                  'percent_discount': None,
                  'amount_discount': 10,
                  'minimum_num_items_required': 1,
                  'minimum_amount_required': 10.00
                }
# Example Cart
cart_test_4 = [{'price': 100.00, 'category': 'fruit'},
               {'price': 20.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert apply_coupons(cart_test_4, coupon_test_4) == 10

coupon_test_5 = {'category': 'toy',
                  'percent_discount': 10,
                  'amount_discount': None,
                  'minimum_num_items_required': 1,
                  'minimum_amount_required': 10.00
                }
# Example Cart
cart_test_5 = [{'price': 100.00, 'category': 'fruit'},
               {'price': 20.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert apply_coupons(cart_test_5, coupon_test_5) == 2


coupon_test_6 = {'category': 'fruit',
                  'percent_discount': 10,
                  'amount_discount': None,
                  'minimum_num_items_required': 3,
                  'minimum_amount_required': 10.00
                }
# Example Cart
cart_test_6 = [{'price': 100.00, 'category': 'fruit'},
               {'price': 20.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert apply_coupons(cart_test_6, coupon_test_6) == 0

coupon_test_7 = {'category': 'fruit',
                  'percent_discount': 10,
                  'amount_discount': None,
                  'minimum_num_items_required': 1,
                  'minimum_amount_required': 40000.00
                }
# Example Cart
cart_test_7 = [{'price': 100.00, 'category': 'fruit'},
               {'price': 20.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert apply_coupons(cart_test_7, coupon_test_7) == 0



print('multi coupon test=====================================')
# multi coupon
coupon_test_10 = [
    {'category': ['clothing', 'toy'],
     'percent_discount': 10,
     'amount_discount': None,
     'minimum_num_items_required': None,
     'minimum_amount_required': None
     },
    {'category': 'fruit',
     'percent_discount': 15,
     'amount_discount': None,
     'minimum_num_items_required': 2,
     'minimum_amount_required': 10.00
     }
]
cart_test_10 = [
    {'price': 10, 'category': 'fruit'},
    {'price': 20.00, 'category': 'toy'},
    {'price': 5.00, 'category': 'clothing'},
    {'price': 90.00, 'category': 'fruit'}
]
assert calculate_totals(cart_test_10, coupon_test_10) == 18 + 5 + 85, 'test amount discount multi category does not pass'
