def some_function(cart, coupon):
    cart_total = sum([item['price'] for item in cart])
    discount = 0

    discountable_items = [item for item in cart if item['category'] == coupon['category']]
    discountable_items_len = len(discountable_items)
    discountable_items_total = sum([item['price'] for item in discountable_items])

    if coupon['minimum_num_items_required'] <= discountable_items_len and coupon['minimum_amount_required'] <= discountable_items_total:
        if coupon['percent_discount']:
            discount += coupon['percent_discount'] * 0.01 * discountable_items_total
        elif coupon['amount_discount']:
            discount += coupon['amount_discount']

    print('discount: ', discount)
    print('cart_total: ', cart_total)
    return cart_total - discount



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

# integration tests
print('test 2 ==========================')
coupon_test_2 = {'category': 'toy',
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
assert some_function(cart_test_2, coupon_test_2) == 300 + 5 + 20, 'simple test 2 case does not pass'

# integration tests
print('test 3 ==========================')
coupon_test_3 = {'category': 'toy',
                  'percent_discount': 10,
                  'amount_discount': None,
                  'minimum_num_items_required': 1,
                  'minimum_amount_required': 10.00
                }
# Example Cart
cart_test_3 = [{'price': 100.00, 'category': 'fruit'},
               {'price': 0.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert some_function(cart_test_3, coupon_test_3) == 300 + 5, 'simple test 3 case does not pass'

# integration tests
print('test 4 ==========================')
coupon_test_4 = {'category': 'fruit',
                  'percent_discount': None,
                  'amount_discount': 20,
                  'minimum_num_items_required': 2,
                  'minimum_amount_required': 10.00
                }
# Example Cart
cart_test_4 = [{'price': 100.00, 'category': 'fruit'},
               {'price': 10.00, 'category': 'toy'},
               {'price': 5.00, 'category': 'clothing'},
               {'price': 200.00, 'category': 'fruit'}
               ]
assert some_function(cart_test_4, coupon_test_4) == 280 + 10 + 5, 'simple test 4 case does not pass'



