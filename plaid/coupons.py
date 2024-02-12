# Example Coupon
#
# Exactly one of percent_discount and amount_discount will be non-null (error if not).
# The two 'minimum_...' values can each be null or non-null.
# coupon = { 'category': 'fruit',
#    'percent_discount': 15,
#    'amount_discount': None,
#    'minimum_num_items_required': 2,
#    'minimum_amount_required': 10.00
#   }
# # Example Cart
# cart = [ {'price': 2.00, 'category': 'fruit'},
#    {'price': 20.00, 'category': 'toy'},
#    {'price': 5.00, 'category': 'clothing'},
#    {'price': 8.00, 'category': 'fruit'}
# ]

def calculate_totals(cart):
    aggregate_totals_per_category = {}
    for cart_item in cart:
        if cart_item['category'] not in aggregate_totals_per_category:
            aggregate_totals_per_category[cart_item['category']] = (cart_item['price'], 1)
        else:
            aggregate_totals_per_category[cart_item['category']] = (
            aggregate_totals_per_category[cart_item['category']][0] + cart_item['price'],
            aggregate_totals_per_category[cart_item['category']][1] + 1)

    return aggregate_totals_per_category


def calculate_coupons(aggregate_totals_per_category, coupons):
    coupon_amounts_to_apply = {}
    for coupon in coupons:
        if isinstance(coupon['category'], str):
            coupon['category'] = [coupon['category']]

        percent_discount = (coupon['percent_discount'] or 0) * 0.01
        amount_discount = coupon['amount_discount']

        if len(set(coupon['category']) - set(aggregate_totals_per_category.keys())) > 0:
            continue

        categories_to_discount = [coupon['category']] if isinstance(coupon['category'], str) else coupon['category']

        for category in categories_to_discount:
            if aggregate_totals_per_category[category][0] < (coupon['minimum_amount_required'] or 0):
                continue
            if aggregate_totals_per_category[category][1] < (coupon['minimum_num_items_required'] or 0):
                continue

            if category not in coupon_amounts_to_apply:
                coupon_amounts_to_apply[category] = 0

            if percent_discount:
                coupon_amounts_to_apply[category] += aggregate_totals_per_category[category][0] * percent_discount
            else:
                coupon_amounts_to_apply[category] += min(amount_discount, aggregate_totals_per_category[category][0])

            # take the biggest discount if it's a multi category coupon
            if len(categories_to_discount) > 1:
                coupon_amounts_to_apply = {key: value for key, value in coupon_amounts_to_apply.items() if
                                           value == max(coupon_amounts_to_apply.values())}

    return coupon_amounts_to_apply


def apply_coupons(coupon_amounts_to_apply, aggregate_totals_per_category):
    total = 0
    if coupon_amounts_to_apply:
        for key, item in aggregate_totals_per_category.items():
            total += item[0] - coupon_amounts_to_apply.get(key, 0)
    else:
        for key, item in aggregate_totals_per_category.items():
            total += item[0]
    return total


def some_function(cart, coupons):
    # section 0, convert single coupons into an array with one coupon
    if isinstance(coupons, dict):
        coupons = [coupons]

    # section 1:
    # let's build up totals, amount and number of items in a tuple
    # data should look like:
    # {
    #     "fruit": (total_amoount, number_of_items),
    #     "toy": total_amount, number_of_items

    # }
    aggregate_totals_per_category = calculate_totals(cart)

    # section 2
    # calculate coupons and add a third field in the tuple to represent amount to discount, total is unchanged here. remember the tuple is (total, count of cart items cateogry, amount_to_discount)
    #  data should look like:
    # {
    #     "fruit": (total_amoount, number_of_items, amount_to_discount),
    #     "toy": total_amount, number_of_items, amount_to_discount

    # }
    coupon_amounts_to_apply = calculate_coupons(aggregate_totals_per_category, coupons)

    # section 3
    # apply coupons
    return apply_coupons(coupon_amounts_to_apply, aggregate_totals_per_category)

