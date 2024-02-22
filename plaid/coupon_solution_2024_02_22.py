def some_function(cart, coupon):
    '''
    :param cart: some array of dicts
    :param coupon: some dict
    :return: int

    so coupon1 * item 1 + coupon2 * item 2 + item 3 + item 4 = item 1 ... + item 4 - (1 - coupon1) * item1 + (1 - coupon2) * item2
    '''

    initial_cart_total = sum([item['price'] for item in cart])
    discount = calculate_coupons(coupon, cart)
    print('discount: ', discount)
    return initial_cart_total - discount


def calculate_coupons(coupon, cart_items):
    discount = 0
    eligible_item = [item for item in cart_items if item['category'] == coupon['category']]
    eligible_item_len = len(eligible_item)
    eligible_item_sum = sum(item['price'] for item in eligible_item)

    if (coupon['minimum_num_items_required'] == None or coupon['minimum_num_items_required'] <= eligible_item_len) and (coupon['minimum_amount_required'] or coupon['minimum_amount_required'] <= eligible_item_sum):
        for elig_item in eligible_item:
            if coupon['percent_discount']:
                discount += coupon['percent_discount'] * 0.01 * elig_item['price']
            if coupon['amount_discount'] and elig_item['price'] > coupon['amount_discount']:
                discount += coupon['amount_discount']

    return discount



#integration tests
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

assert calculate_coupons(coupon_test_1, cart_test_1) == 30

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

# print('test 6 ==========================')
# # multi coupon
# coupon_test_6 = [
#     {'category': ['clothing', 'toy'],
#      'percent_discount': None,
#      'amount_discount': 6,
#      'minimum_num_items_required': None,
#      'minimum_amount_required': None
#      },
#     {'category': 'fruit',
#      'percent_discount': 15,
#      'amount_discount': None,
#      'minimum_num_items_required': 2,
#      'minimum_amount_required': 10.00
#      }
# ]
# cart_test_6 = [
#     {'price': 10, 'category': 'fruit'},
#     {'price': 20.00, 'category': 'toy'},
#     {'price': 5.00, 'category': 'clothing'},
#     {'price': 90.00, 'category': 'fruit'}
# ]
# assert some_function(cart_test_6, coupon_test_6) == 14 + 5 + 85, 'test amount discount multi cateegory does not pass'
#
# print('test 65 ==========================')
# coupon_test_65 = [
#     {'category': ['clothing', 'toy'],
#      'percent_discount': 10,
#      'amount_discount': None,
#      'minimum_num_items_required': None,
#      'minimum_amount_required': None
#      },
#     {'category': 'fruit',
#      'percent_discount': 15,
#      'amount_discount': None,
#      'minimum_num_items_required': 2,
#      'minimum_amount_required': 10.00
#      }
# ]
# cart_test_65 = [
#     {'price': 10, 'category': 'fruit'},
#     {'price': 20.00, 'category': 'toy'},
#     {'price': 50.00, 'category': 'clothing'},
#     {'price': 90.00, 'category': 'fruit'}
# ]
# assert some_function(cart_test_65,
#                      coupon_test_65) == 85 + 20 + 45, 'test amount discount multi cateegory with percent does not pass'
#
#
#
# # unit tests for calculating initial totals
# cart_test_1 = [{'price': 100.00, 'category': 'fruit'},
#                {'price': 20.00, 'category': 'toy'},
#                {'price': 5.00, 'category': 'clothing'},
#                {'price': 200.00, 'category': 'fruit'}
#                ]
# assert calculate_totals(cart_test_1) == {
#     "fruit": (300, 2),
#     "toy": (20.00, 1),
#     "clothing": (5.00, 1)
# }
#
# cart_test_2 = [{'price': 100.00, 'category': 'fruit'},
#                {'price': 0.00, 'category': 'toy'}
#                ]
# assert calculate_totals(cart_test_2) == {
#     "fruit": (100.00, 1),
#     "toy": (0.00, 1)
# }
#
# # unit tests for coupon calculation
# coupon_test_8 = [{'category': 'fruit',
#                   'percent_discount': 10,
#                   'amount_discount': None,
#                   'minimum_num_items_required': 2,
#                   'minimum_amount_required': 10.00
#                 }]
# aggregate_totals_1 = {
#     "fruit": (100.00, 1),
#     "toy": (0.00, 1)
# }
# assert calculate_coupons(aggregate_totals_1, coupon_test_8) == {}, 'unit test 1 for coupon calculation did not pass'
#
# coupon_test_9 = [{'category': 'fruit',
#                   'percent_discount': 10,
#                   'amount_discount': None,
#                   'minimum_num_items_required': 2,
#                   'minimum_amount_required': 10.00
#                 }]
# aggregate_totals_2 = {
#     "fruit": (100.00, 2),
#     "toy": (0.00, 1)
# }
#
# assert calculate_coupons(aggregate_totals_2, coupon_test_9) == {"fruit": 10}, 'unit test 2 for coupon calculation did not pass'
#
# coupon_test_10 = [{'category': 'fruit',
#                   'percent_discount': None,
#                   'amount_discount': 15,
#                   'minimum_num_items_required': 2,
#                   'minimum_amount_required': 10.00
#                 }]
# aggregate_totals_3 = {
#     "fruit": (100.00, 2),
#     "toy": (0.00, 1)
# }
#
# assert calculate_coupons(aggregate_totals_3, coupon_test_10) == {"fruit": 15}, 'unit test 3 for coupon calculation did not pass'
#
# coupon_test_115 = [{'category': ['fruit', 'clothing'],
#                   'percent_discount': 10,
#                   'amount_discount': None,
#                   'minimum_num_items_required': 2,
#                   'minimum_amount_required': 10.00
#                 }]
# aggregate_totals_45 = {
#     "fruit": (100.00, 2),
#     "toy": (200.00, 2),
#     "clothing": (105, 1)
# }
#
# assert calculate_coupons(aggregate_totals_45, coupon_test_115) == {"fruit": 10}, 'unit test 45 (multi category) for coupon calculation did not pass'
#
#
# coupon_test_12 = [{'category': ['fruit', 'toy'],
#                   'percent_discount': None,
#                   'amount_discount': 15,
#                   'minimum_num_items_required': 2,
#                   'minimum_amount_required': 10.00
#                 }]
# aggregate_totals_5 = {
#     "fruit": (100.00, 2),
#     "toy": (200.00, 2),
#     "clothing": [105,1]
# }
# # if the amounts are equal, our logic codes that both apply
# assert calculate_coupons(aggregate_totals_5, coupon_test_12) == {"fruit": 15, 'toy': 15}, 'unit test 5 (multi category) for coupon calculation did not pass'
#
# # unit testing for apply coupons
# coupons_to_apply_1 = {"fruit": 15, 'toy': 15}
# aggregate_totals_6 = {
#     "fruit": (100.00, 2),
#     "toy": (200.00, 2),
#     "clothing": (105,1)
# }
# # if the amounts are equal, our logic codes that both apply
# assert apply_coupons(coupons_to_apply_1, aggregate_totals_6) == 375, 'unit test 1 for applying coupons did not pass'
#
#
# # unit testing for apply coupons
# coupons_to_apply_2 = {"fruit": 25}
# aggregate_totals_7 = {
#     "fruit": (100.00, 2),
#     "toy": (200.00, 2),
#     "clothing": (105,1)
# }
# # if the amounts are equal, our logic codes that both apply
# assert apply_coupons(coupons_to_apply_2, aggregate_totals_7) == 380, 'unit test 2 applying coupons did not pass'
#
#
