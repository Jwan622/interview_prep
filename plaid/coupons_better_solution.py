def some_function(cart, coupon):
    cart_total = sum([item['price'] for item in cart])

    coupons = [coupon] if isinstance(coupon, dict) else coupon
    total_discount = 0

    for coupon in coupons:
        categories = coupon['category'] if isinstance(coupon['category'], list) else [coupon['category']]
        print('categories: ', categories)
        category_discounts = []
        for category in categories:
            discountable_items = [item for item in cart if item['category'] == category]
            print(discountable_items)
            discountable_items_len = len(discountable_items)
            discountable_items_amt = sum([item['price'] for item in discountable_items])

            print('coupon: ' ,coupon)
            if (coupon['minimum_num_items_required'] is None or coupon['minimum_num_items_required'] <= discountable_items_len) and (coupon['minimum_amount_required'] is None or coupon['minimum_amount_required'] <= discountable_items_amt):
                if coupon['percent_discount']:
                    category_discounts.append((category, coupon['percent_discount'] * 0.01 * discountable_items_amt))
                elif coupon['amount_discount']:
                    category_discounts.append((category, coupon['amount_discount']))

        # category_discounts.sort(key=lambda i: i[1], reverse=True)

        print('category_discounts:', category_discounts)
        if category_discounts:
            total_discount += max(category_discounts, key=lambda x: x[1])[1]

    print('discount: ', total_discount)
    print('cart_total: ', cart_total)
    return cart_total - total_discount

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

print('test 6 ==========================')
# multi coupon
coupon_test_6 = [
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
cart_test_6 = [
    {'price': 10, 'category': 'fruit'},
    {'price': 20.00, 'category': 'toy'},
    {'price': 5.00, 'category': 'clothing'},
    {'price': 90.00, 'category': 'fruit'}
]
assert some_function(cart_test_6, coupon_test_6) == 18 + 5 + 85, 'test amount discount multi cateegory does not pass'