# integration tests
print('test 1 ==========================')
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
assert some_function(cart_test_1, coupon_test_1) == 295, 'simple test 1 case does not pass'

print('test 2============================================================')
coupon_test_2 = {'category': 'fruit',
                  'percent_discount': 10,
                  'amount_discount': None,
                  'minimum_num_items_required': 2,
                  'minimum_amount_required': 10.00
                  }
# Example Cart
cart_test_2 = [{'price': 0, 'category': 'fruit'},
               {'price': 20.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert some_function(cart_test_2, coupon_test_2) == 205, 'simple test 2 case does not pass'

print('test 2.5============================================================')
coupon_test_25 = {'category': 'fruit',
                   'percent_discount': None,
                   'amount_discount': 6,
                   'minimum_num_items_required': 2,
                   'minimum_amount_required': 10.00
                 }
# Example Cart
cart_test_25 = [{'price': 0, 'category': 'fruit'},
                {'price': 20.00, 'category': 'toy'},
                {'price': 5.00, 'category': 'clothing'},
                {'price': 200.00, 'category': 'fruit'}
                ]
assert some_function(cart_test_25,
                     coupon_test_25) == 194 + 5 + 20, 'simple test 2.5 case does not pass for fixed amounts'

print('test 3==========================================')
coupon_test_3 = {'category': 'toy',
                  'percent_discount': 20,
                  'amount_discount': None,
                  'minimum_num_items_required': 2,
                  'minimum_amount_required': 10.00
                }
# Example Cart
cart_test_3 = [{'price': 100, 'category': 'fruit'},
               {'price': 20.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert some_function(cart_test_3, coupon_test_3) == 325, 'simple test 3 case does not pass'

print('test 35==========================')
coupon_test_35 = {'category': 'toy',
                   'percent_discount': 20,
                   'amount_discount': None,
                   'minimum_num_items_required': 4,
                   'minimum_amount_required': 10.00
                }
# Example Cart
cart_test_35 = [{'price': 100, 'category': 'fruit'},
                {'price': 30.00, 'category': 'toy'},
                {'price': 20.00, 'category': 'toy'},
                {'price': 40.00, 'category': 'toy'},
                {'price': 10.00, 'category': 'toy'},
                {'price': 5.00, 'category': 'clothing'},
                {'price': 200.00, 'category': 'fruit'}
                ]
assert some_function(cart_test_35,
                     coupon_test_35) == 305 + 80, 'simple test 35 where all items are valid toys to discount case does not pass'

print('test 4 ==========================')
coupon_test_4 = {'category': 'toy',
                  'percent_discount': 20,
                  'amount_discount': None,
                  'minimum_num_items_required': 4,
                  'minimum_amount_required': 10.00
                }
# Example Cart
cart_test_4 = [{'price': 100, 'category': 'fruit'},
               {'price': 30.00, 'category': 'toy'},
               {'price': 20.00, 'category': 'toy'},
               {'price': 40.00, 'category': 'toy'},
               {'price': 10.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert some_function(cart_test_4,
                     coupon_test_4) == 305 + 80, 'simple test 4 where all category matched items are valid to discount'

print('test 5 ==========================')
coupon_test_5 = {'category': 'this cateogyr does not exist',
                  'percent_discount': 20,
                  'amount_discount': None,
                  'minimum_num_items_required': 2,
                  'minimum_amount_required': 10.00
                  }
# Example Cart
cart_test_5 = [{'price': 100, 'category': 'fruit'},
               {'price': 20.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert some_function(cart_test_5, coupon_test_5) == 325, 'simple test 5 case does not pass'

print('test 6 ==========================')
# multi coupon
coupon_test_6 = [
    {'category': ['clothing', 'toy'],
     'percent_discount': None,
     'amount_discount': 6,
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
cart_test_6 = [
    {'price': 10, 'category': 'fruit'},
    {'price': 20.00, 'category': 'toy'},
    {'price': 5.00, 'category': 'clothing'},
    {'price': 90.00, 'category': 'fruit'}
]
assert some_function(cart_test_6, coupon_test_6) == 14 + 5 + 85, 'test amount discount multi cateegory does not pass'

print('test 65 ==========================')
coupon_test_65 = [
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
cart_test_65 = [
    {'price': 10, 'category': 'fruit'},
    {'price': 20.00, 'category': 'toy'},
    {'price': 50.00, 'category': 'clothing'},
    {'price': 90.00, 'category': 'fruit'}
]
assert some_function(cart_test_65,
                     coupon_test_65) == 85 + 20 + 45, 'test amount discount multi cateegory with percent does not pass'



# unit tests
cart_test_1 = [{'price': 100.00, 'category': 'fruit'},
               {'price': 20.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert calculate_totals(cart_test_1) == {
    "fruit": (300, 2),
    "toy": (20.00, 1),
    "clothing": (5.00, 1)
}

cart_test_2 = [{'price': 100.00, 'category': 'fruit'},
               {'price': 0.00, 'category': 'toy'}
               ]
assert calculate_totals(cart_test_2) == {
    "fruit": (100.00, 1),
    "toy": (0.00, 1)
}

# unit tests for coupon calculation
coupon_test_8 = [{'category': 'fruit',
                  'percent_discount': 10,
                  'amount_discount': None,
                  'minimum_num_items_required': 2,
                  'minimum_amount_required': 10.00
                }]
aggregate_totals_1 = {
    "fruit": (100.00, 1),
    "toy": (0.00, 1)
}
assert calculate_coupons(aggregate_totals_1, coupon_test_8) == {}, 'unit test 1 for coupon calculation did not pass'

coupon_test_9 = [{'category': 'fruit',
                  'percent_discount': 10,
                  'amount_discount': None,
                  'minimum_num_items_required': 2,
                  'minimum_amount_required': 10.00
                }]
aggregate_totals_2 = {
    "fruit": (100.00, 2),
    "toy": (0.00, 1)
}

assert calculate_coupons(aggregate_totals_2, coupon_test_9) == {"fruit": 10}, 'unit test 2 for coupon calculation did not pass'

coupon_test_10 = [{'category': 'fruit',
                  'percent_discount': None,
                  'amount_discount': 15,
                  'minimum_num_items_required': 2,
                  'minimum_amount_required': 10.00
                }]
aggregate_totals_3 = {
    "fruit": (100.00, 2),
    "toy": (0.00, 1)
}

assert calculate_coupons(aggregate_totals_3, coupon_test_10) == {"fruit": 15}, 'unit test 3 for coupon calculation did not pass'

coupon_test_115 = [{'category': ['fruit', 'clothing'],
                  'percent_discount': 10,
                  'amount_discount': None,
                  'minimum_num_items_required': 2,
                  'minimum_amount_required': 10.00
                }]
aggregate_totals_45 = {
    "fruit": (100.00, 2),
    "toy": (200.00, 2),
    "clothing": (105, 1)
}

assert calculate_coupons(aggregate_totals_45, coupon_test_115) == {"fruit": 10}, 'unit test 45 (multi category) for coupon calculation did not pass'


coupon_test_12 = [{'category': ['fruit', 'toy'],
                  'percent_discount': None,
                  'amount_discount': 15,
                  'minimum_num_items_required': 2,
                  'minimum_amount_required': 10.00
                }]
aggregate_totals_5 = {
    "fruit": (100.00, 2),
    "toy": (200.00, 2),
    "clothing": [105,1]
}
# if the amounts are equal, our logic codes that both apply
assert calculate_coupons(aggregate_totals_5, coupon_test_12) == {"fruit": 15, 'toy': 15}, 'unit test 5 (multi category) for coupon calculation did not pass'
