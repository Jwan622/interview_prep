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
#

def calculate_total(cart, coupon):
    original_sum = sum(item['price'] for item in cart)
    discounts = 0

    coupons = [coupon] if isinstance(coupon, dict) else coupon
    for coupon in coupons:
        possible_discounts = []
        coupon_categories = [coupon['category']] if isinstance(coupon['category'], str) else coupon['category']
        for category in coupon_categories:
            print('cateogry', category)
            applicable_items = [cart_item for cart_item in cart if cart_item['category'] == category]
            len_applicable_items = len(applicable_items)
            applicable_items_total = sum(item['price'] for item in applicable_items)

            if (coupon['minimum_num_items_required'] is None or len_applicable_items >= coupon['minimum_num_items_required']) and (coupon['minimum_amount_required'] is None or applicable_items_total >= coupon['minimum_amount_required']):
                if coupon['percent_discount']:
                    possible_discounts.append(applicable_items_total * coupon['percent_discount'] * 0.01)
                elif coupon['amount_discount']:
                    possible_discounts.append(coupon['amount_discount'])
        print(possible_discounts)

        discounts += max(possible_discounts, default=0)
        print('discounts', discounts)
    return original_sum - discounts

coupon_1 = { 'category': 'fruit',
   'percent_discount': 15,
   'amount_discount': None,
   'minimum_num_items_required': 2,
   'minimum_amount_required': 10.00
  }
# Example Cart
cart_1 = [ {'price': 2.00, 'category': 'fruit'},
   {'price': 20.00, 'category': 'toy'},
   {'price': 5.00, 'category': 'clothing'},
   {'price': 8.00, 'category': 'fruit'}
]

assert calculate_total(cart_1, coupon_1) == 8.50 + 20 + 5


coupon_1 = { 'category': 'fruit',
   'percent_discount': None,
   'amount_discount': 2,
   'minimum_num_items_required': 2,
   'minimum_amount_required': 10.00
  }
# Example Cart
cart_1 = [ {'price': 2.00, 'category': 'fruit'},
   {'price': 20.00, 'category': 'toy'},
   {'price': 5.00, 'category': 'clothing'},
   {'price': 8.00, 'category': 'fruit'}
]

assert calculate_total(cart_1, coupon_1) == 8 + 20 + 5



coupon_1 = { 'category': 'fruit',
   'percent_discount': None,
   'amount_discount': 2,
   'minimum_num_items_required': 3,
   'minimum_amount_required': 10.00
  }
# Example Cart
cart_1 = [ {'price': 2.00, 'category': 'fruit'},
   {'price': 20.00, 'category': 'toy'},
   {'price': 5.00, 'category': 'clothing'},
   {'price': 8.00, 'category': 'fruit'}
]

assert calculate_total(cart_1, coupon_1) == 10 + 20 + 5



coupon_1 = { 'category': 'fruit',
   'percent_discount': 2,
   'amount_discount': None,
   'minimum_num_items_required': 3,
   'minimum_amount_required': 10.00
  }
# Example Cart
cart_1 = [ {'price': 2.00, 'category': 'fruit'},
   {'price': 20.00, 'category': 'toy'},
   {'price': 5.00, 'category': 'clothing'},
   {'price': 8.00, 'category': 'fruit'}
]

assert calculate_total(cart_1, coupon_1) == 10 + 20 + 5

coupon_1 = { 'category': 'fruit',
   'percent_discount': 2,
   'amount_discount': None,
   'minimum_num_items_required': 2,
   'minimum_amount_required': 50.00
  }
# Example Cart
cart_1 = [ {'price': 2.00, 'category': 'fruit'},
   {'price': 20.00, 'category': 'toy'},
   {'price': 5.00, 'category': 'clothing'},
   {'price': 8.00, 'category': 'fruit'}
]

assert calculate_total(cart_1, coupon_1) == 10 + 20 + 5

coupon_1 = { 'category': 'toy',
   'percent_discount': None,
   'amount_discount': 2,
   'minimum_num_items_required': 1,
   'minimum_amount_required': 20.00
  }
# Example Cart
cart_1 = [ {'price': 2.00, 'category': 'fruit'},
   {'price': 20.00, 'category': 'toy'},
   {'price': 5.00, 'category': 'clothing'},
   {'price': 8.00, 'category': 'fruit'}
]

assert calculate_total(cart_1, coupon_1) == 10 + 18 + 5



print('multi coupon test=====================================')
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
assert calculate_total(cart_test_10, coupon_test_10) == 18 + 5 + 85, 'test amount discount multi category does not pass'
